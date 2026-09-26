#!/usr/bin/env python3
"""PySide6 desktop frontend for the Gemini Game Voice Studio.

The GUI is intentionally a thin presentation layer over voice_studio.py. Rate limiting,
retry/backoff, token accounting, registry handling and provider operations stay in the
shared backend so the terminal and Windows UI cannot silently diverge.
"""

from __future__ import annotations

import json
import math
import os
import sys
import time
import traceback
from collections import Counter
from pathlib import Path
from typing import Any, Callable

try:
    from PySide6.QtCore import QObject, QRunnable, QThreadPool, QUrl, Signal, Slot, Qt
    from PySide6.QtGui import QAction, QCloseEvent, QFont
    from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
    from PySide6.QtWidgets import (
        QApplication,
        QComboBox,
        QDialog,
        QDialogButtonBox,
        QFileDialog,
        QFormLayout,
        QFrame,
        QGridLayout,
        QGroupBox,
        QHBoxLayout,
        QLabel,
        QLineEdit,
        QListWidget,
        QListWidgetItem,
        QMainWindow,
        QMessageBox,
        QPlainTextEdit,
        QProgressBar,
        QPushButton,
        QScrollArea,
        QSlider,
        QSpinBox,
        QDoubleSpinBox,
        QSplitter,
        QStatusBar,
        QTabWidget,
        QTableWidget,
        QTableWidgetItem,
        QTextEdit,
        QToolBar,
        QVBoxLayout,
        QWidget,
        QHeaderView,
        QAbstractItemView,
    )
except ImportError as exc:
    raise SystemExit(
        "PySide6 is not installed. Run: "
        "python -m pip install -r requirements-voice-gui.txt"
    ) from exc

import voice_pipeline as vp
import voice_studio as vs


APP_TITLE = "Gemini Game Voice Studio"
WINDOW_MIN_WIDTH = 1180
WINDOW_MIN_HEIGHT = 760


class WorkerSignals(QObject):
    result = Signal(str, object)
    error = Signal(str, str)
    finished = Signal(str)
    message = Signal(str, str)


