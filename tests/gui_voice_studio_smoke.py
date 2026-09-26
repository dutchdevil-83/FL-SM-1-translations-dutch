#!/usr/bin/env python3
"""Headless smoke test for the PySide6 waveform frontend."""

from __future__ import annotations

import math
import os
import sys
import tempfile
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import numpy as np
import soundfile as sf
from PySide6.QtWidgets import QApplication

import voice_studio_gui as gui


def main() -> int:
    app = QApplication.instance() or QApplication([])

    with tempfile.TemporaryDirectory() as temp_dir:
        wav_path = Path(temp_dir) / "smoke.wav"
        sample_rate = 24000
        duration = 1.25
        sample_count = int(sample_rate * duration)
        t = np.arange(sample_count, dtype=np.float32) / sample_rate
        samples = (0.35 * np.sin(2.0 * math.pi * 440.0 * t)).astype(np.float32)
        sf.write(str(wav_path), samples, sample_rate, subtype="PCM_16")

        widget = gui.WaveformWidget(interactive=True)
        widget.resize(900, 220)
        widget.load_file(wav_path)
        app.processEvents()

        assert widget.file_path == wav_path.resolve()
        assert abs(widget.duration_seconds - duration) < 0.02
        assert len(widget.upper_curve.getData()[0]) > 10
        assert len(widget.lower_curve.getData()[0]) > 10

        widget.set_playhead(0.5)
        assert abs(float(widget.playhead.value()) - 0.5) < 0.01

        widget.zoom(0.5)
        visible = widget.getViewBox().viewRange()[0]
        assert 0.0 <= visible[0] < visible[1] <= duration + 0.05

        widget.reset_zoom()
        app.processEvents()
        widget.close()

    print("PySide6 waveform GUI smoke test passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