class Worker(QRunnable):
    def __init__(
        self,
        title: str,
        fn: Callable[..., Any],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__()
        self.title = title
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()
    def run(self) -> None:
        def emit_message(message: str) -> None:
            self.signals.message.emit(self.title, message)

        try:
            result = self.fn(emit_message, *self.args, **self.kwargs)
        except Exception:
            self.signals.error.emit(self.title, traceback.format_exc())
        else:
            self.signals.result.emit(self.title, result)
        finally:
            self.signals.finished.emit(self.title)


class RuntimeSettingsDialog(QDialog):
    def __init__(self, settings: dict[str, Any], parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Rate limiting & retry settings")
        self.setMinimumWidth(520)
        self.settings = dict(settings)

        layout = QVBoxLayout(self)
        note = QLabel(
            "Client-side guardrails. Google AI Studio remains authoritative for your "
            "project/model limits. TPM = 0 means no local TPM enforcement."
        )
        note.setWordWrap(True)
        layout.addWidget(note)

        form = QFormLayout()
        self.preview_rpm = self._spin(int(settings["preview_rpm"]), 1, 1000)
        self.preview_tpm = self._spin(int(settings["preview_tpm"]), 0, 1_000_000_000)
        self.final_rpm = self._spin(int(settings["final_rpm"]), 1, 1000)
        self.final_tpm = self._spin(int(settings["final_tpm"]), 0, 1_000_000_000)
        self.voice_rpm = self._spin(int(settings["voice_api_rpm"]), 1, 1000)
        self.max_retries = self._spin(int(settings["max_retries"]), 0, 20)
        self.retry_base = self._double(
            float(settings["retry_base_delay_seconds"]), 0.0, 600.0
        )
        self.permission_delay = self._double(
            float(settings["permission_retry_delay_seconds"]), 0.0, 600.0
        )
        self.safety_margin = self._double(
            float(settings["rate_safety_margin_seconds"]), 0.0, 30.0
        )
        self.demo_count = self._spin(int(settings["demo_line_count"]), 1, 20)

        form.addRow("Preview RPM", self.preview_rpm)
        form.addRow("Preview input TPM", self.preview_tpm)
        form.addRow("Final RPM", self.final_rpm)
        form.addRow("Final input TPM", self.final_tpm)
        form.addRow("Voices API RPM", self.voice_rpm)
        form.addRow("Maximum retries", self.max_retries)
        form.addRow("Base retry delay (sec)", self.retry_base)
        form.addRow("403 retry delay (sec)", self.permission_delay)
        form.addRow("Rate safety margin (sec)", self.safety_margin)
        form.addRow("Default demo lines", self.demo_count)
        layout.addLayout(form)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    @staticmethod
    def _spin(value: int, minimum: int, maximum: int) -> QSpinBox:
        widget = QSpinBox()
        widget.setRange(minimum, maximum)
        widget.setValue(value)
        widget.setGroupSeparatorShown(True)
        return widget

    @staticmethod
    def _double(value: float, minimum: float, maximum: float) -> QDoubleSpinBox:
        widget = QDoubleSpinBox()
        widget.setRange(minimum, maximum)
        widget.setDecimals(1)
        widget.setSingleStep(0.5)
        widget.setValue(value)
        return widget

    def values(self) -> dict[str, Any]:
        result = dict(self.settings)
        result.update(
            {
                "preview_rpm": self.preview_rpm.value(),
                "preview_tpm": self.preview_tpm.value(),
                "final_rpm": self.final_rpm.value(),
                "final_tpm": self.final_tpm.value(),
                "voice_api_rpm": self.voice_rpm.value(),
                "max_retries": self.max_retries.value(),
                "retry_base_delay_seconds": self.retry_base.value(),
                "permission_retry_delay_seconds": self.permission_delay.value(),
                "rate_safety_margin_seconds": self.safety_margin.value(),
                "demo_line_count": self.demo_count.value(),
            }
        )
        return result


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.config = vp.load_config()
        self.settings = vs.load_runtime_settings()
        self.backend = vs.VoiceStudio(self.config, self.settings)
        self.registry: dict[str, Any] = {}
        self.manifest: list[dict[str, Any]] = []
        self.current_speaker: str | None = None
        self.thread_pool = QThreadPool.globalInstance()
        self.busy_count = 0
        self.active_worker: Worker | None = None
        self.active_result_handler: Callable[[Any], None] | None = None
        self.active_job_started = 0.0
        self.active_job_failed = False

        self.player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.audio_output.setVolume(0.85)
        self.player.setAudioOutput(self.audio_output)
        self.player.errorOccurred.connect(self._media_error)
        self.player.positionChanged.connect(self._media_position_changed)
        self.player.durationChanged.connect(self._media_duration_changed)
        self.player.playbackStateChanged.connect(self._media_state_changed)
        self.current_audio_path: Path | None = None

        self.setWindowTitle(APP_TITLE)
        self.setMinimumSize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        self.resize(1440, 900)

        self._build_ui()
        self._apply_style()
        self.reload_data(select_speaker="mc")

    # ---------- UI construction ----------

    def _build_ui(self) -> None:
        self._build_toolbar()
        self.setStatusBar(QStatusBar(self))

        central = QWidget()
        root = QVBoxLayout(central)
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(10)

        self.summary_bar = self._build_summary_bar()
        root.addWidget(self.summary_bar)

        self.operation_banner = QLabel()
        self.operation_banner.setObjectName("operationBanner")
        self.operation_banner.setWordWrap(True)
        self.operation_banner.setVisible(False)
        root.addWidget(self.operation_banner)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setChildrenCollapsible(False)
        splitter.addWidget(self._build_character_pane())
        splitter.addWidget(self._build_workspace())
        splitter.setSizes([350, 1050])
        root.addWidget(splitter, 1)

        self.setCentralWidget(central)

    def _build_toolbar(self) -> None:
        toolbar = QToolBar("Main")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        refresh_action = QAction("Refresh", self)
        refresh_action.setShortcut("F5")
        refresh_action.triggered.connect(lambda: self.reload_data(self.current_speaker))
        toolbar.addAction(refresh_action)

        settings_action = QAction("Rate settings", self)
        settings_action.triggered.connect(self.open_settings)
        toolbar.addAction(settings_action)

        usage_action = QAction("Usage dashboard", self)
        usage_action.triggered.connect(lambda: self.tabs.setCurrentWidget(self.usage_tab))
        toolbar.addAction(usage_action)

        toolbar.addSeparator()

        open_folder_action = QAction("Open voice folder", self)
        open_folder_action.triggered.connect(self.open_voice_folder)
        toolbar.addAction(open_folder_action)

    def _build_summary_bar(self) -> QWidget:
        frame = QFrame()
        frame.setObjectName("summaryBar")
        layout = QHBoxLayout(frame)
        layout.setContentsMargins(12, 8, 12, 8)

        self.api_label = QLabel()
        self.character_summary = QLabel()
        self.rate_summary = QLabel()

        layout.addWidget(self.api_label)
        layout.addSpacing(20)
        layout.addWidget(self.character_summary)
        layout.addStretch(1)
        layout.addWidget(self.rate_summary)
        return frame

    def _build_character_pane(self) -> QWidget:
        pane = QWidget()
        layout = QVBoxLayout(pane)
        layout.setContentsMargins(0, 0, 0, 0)

        title = QLabel("Characters")
        title.setObjectName("sectionTitle")
        layout.addWidget(title)

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search token or character name...")
        self.search_box.textChanged.connect(self.refresh_character_list)
        layout.addWidget(self.search_box)

        self.status_filter = QComboBox()
        self.status_filter.addItems(
            [
                "All",
                "Needs voice",
                "Audition",
                "Approved",
                "Disabled",
                "Aliases",
            ]
        )
        self.status_filter.currentIndexChanged.connect(self.refresh_character_list)
        layout.addWidget(self.status_filter)

        self.character_list = QListWidget()
        self.character_list.setAlternatingRowColors(True)
        self.character_list.currentItemChanged.connect(self._character_changed)
        layout.addWidget(self.character_list, 1)

        self.next_attention_button = QPushButton("Open next needing attention")
        self.next_attention_button.clicked.connect(self.open_next_attention)
        layout.addWidget(self.next_attention_button)

        return pane

    def _build_workspace(self) -> QWidget:
        self.tabs = QTabWidget()
        self.character_tab = self._build_character_tab()
        self.audition_tab = self._build_audition_tab()
        self.usage_tab = self._build_usage_tab()
        self.log_tab = self._build_log_tab()

        self.tabs.addTab(self.character_tab, "Character & casting")
        self.tabs.addTab(self.audition_tab, "Audition & demos")
        self.tabs.addTab(self.usage_tab, "Usage & tokens")
        self.tabs.addTab(self.log_tab, "Activity log")
        return self.tabs

    def _build_character_tab(self) -> QWidget:
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)

        header = QHBoxLayout()
        self.character_title = QLabel("Select a character")
        self.character_title.setObjectName("pageTitle")
        self.status_badge = QLabel()
        self.status_badge.setObjectName("statusBadge")
        header.addWidget(self.character_title)
        header.addStretch(1)
        header.addWidget(self.status_badge)
        layout.addLayout(header)

        profile_group = QGroupBox("Profile")
        grid = QGridLayout(profile_group)
        self.profile_labels: dict[str, QLabel] = {}
        fields = [
            ("token", "Token"),
            ("line_count", "Dialogue lines"),
            ("voice_id", "Provider voice"),
            ("voice_ref", "Voice alias"),
            ("language", "Language"),
            ("gender", "Gender"),
            ("age", "Casting age"),
            ("accent", "Accent"),
            ("pitch", "Pitch"),
            ("timbre", "Timbre"),
            ("cadence", "Cadence"),
        ]
        for index, (key, caption) in enumerate(fields):
            row = index // 2
            column = (index % 2) * 2
            label = QLabel(caption + ":")
            value = QLabel("-")
            value.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
            grid.addWidget(label, row, column)
            grid.addWidget(value, row, column + 1)
            self.profile_labels[key] = value
        layout.addWidget(profile_group)

        prompt_group = QGroupBox("Voice Design prompt")
        prompt_layout = QVBoxLayout(prompt_group)
        self.prompt_edit = QPlainTextEdit()
        self.prompt_edit.setMinimumHeight(130)
        self.prompt_edit.textChanged.connect(self._prompt_changed)
        prompt_layout.addWidget(self.prompt_edit)

        prompt_buttons = QHBoxLayout()
        self.save_prompt_button = QPushButton("Save prompt & rebuild request")
        self.save_prompt_button.clicked.connect(self.save_prompt)
        self.save_prompt_button.setEnabled(False)
        prompt_buttons.addWidget(self.save_prompt_button)
        prompt_buttons.addStretch(1)
        prompt_layout.addLayout(prompt_buttons)
        layout.addWidget(prompt_group)

        actions = QGroupBox("Casting actions")
        action_layout = QGridLayout(actions)
        self.create_voice_button = QPushButton("Create character voice")
        self.create_voice_button.setObjectName("primaryButton")
        self.create_voice_button.clicked.connect(self.create_voice)
        self.approve_button = QPushButton("Approve voice")
        self.approve_button.clicked.connect(self.approve_voice)
        self.retry_button = QPushButton("Reject / retry voice")
        self.retry_button.clicked.connect(self.retry_voice)
        self.refresh_sample_button = QPushButton("Refresh provider sample")
        self.refresh_sample_button.clicked.connect(self.refresh_design_sample)
        self.play_sample_casting_button = QPushButton("Listen audition sample")
        self.play_sample_casting_button.clicked.connect(self.play_design_sample)
        self.final_button = QPushButton("Generate final audio")
        self.final_button.clicked.connect(self.generate_final_audio)
        action_layout.addWidget(self.create_voice_button, 0, 0)
        action_layout.addWidget(self.approve_button, 0, 1)
        action_layout.addWidget(self.play_sample_casting_button, 1, 0)
        action_layout.addWidget(self.refresh_sample_button, 1, 1)
        action_layout.addWidget(self.retry_button, 2, 0)
        action_layout.addWidget(self.final_button, 2, 1)
        layout.addWidget(actions)

        layout.addStretch(1)
        scroll.setWidget(content)
        return scroll

    def _build_audition_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        player_group = QGroupBox("Audio player")
        player_layout = QVBoxLayout(player_group)

        now_row = QHBoxLayout()
        self.now_playing_label = QLabel("Nothing loaded")
        self.now_playing_label.setObjectName("nowPlaying")
        self.now_playing_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        now_row.addWidget(QLabel("Now loaded:"))
        now_row.addWidget(self.now_playing_label, 1)
        player_layout.addLayout(now_row)

        transport = QHBoxLayout()
        self.player_play_button = QPushButton("Play")
        self.player_play_button.clicked.connect(self._player_play)
        self.player_pause_button = QPushButton("Pause")
        self.player_pause_button.clicked.connect(self.player.pause)
        self.player_stop_button = QPushButton("Stop")
        self.player_stop_button.clicked.connect(self._player_stop)

        self.player_time_label = QLabel("00:00 / 00:00")
        self.player_time_label.setMinimumWidth(100)

        self.player_seek = QSlider(Qt.Orientation.Horizontal)
        self.player_seek.setRange(0, 0)
        self.player_seek.sliderMoved.connect(self.player.setPosition)

        self.player_volume = QSlider(Qt.Orientation.Horizontal)
        self.player_volume.setRange(0, 100)
        self.player_volume.setValue(85)
        self.player_volume.setFixedWidth(120)
        self.player_volume.valueChanged.connect(
            lambda value: self.audio_output.setVolume(value / 100.0)
        )

        transport.addWidget(self.player_play_button)
        transport.addWidget(self.player_pause_button)
        transport.addWidget(self.player_stop_button)
        transport.addWidget(self.player_time_label)
        transport.addWidget(self.player_seek, 1)
        transport.addWidget(QLabel("Volume"))
        transport.addWidget(self.player_volume)
        player_layout.addLayout(transport)
        layout.addWidget(player_group)

        design_group = QGroupBox("Voice Design sample")
        design_layout = QHBoxLayout(design_group)
        self.design_sample_path = QLabel("No local sample")
        self.design_sample_path.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.play_design_button = QPushButton("Load & play")
        self.play_design_button.clicked.connect(self.play_design_sample)
        design_layout.addWidget(self.design_sample_path, 1)
        design_layout.addWidget(self.play_design_button)
        layout.addWidget(design_group)

        demo_controls = QHBoxLayout()
        self.demo_count = QSpinBox()
        self.demo_count.setRange(1, 20)
        self.demo_count.setValue(int(self.settings["demo_line_count"]))
        self.generate_demo_button = QPushButton("Generate representative demos")
        self.generate_demo_button.clicked.connect(self.generate_demos)
        self.play_selected_demo_button = QPushButton("Load & play selected")
        self.play_selected_demo_button.clicked.connect(self.play_selected_demo)
        self.open_demo_folder_button = QPushButton("Open demo folder")
        self.open_demo_folder_button.clicked.connect(self.open_demo_folder)
        demo_controls.addWidget(QLabel("Demo lines:"))
        demo_controls.addWidget(self.demo_count)
        demo_controls.addWidget(self.generate_demo_button)
        demo_controls.addWidget(self.play_selected_demo_button)
        demo_controls.addWidget(self.open_demo_folder_button)
        demo_controls.addStretch(1)
        layout.addLayout(demo_controls)

        self.demo_table = QTableWidget(0, 5)
        self.demo_table.setHorizontalHeaderLabels(
            ["Dialogue ID", "Text", "File", "Size", "Status"]
        )
        self.demo_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.demo_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.demo_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.demo_table.itemSelectionChanged.connect(self._demo_selection_changed)
        self.demo_table.doubleClicked.connect(self.play_selected_demo)
        header = self.demo_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        layout.addWidget(self.demo_table, 1)

        self.player_pause_button.setEnabled(False)
        return widget

    def _build_usage_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        top = QHBoxLayout()
        title = QLabel("Local API usage ledger")
        title.setObjectName("sectionTitle")
        refresh = QPushButton("Refresh usage")
        refresh.clicked.connect(self.refresh_usage)
        top.addWidget(title)
        top.addStretch(1)
        top.addWidget(refresh)
        layout.addLayout(top)

        cards = QHBoxLayout()
        self.usage_requests = self._metric_card("Requests")
        self.usage_success = self._metric_card("Successful")
        self.usage_input = self._metric_card("Input tokens")
        self.usage_audio = self._metric_card("Audio tokens")
        self.usage_total = self._metric_card("Total tokens")
        for card in (
            self.usage_requests,
            self.usage_success,
            self.usage_input,
            self.usage_audio,
            self.usage_total,
        ):
            cards.addWidget(card["frame"])
        layout.addLayout(cards)

        self.usage_table = QTableWidget(0, 7)
        self.usage_table.setHorizontalHeaderLabels(
            ["Time", "Action", "Model", "Speaker", "Status", "Tokens", "Latency"]
        )
        self.usage_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.usage_table.horizontalHeader().setSectionResizeMode(
            2, QHeaderView.ResizeMode.Stretch
        )
        layout.addWidget(self.usage_table, 1)

        return widget

    def _build_log_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        top = QHBoxLayout()
        title = QLabel("Activity")
        title.setObjectName("sectionTitle")
        clear = QPushButton("Clear")
        clear.clicked.connect(lambda: self.log_view.clear())
        top.addWidget(title)
        top.addStretch(1)
        top.addWidget(clear)
        layout.addLayout(top)

        self.log_view = QTextEdit()
        self.log_view.setReadOnly(True)
        self.log_view.setFont(QFont("Consolas", 9))
        layout.addWidget(self.log_view, 1)

        self.progress = QProgressBar()
        self.progress.setRange(0, 0)
        self.progress.setVisible(False)
        layout.addWidget(self.progress)

        return widget

    @staticmethod
    def _metric_card(title: str) -> dict[str, Any]:
        frame = QFrame()
        frame.setObjectName("metricCard")
        layout = QVBoxLayout(frame)
        title_label = QLabel(title)
        title_label.setObjectName("metricTitle")
        value_label = QLabel("0")
        value_label.setObjectName("metricValue")
        layout.addWidget(title_label)
        layout.addWidget(value_label)
        return {"frame": frame, "value": value_label}

    def _apply_style(self) -> None:
        self.setStyleSheet(
            """
            QMainWindow, QWidget {
                background: #15171a;
                color: #e9edf2;
            }
            QToolBar, QStatusBar {
                background: #1c1f23;
                border: none;
            }
            QFrame#summaryBar, QFrame#metricCard, QGroupBox {
                background: #1d2025;
                border: 1px solid #30343a;
                border-radius: 8px;
            }
            QLabel#operationBanner {
                background: #172554;
                border: 1px solid #2563eb;
                border-radius: 7px;
                color: #dbeafe;
                padding: 8px 12px;
                font-weight: 600;
            }
            QGroupBox {
                margin-top: 10px;
                padding: 12px;
                font-weight: 600;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
            QLineEdit, QPlainTextEdit, QTextEdit, QComboBox, QSpinBox,
            QDoubleSpinBox, QListWidget, QTableWidget {
                background: #101215;
                border: 1px solid #343941;
                border-radius: 5px;
                padding: 5px;
                selection-background-color: #2563eb;
            }
            QPushButton {
                background: #2b3037;
                border: 1px solid #3b424c;
                border-radius: 6px;
                padding: 7px 12px;
            }
            QPushButton:hover {
                background: #353b44;
            }
            QPushButton:disabled {
                color: #707780;
                background: #202328;
            }
            QPushButton#primaryButton {
                background: #2563eb;
                border-color: #3b82f6;
                font-weight: 600;
            }
            QPushButton#primaryButton:hover {
                background: #1d4ed8;
            }
            QLabel#pageTitle {
                font-size: 20px;
                font-weight: 700;
            }
            QLabel#sectionTitle {
                font-size: 16px;
                font-weight: 700;
            }
            QLabel#statusBadge {
                background: #2a2f36;
                border-radius: 10px;
                padding: 5px 10px;
                font-weight: 700;
            }
            QLabel#metricTitle {
                color: #9ba3ad;
                font-size: 11px;
            }
            QLabel#metricValue {
                font-size: 20px;
                font-weight: 700;
            }
            QLabel#nowPlaying {
                color: #93c5fd;
                font-weight: 600;
            }
            QTabBar::tab {
                background: #1d2025;
                padding: 8px 14px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background: #2b3037;
                border-bottom: 2px solid #3b82f6;
            }
            """
        )

    # ---------- state ----------

    def reload_data(self, select_speaker: str | None = None) -> None:
        self.registry = vs.load_registry(self.config)
        try:
            self.manifest = vp.load_manifest(self.config)
        except Exception as exc:
            self.manifest = []
            self.log(f"Manifest load failed: {exc}", error=True)

        self.refresh_summary()
        self.refresh_character_list()
        self.refresh_usage()

        target = select_speaker or self.current_speaker
        if target and target in self.registry.get("characters", {}):
            self.select_character(target)
        elif self.character_list.count():
            self.character_list.setCurrentRow(0)

    def refresh_summary(self) -> None:
        characters = self.registry.get("characters", {})
        statuses = Counter(vs.character_status(entry) for entry in characters.values())
        self.api_label.setText(
            "API key: READY"
            if os.environ.get("GEMINI_API_KEY")
            else "API key: NOT SET"
        )
        self.character_summary.setText(
            f"{len(characters)} profiles  |  "
            f"{statuses['APPROVED']} approved  |  "
            f"{statuses['AUDITION']} audition  |  "
            f"{statuses['NEEDS VOICE']} need voice"
        )
        self.rate_summary.setText(
            f"Preview {self.settings['preview_rpm']} RPM"
            f" / {self.settings['preview_tpm'] or '∞'} TPM   •   "
            f"Final {self.settings['final_rpm']} RPM"
            f" / {self.settings['final_tpm'] or '∞'} TPM"
        )

    def refresh_character_list(self) -> None:
        selected = self.current_speaker
        query = self.search_box.text().strip().lower()
        filter_name = self.status_filter.currentText()

        self.character_list.blockSignals(True)
        self.character_list.clear()

        rows = []
        for token, entry in self.registry.get("characters", {}).items():
            status = vs.character_status(entry)
            haystack = f"{token} {entry.get('display_name', '')}".lower()
            if query and query not in haystack:
                continue
            if filter_name == "Needs voice" and status != "NEEDS VOICE":
                continue
            if filter_name == "Audition" and status != "AUDITION":
                continue
            if filter_name == "Approved" and status != "APPROVED":
                continue
            if filter_name == "Disabled" and status != "DISABLED":
                continue
            if filter_name == "Aliases" and not status.startswith("ALIAS->"):
                continue

            priority = {
                "AUDITION": 0,
                "NEEDS VOICE": 1,
                "APPROVED": 2,
                "DISABLED": 4,
            }.get(status, 3)
            rows.append(
                (
                    priority,
                    -int(entry.get("line_count") or 0),
                    token,
                    entry,
                    status,
                )
            )

        rows.sort(key=lambda item: (item[0], item[1], item[2]))
        selected_row = -1
        for index, (_, _, token, entry, status) in enumerate(rows):
            text = (
                f"{entry.get('display_name', token)}\n"
                f"{token}  •  {int(entry.get('line_count') or 0):,} lines  •  {status}"
            )
            item = QListWidgetItem(text)
            item.setData(Qt.ItemDataRole.UserRole, token)
            item.setToolTip(entry.get("design_prompt") or "")
            self.character_list.addItem(item)
            if token == selected:
                selected_row = index

        self.character_list.blockSignals(False)
        if selected_row >= 0:
            self.character_list.setCurrentRow(selected_row)

    def select_character(self, speaker: str) -> None:
        for index in range(self.character_list.count()):
            item = self.character_list.item(index)
            if item.data(Qt.ItemDataRole.UserRole) == speaker:
                self.character_list.setCurrentRow(index)
                return
        self.search_box.clear()
        self.status_filter.setCurrentText("All")
        self.refresh_character_list()
        for index in range(self.character_list.count()):
            item = self.character_list.item(index)
            if item.data(Qt.ItemDataRole.UserRole) == speaker:
                self.character_list.setCurrentRow(index)
                return

    def _character_changed(
        self,
        current: QListWidgetItem | None,
        previous: QListWidgetItem | None,
    ) -> None:
        del previous
        if current is None:
            return
        self.current_speaker = current.data(Qt.ItemDataRole.UserRole)
        self.refresh_current_character()

    def refresh_current_character(self) -> None:
        if not self.current_speaker:
            return
        entry = self.registry["characters"][self.current_speaker]
        profile = entry.get("profile") or {}
        status = vs.character_status(entry)

        self.character_title.setText(
            f"{entry.get('display_name', self.current_speaker)}"
        )
        self.status_badge.setText(status)

        values = {
            "token": self.current_speaker,
            "line_count": f"{int(entry.get('line_count') or 0):,}",
            "voice_id": entry.get("voice_id") or "-",
            "voice_ref": entry.get("voice_ref") or "-",
            "language": entry.get("language_code") or "-",
            "gender": entry.get("gender") or "-",
            "age": profile.get("casting_age") or "-",
            "accent": profile.get("accent") or "-",
            "pitch": profile.get("pitch") or "-",
            "timbre": profile.get("timbre") or "-",
            "cadence": profile.get("cadence") or "-",
        }
        for key, value in values.items():
            self.profile_labels[key].setText(str(value))

        self.prompt_edit.blockSignals(True)
        self.prompt_edit.setPlainText(entry.get("design_prompt") or "")
        self.prompt_edit.blockSignals(False)
        self.save_prompt_button.setEnabled(False)

        has_voice = bool((entry.get("voice_id") or "").strip())
        enabled = bool(entry.get("enabled", True))
        alias = bool((entry.get("voice_ref") or "").strip())
        approved = entry.get("casting_status") == "approved"

        self.create_voice_button.setEnabled(enabled and not alias and not has_voice)
        self.approve_button.setEnabled(has_voice and not approved)
        self.retry_button.setEnabled(has_voice and not alias)
        self.refresh_sample_button.setEnabled(has_voice and not alias)
        self.final_button.setEnabled(has_voice and approved)

        sample = vs.provider_voice_sample_path(self.current_speaker)
        self.design_sample_path.setText(
            str(sample.relative_to(vs.ROOT)) if sample.exists() else "No local sample"
        )
        self.play_design_button.setEnabled(sample.exists())
        self.play_sample_casting_button.setEnabled(sample.exists())
        self.refresh_demo_table()
        if sample.exists() and (
            self.current_audio_path is None
            or self.current_audio_path.name != sample.name
        ):
            self._load_audio(sample, autoplay=False)

    def _prompt_changed(self) -> None:
        if not self.current_speaker:
            return
        original = (
            self.registry["characters"][self.current_speaker].get("design_prompt") or ""
        )
        self.save_prompt_button.setEnabled(
            self.prompt_edit.toPlainText().strip() != original.strip()
        )

    # ---------- background jobs ----------

    def run_job(
        self,
        title: str,
        fn: Callable[..., Any],
        on_result: Callable[[Any], None] | None = None,
    ) -> None:
        if self.busy_count:
            QMessageBox.information(
                self,
                "Voice Studio busy",
                "Another API/background operation is still running. "
                "Wait for it to finish before starting the next one.",
            )
            return

        worker = Worker(title, fn)
        worker.setAutoDelete(False)
        worker.signals.message.connect(self._worker_message)
        worker.signals.error.connect(self._worker_error)
        worker.signals.result.connect(self._worker_result)
        worker.signals.finished.connect(self._worker_finished)

        self.active_worker = worker
        self.active_result_handler = on_result
        self.active_job_started = time.perf_counter()
        self.active_job_failed = False
        self.busy_count = 1

        self.progress.setVisible(True)
        self.operation_banner.setText(
            f"Working: {title}. Gemini Voice Design can take 15–30 seconds. "
            "The controls will refresh automatically when it finishes."
        )
        self.operation_banner.setVisible(True)
        self.statusBar().showMessage(title)
        self.log(f"START {title}")
        self.tabs.setCurrentWidget(self.log_tab)
        self.thread_pool.start(worker)

    @Slot(str, str)
    def _worker_message(self, title: str, message: str) -> None:
        self.log(f"{title}: {message}")
        self.statusBar().showMessage(f"{title} — {message}")

    @Slot(str, object)
    def _worker_result(self, title: str, result: Any) -> None:
        self.log(f"RESULT {title}: {result}")
        handler = self.active_result_handler
        if handler is not None:
            handler(result)

    @Slot(str, str)
    def _worker_error(self, title: str, trace: str) -> None:
        self.active_job_failed = True
        self.log(f"FAIL  {title}\n{trace}", error=True)
        last_line = trace.strip().splitlines()[-1] if trace.strip() else "Unknown error"
        QMessageBox.critical(self, title, last_line)

    @Slot(str)
    def _worker_finished(self, title: str) -> None:
        elapsed = max(0.0, time.perf_counter() - self.active_job_started)
        failed = self.active_job_failed

        self.busy_count = 0
        self.progress.setVisible(False)
        self.operation_banner.setVisible(False)
        self.active_result_handler = None
        self.active_worker = None
        self.active_job_started = 0.0
        self.active_job_failed = False

        if failed:
            self.log(f"FAILED {title} after {elapsed:.1f}s")
            self.statusBar().showMessage(f"Failed: {title}", 8000)
        else:
            self.log(f"DONE  {title} in {elapsed:.1f}s")
            self.statusBar().showMessage(f"Completed: {title}", 8000)

        self.reload_data(self.current_speaker)

    # ---------- casting actions ----------

    def create_voice(self) -> None:
        speaker = self.current_speaker
        if not speaker:
            return
        entry = self.registry["characters"][speaker]
        if not os.environ.get("GEMINI_API_KEY"):
            QMessageBox.warning(
                self,
                "API key missing",
                "GEMINI_API_KEY is not set in this process. Start the GUI from the "
                "PowerShell session where the working key is loaded.",
            )
            return
        answer = QMessageBox.question(
            self,
            "Create character voice",
            f"Create a stored Gemini voice for\n\n"
            f"{entry.get('display_name', speaker)} ({speaker})?\n\n"
            f"This makes a real API call.",
        )
        if answer != QMessageBox.StandardButton.Yes:
            return

        def task(message: Callable[[str], None]) -> dict[str, Any]:
            worker_backend = vs.VoiceStudio(self.config, self.settings)
            registry = vs.load_registry(self.config)
            current = registry["characters"][speaker]
            request_path, request = vs.ensure_casting_request(
                self.config, speaker, current
            )
            limiter = worker_backend.limiter(
                "voices:create", int(self.settings["voice_api_rpm"])
            )
            message("Sending Voice Design request...")
            created, latency_ms = vs.api_call_with_retry(
                lambda: worker_backend.client.voices.create(**request),
                limiter=limiter,
                settings=self.settings,
                label=f"create voice {speaker}",
                idempotent=False,
            )
            voice_id = vs.save_created_voice(
                self.config,
                registry,
                speaker,
                request_path,
                request,
                created,
            )
            vs.log_usage(
                action="voice_create",
                model=request["voice"].get("model", ""),
                speaker=speaker,
                status="ok",
                latency_ms=latency_ms,
                text=request["voice"].get("prompted", {}).get("input", ""),
            )
            sample_path = vs.provider_voice_sample_path(speaker)
            message(f"Created provider voice {voice_id}")
            if sample_path.exists():
                message(f"Saved audition sample: {sample_path.relative_to(vs.ROOT)}")
            else:
                message("Provider returned no local sample; use Refresh provider sample.")
            return {
                "speaker": speaker,
                "display_name": current.get("display_name", speaker),
                "voice_id": voice_id,
                "sample_path": str(sample_path),
                "sample_exists": sample_path.exists(),
            }

        self.run_job(
            f"Create voice: {speaker}",
            task,
            self._voice_created,
        )

    def _voice_created(self, result: dict[str, Any]) -> None:
        speaker = str(result["speaker"])
        voice_id = str(result["voice_id"])
        sample_exists = bool(result.get("sample_exists"))
        display_name = str(result.get("display_name") or speaker)

        self.log(
            f"VOICE READY {display_name} ({speaker}) -> {voice_id}; "
            f"sample={'ready' if sample_exists else 'not returned'}"
        )
        self.reload_data(speaker)
        self.tabs.setCurrentWidget(self.audition_tab)

        if sample_exists:
            message = (
                f"Voice created successfully for {display_name}.\n\n"
                f"Provider voice: {voice_id}\n"
                f"Audition sample: voice/previews/{speaker}.wav\n\n"
                "The Audition & demos tab is now open. Click Play to listen."
            )
        else:
            message = (
                f"Voice created successfully for {display_name}.\n\n"
                f"Provider voice: {voice_id}\n\n"
                "No sample audio was returned with the create response. "
                "Use Refresh provider sample in Character & casting."
            )
        QMessageBox.information(self, "Voice ready", message)

    def save_prompt(self) -> None:
        speaker = self.current_speaker
        if not speaker:
            return
        new_prompt = self.prompt_edit.toPlainText().strip()
        if not new_prompt:
            QMessageBox.warning(self, "Prompt", "Voice Design prompt cannot be empty.")
            return

        def task(message: Callable[[str], None]) -> None:
            registry = vs.load_registry(self.config)
            registry["characters"][speaker]["design_prompt"] = new_prompt
            vs.save_registry(self.config, registry)
            message("Regenerating casting request...")
            vs.regenerate_casting_pack()

        self.run_job(f"Save prompt: {speaker}", task)

    def refresh_design_sample(self) -> None:
        speaker = self.current_speaker
        if not speaker:
            return

        def task(message: Callable[[str], None]) -> Path:
            worker_backend = vs.VoiceStudio(self.config, self.settings)
            registry = vs.load_registry(self.config)
            voice_id = (registry["characters"][speaker].get("voice_id") or "").strip()
            if not voice_id:
                raise RuntimeError("No provider voice ID stored.")
            limiter = worker_backend.limiter(
                "voices:get", int(self.settings["voice_api_rpm"])
            )
            message(f"Fetching {voice_id}...")
            details, _ = vs.api_call_with_retry(
                lambda: worker_backend.client.voices.get(id=voice_id),
                limiter=limiter,
                settings=self.settings,
                label=f"get voice {speaker}",
                idempotent=True,
            )
            sample_audio = vs.field_value(details, "sample_audio")
            sample_data = (
                vs.field_value(sample_audio, "data") if sample_audio else None
            )
            if not sample_data:
                raise RuntimeError("Provider returned no sample_audio.")
            path = vs.provider_voice_sample_path(speaker)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(vp.decode_audio_data(sample_data))
            return path

        self.run_job(f"Refresh sample: {speaker}", task)

    def approve_voice(self) -> None:
        speaker = self.current_speaker
        if not speaker:
            return
        entry = self.registry["characters"][speaker]
        voice_id = (entry.get("voice_id") or "").strip()
        if not voice_id:
            return
        answer = QMessageBox.question(
            self,
            "Approve voice",
            f"Approve this voice for final production?\n\n"
            f"{entry.get('display_name', speaker)}\n{voice_id}",
        )
        if answer != QMessageBox.StandardButton.Yes:
            return

        approvals = vs.read_json(
            vs.APPROVALS_PATH,
            {"schema_version": 1, "approvals": {}, "history": []},
        )
        sample = vs.provider_voice_sample_path(speaker)
        approval = {
            "speaker": speaker,
            "display_name": entry.get("display_name", speaker),
            "voice_id": voice_id,
            "approved_at": vs.utc_now(),
            "design_prompt_sha256": __import__("hashlib").sha256(
                (entry.get("design_prompt") or "").encode("utf-8")
            ).hexdigest(),
            "sample_sha256": vs.file_sha256(sample) if sample.exists() else "",
        }
        approvals.setdefault("approvals", {})[speaker] = approval
        vs.write_json_atomic(vs.APPROVALS_PATH, approvals)

        registry = vs.load_registry(self.config)
        registry["characters"][speaker]["casting_status"] = "approved"
        vs.save_registry(self.config, registry)
        self.log(f"APPROVED {speaker} -> {voice_id}")
        self.reload_data(speaker)

    def retry_voice(self) -> None:
        speaker = self.current_speaker
        if not speaker:
            return
        entry = self.registry["characters"][speaker]
        voice_id = (entry.get("voice_id") or "").strip()
        if not voice_id:
            return

        text = (
            f"Reject and delete the current provider voice?\n\n"
            f"{entry.get('display_name', speaker)}\n{voice_id}\n\n"
            f"The local audition is archived. A replacement is NOT created automatically."
        )
        if (
            QMessageBox.warning(
                self,
                "Reject / retry Voice Design",
                text,
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
                QMessageBox.StandardButton.Cancel,
            )
            != QMessageBox.StandardButton.Yes
        ):
            return

        reason = "Rejected from PySide6 Voice Studio"

        def task(message: Callable[[str], None]) -> dict[str, Any]:
            worker_backend = vs.VoiceStudio(self.config, self.settings)
            limiter = worker_backend.limiter(
                "voices:delete", int(self.settings["voice_api_rpm"])
            )
            message(f"Deleting stored provider voice {voice_id}...")
            vs.api_call_with_retry(
                lambda: worker_backend.client.voices.delete(id=voice_id),
                limiter=limiter,
                settings=self.settings,
                label=f"delete voice {speaker}",
                idempotent=True,
            )
            archive = vs.archive_local_candidate(speaker, voice_id, reason)
            self.backend.revoke_approval(speaker, reason)
            registry = vs.load_registry(self.config)
            registry["characters"][speaker]["voice_id"] = ""
            registry["characters"][speaker]["casting_status"] = "proposed"
            vs.save_registry(self.config, registry)
            return {"archive": str(archive.relative_to(vs.ROOT))}

        self.run_job(
            f"Reject voice: {speaker}",
            task,
            lambda result: QMessageBox.information(
                self,
                "Voice rejected",
                f"Candidate archived under:\n{result['archive']}\n\n"
                "You can now edit the prompt and create a replacement.",
            ),
        )

    # ---------- demos / TTS ----------

    def generate_demos(self) -> None:
        speaker = self.current_speaker
        if not speaker:
            return
        count = self.demo_count.value()

        def task(message: Callable[[str], None]) -> dict[str, int]:
            worker_backend = vs.VoiceStudio(self.config, self.settings)
            registry = vs.load_registry(self.config)
            voice_id, entry = vp.resolve_voice_id(registry["characters"], speaker)
            rows = vs.representative_rows(self.manifest, speaker, count)
            if not rows:
                raise RuntimeError("No ready dialogue lines found.")

            model = self.config["preview_model"]
            limiter = worker_backend.limiter(
                f"tts:{model}",
                int(self.settings["preview_rpm"]),
                int(self.settings["preview_tpm"]),
            )
            output_dir = vs.DIALOGUE_PREVIEW_DIR / speaker
            output_dir.mkdir(parents=True, exist_ok=True)
            sample_rate = int(self.config.get("sample_rate", 24000))
            style = (
                entry.get("default_style")
                or self.config.get("default_style")
                or ""
            ).strip()

            generated = skipped = failed = 0
            for index, row in enumerate(rows, start=1):
                path = output_dir / f"{row['id']}.wav"
                if path.exists():
                    skipped += 1
                    message(f"SKIP {row['id']} (already exists)")
                    continue

                text = row["tts_text"].strip()
                message(f"[{index}/{len(rows)}] {row['id']}  {text}")
                try:
                    interaction, latency_ms = vs.api_call_with_retry(
                        lambda text=text: vs.create_tts_interaction(
                            worker_backend.client,
                            model=model,
                            voice_id=voice_id,
                            text=text,
                            style=style,
                            sample_rate=sample_rate,
                        ),
                        limiter=limiter,
                        settings=self.settings,
                        label=row["id"],
                        idempotent=True,
                        retry_permission=True,
                        estimated_tokens=max(1, math.ceil(len(text) / 4)),
                    )
                    output_audio = vs.field_value(interaction, "output_audio")
                    audio_data = (
                        vs.field_value(output_audio, "data") if output_audio else None
                    )
                    path.write_bytes(vp.decode_audio_data(audio_data))
                    usage = vs.extract_provider_usage(interaction, text)
                    vs.log_usage(
                        action="tts_preview",
                        model=model,
                        speaker=speaker,
                        row_id=row["id"],
                        status="ok",
                        latency_ms=latency_ms,
                        text=text,
                        usage=usage,
                    )
                    generated += 1
                    message(f"OK   {row['id']} [{vs.usage_suffix(usage)}]")
                except Exception as exc:
                    failed += 1
                    vs.log_usage(
                        action="tts_preview",
                        model=model,
                        speaker=speaker,
                        row_id=row["id"],
                        status="failed",
                        text=text,
                        error=str(exc),
                    )
                    message(f"FAIL {row['id']}: {exc}")
            return {"generated": generated, "skipped": skipped, "failed": failed}

        self.run_job(
            f"Generate demos: {speaker}",
            task,
            lambda result: QMessageBox.information(
                self,
                "Demo generation",
                f"Generated: {result['generated']}\n"
                f"Skipped: {result['skipped']}\n"
                f"Failed: {result['failed']}",
            ),
        )

    def refresh_demo_table(self) -> None:
        self.demo_table.setRowCount(0)
        speaker = self.current_speaker
        if not speaker:
            return
        rows_by_id = {
            row["id"]: row
            for row in self.manifest
            if row.get("speaker") == speaker
        }
        found: list[tuple[Path, dict[str, Any] | None]] = []
        demo_dir = vs.DIALOGUE_PREVIEW_DIR / speaker
        if demo_dir.exists():
            for path in sorted(demo_dir.glob("*.wav")):
                found.append((path, rows_by_id.get(path.stem)))

        for path, row in found:
            index = self.demo_table.rowCount()
            self.demo_table.insertRow(index)
            values = [
                path.stem,
                (row or {}).get("tts_text", ""),
                str(path.relative_to(vs.ROOT)),
                f"{path.stat().st_size / 1024:.0f} KB",
                "Ready",
            ]
            for column, value in enumerate(values):
                item = QTableWidgetItem(str(value))
                if column == 0:
                    item.setData(Qt.ItemDataRole.UserRole, str(path))
                self.demo_table.setItem(index, column, item)

    def play_design_sample(self) -> None:
        if not self.current_speaker:
            return
        path = vs.provider_voice_sample_path(self.current_speaker)
        self.play_file(path)

    def _selected_demo_path(self) -> Path | None:
        row = self.demo_table.currentRow()
        if row < 0:
            return None
        item = self.demo_table.item(row, 0)
        if item is None:
            return None
        raw = item.data(Qt.ItemDataRole.UserRole)
        return Path(raw) if raw else None

    def _demo_selection_changed(self) -> None:
        path = self._selected_demo_path()
        if path is not None and path.exists():
            self._load_audio(path, autoplay=False)

    def play_selected_demo(self, *_: Any) -> None:
        path = self._selected_demo_path()
        if path is None:
            QMessageBox.information(
                self,
                "Dialogue demo",
                "Select a generated dialogue demo first.",
            )
            return
        self.play_file(path)

    def _load_audio(self, path: Path, *, autoplay: bool) -> None:
        if not path.exists():
            QMessageBox.warning(self, "Audio", f"File does not exist:\n{path}")
            return

        resolved = path.resolve()
        if self.current_audio_path != resolved:
            self.player.stop()
            self.current_audio_path = resolved
            self.player.setSource(QUrl.fromLocalFile(str(resolved)))
            try:
                display = str(resolved.relative_to(vs.ROOT))
            except ValueError:
                display = str(resolved)
            self.now_playing_label.setText(display)
            self.player_seek.setValue(0)
            self.player_time_label.setText("00:00 / 00:00")
            self.log(f"AUDIO loaded: {display}")

        self.tabs.setCurrentWidget(self.audition_tab)
        if autoplay:
            self.player.play()
            self.statusBar().showMessage(f"Playing {resolved.name}", 5000)

    def play_file(self, path: Path) -> None:
        self._load_audio(path, autoplay=True)

    def _player_play(self) -> None:
        if self.player.source().isEmpty():
            QMessageBox.information(
                self,
                "Audio player",
                "Load the Voice Design sample or select a dialogue demo first.",
            )
            return
        self.player.play()

    def _player_stop(self) -> None:
        self.player.stop()
        self.player.setPosition(0)

    @staticmethod
    def _format_media_time(milliseconds: int) -> str:
        seconds = max(0, int(milliseconds // 1000))
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        if hours:
            return f"{hours:d}:{minutes:02d}:{seconds:02d}"
        return f"{minutes:02d}:{seconds:02d}"

    @Slot(int)
    def _media_position_changed(self, position: int) -> None:
        if not self.player_seek.isSliderDown():
            self.player_seek.setValue(position)
        self.player_time_label.setText(
            f"{self._format_media_time(position)} / "
            f"{self._format_media_time(self.player.duration())}"
        )

    @Slot(int)
    def _media_duration_changed(self, duration: int) -> None:
        self.player_seek.setRange(0, max(0, duration))
        self.player_time_label.setText(
            f"{self._format_media_time(self.player.position())} / "
            f"{self._format_media_time(duration)}"
        )

    @Slot(object)
    def _media_state_changed(self, state: Any) -> None:
        playing = state == QMediaPlayer.PlaybackState.PlayingState
        self.player_play_button.setEnabled(not playing)
        self.player_pause_button.setEnabled(playing)
        if state == QMediaPlayer.PlaybackState.StoppedState:
            self.statusBar().showMessage("Audio stopped", 2000)

    def _media_error(self, error: Any, text: str) -> None:
        del error
        if text:
            self.log(f"Audio playback error: {text}", error=True)
            self.statusBar().showMessage(f"Audio error: {text}", 8000)

    # ---------- final generation ----------

    def generate_final_audio(self) -> None:
        speaker = self.current_speaker
        if not speaker:
            return
        entry = self.registry["characters"][speaker]
        if entry.get("casting_status") != "approved":
            QMessageBox.warning(
                self, "Final generation", "Approve the voice before final generation."
            )
            return

        answer = QMessageBox.question(
            self,
            "Final generation",
            f"Generate resumable final WAV output for "
            f"{entry.get('display_name', speaker)}?\n\n"
            f"Existing WAVs will be skipped.",
        )
        if answer != QMessageBox.StandardButton.Yes:
            return

        def task(message: Callable[[str], None]) -> dict[str, int]:
            worker_backend = vs.VoiceStudio(self.config, self.settings)
            registry = vs.load_registry(self.config)
            characters = registry["characters"]
            canonical = worker_backend.canonical_voice_token(characters, speaker)
            related = {
                token
                for token in characters
                if worker_backend.canonical_voice_token(characters, token) == canonical
            }
            rows = [
                row
                for row in self.manifest
                if row.get("speaker") in related
                and row.get("status") == "ready"
                and row.get("renpy_id")
            ]
            message(f"{len(rows)} ready lines across {sorted(related)}")
            generated, skipped, failed, _ = worker_backend._generate_rows(
                rows,
                mode="final",
                output_dir=vp.root_path(self.config["wav_output_dir"]),
                force=False,
            )
            return {"generated": generated, "skipped": skipped, "failed": failed}

        self.run_job(
            f"Final generation: {speaker}",
            task,
            lambda result: QMessageBox.information(
                self,
                "Final generation complete",
                f"Generated: {result['generated']}\n"
                f"Skipped: {result['skipped']}\n"
                f"Failed: {result['failed']}",
            ),
        )

    # ---------- usage ----------

    def refresh_usage(self) -> None:
        records: list[dict[str, Any]] = []
        if vs.USAGE_LEDGER_PATH.exists():
            with vs.USAGE_LEDGER_PATH.open("r", encoding="utf-8") as handle:
                for line in handle:
                    try:
                        records.append(json.loads(line))
                    except (json.JSONDecodeError, TypeError):
                        continue

        success = sum(record.get("status") == "ok" for record in records)
        exact_input = sum(
            int(record.get("total_input_tokens") or 0) for record in records
        )
        audio = sum(int(record.get("output_audio_tokens") or 0) for record in records)
        total = sum(int(record.get("total_tokens") or 0) for record in records)

        self.usage_requests["value"].setText(f"{len(records):,}")
        self.usage_success["value"].setText(f"{success:,}")
        self.usage_input["value"].setText(f"{exact_input:,}")
        self.usage_audio["value"].setText(f"{audio:,}")
        self.usage_total["value"].setText(f"{total:,}")

        self.usage_table.setRowCount(0)
        for record in reversed(records[-300:]):
            row = self.usage_table.rowCount()
            self.usage_table.insertRow(row)
            token_value = record.get("total_tokens")
            if token_value is None:
                token_value = f"~{record.get('estimated_input_tokens', 0)}"
            values = [
                record.get("timestamp", ""),
                record.get("action", ""),
                record.get("model", ""),
                record.get("speaker", ""),
                record.get("status", ""),
                token_value,
                f"{record.get('latency_ms', '')} ms"
                if record.get("latency_ms") is not None
                else "",
            ]
            for column, value in enumerate(values):
                self.usage_table.setItem(row, column, QTableWidgetItem(str(value)))

    # ---------- utilities ----------

    def open_settings(self) -> None:
        dialog = RuntimeSettingsDialog(self.settings, self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        self.settings = dialog.values()
        vs.save_runtime_settings(self.settings)
        self.backend.settings = self.settings
        self.demo_count.setValue(int(self.settings["demo_line_count"]))
        self.refresh_summary()
        self.log("Saved runtime rate/retry settings.")

    def open_next_attention(self) -> None:
        speaker = self.backend.next_attention_character()
        if speaker:
            self.select_character(speaker)
        else:
            QMessageBox.information(self, "Casting", "No characters need attention.")

    def open_voice_folder(self) -> None:
        self._open_folder(vs.ROOT / "voice")

    def open_demo_folder(self) -> None:
        if not self.current_speaker:
            return
        path = vs.DIALOGUE_PREVIEW_DIR / self.current_speaker
        path.mkdir(parents=True, exist_ok=True)
        self._open_folder(path)

    @staticmethod
    def _open_folder(path: Path) -> None:
        if os.name == "nt":
            os.startfile(str(path.resolve()))  # type: ignore[attr-defined]
        else:
            from PySide6.QtGui import QDesktopServices

            QDesktopServices.openUrl(QUrl.fromLocalFile(str(path.resolve())))

    def log(self, message: str, error: bool = False) -> None:
        prefix = "ERROR " if error else ""
        self.log_view.append(f"{prefix}{message}")
        scrollbar = self.log_view.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def closeEvent(self, event: QCloseEvent) -> None:
        self.player.stop()
        if self.busy_count:
            answer = QMessageBox.question(
                self,
                "Background work active",
                "API work is still running. Close the window anyway?",
            )
            if answer != QMessageBox.StandardButton.Yes:
                event.ignore()
                return
        event.accept()


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName(APP_TITLE)
    app.setOrganizationName("FL-SM-1-translations-dutch")
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
