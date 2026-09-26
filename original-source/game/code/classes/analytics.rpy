init -1 python:
    import requests
    import json
    import hmac
    import base64
    import hashlib
    import calendar
    import gzip
    import uuid
    import platform
    import re
    import os
    from io import BytesIO

    class GameAnalytics:
        INIT_URL_TEMPLATE = "https://api.gameanalytics.com/v2/{}/init"
        EVENTS_URL_TEMPLATE = "https://api.gameanalytics.com/v2/{}/events"
    
        @staticmethod
        def init():
            persistent.platform, persistent.os_version = GameAnalytics.get_os_info()
        
            if collect_analytics and persistent.analytics_enabled and not renpy.get_autoreload():
                GameAnalytics.setup_persistent_data()
                GameAnalytics.setup_session_data()
            
                if GameAnalytics.get_session_end_persistent():
                    GameAnalytics.clear_event_queue()
                    GameAnalytics.delete_session_end_persistent()
            
                init_response, init_response_code = GameAnalytics.request_init()
            
                if init_response_code == 200 and init_response.get("server_ts"):
                    persistent.client_ts_offset = GameAnalytics.update_client_ts_offset(init_response["server_ts"])
                    GameAnalytics.print_verbose(f"Init response: {init_response}")
                else:
                    print_verbose("Init failed or server_ts missing.")
    
        @staticmethod
        def setup_persistent_data():
            persistent.use_gzip = True
            persistent.verbose_log = is_dev_environment
            persistent.engine_version = f"gamemaker {renpy.version_only[:5]}"
            persistent.sdk_version = "rest api v2"
            persistent.device = "unknown"
            persistent.manufacturer = "unknown"
            persistent.build_version = config.version
            persistent.steam_version = "Steam Version" if achievement.steamapi else "Not Steam Version"
            persistent.developer = "Developer Mode" if is_dev_environment else "Release Version"
            persistent.game_language = "english" if preferences.language is None else preferences.language
            persistent.client_ts_offset = 0
    
        @staticmethod
        def setup_session_data():
            if not persistent._hasattr("user_id"):
                persistent.user_id = str(uuid.uuid4())
            if not persistent._hasattr("session_num"):
                persistent.session_num = 0
            persistent.session_id = str(uuid.uuid4())
            persistent.session_num += 1
            persistent.session_start_time = datetime.datetime.utcnow()
            if not persistent._hasattr("event_queue"):
                persistent.event_queue = []
        
            persistent.game_key = "fe5c4da7ea72d93cc2e48fb923e41653"
            persistent.secret_key = "ca1fc94305f89a76fc015fd7a749d6bea4432800"
            persistent.url_init = GameAnalytics.INIT_URL_TEMPLATE.format(persistent.game_key)
            persistent.url_events = GameAnalytics.EVENTS_URL_TEMPLATE.format(persistent.game_key)
    
        @staticmethod
        def request_init():
            init_payload = {
                    "platform": persistent.platform,
                    "os_version": persistent.os_version,
                    "sdk_version": persistent.sdk_version,
                    "user_id": persistent.user_id
                    }
        
            headers = {
                    "Authorization": GameAnalytics.hmac_hash_with_secret(json.dumps(init_payload).encode("utf-8"), persistent.secret_key),
                    "Content-Type": "application/json"
                    }
        
            try:
                init_response = requests.post(persistent.url_init, json=init_payload, headers=headers, timeout = 15)
                response_dict = init_response.json() if init_response.status_code == 200 else None
            except Exception as e:
                print_verbose(f"An error occurred during init request: {e}")
                return None, None
        
            if init_response.status_code != 200:
                GameAnalytics.handle_http_error(init_response.status_code, response_dict, "Init")
        
            return response_dict, init_response.status_code
    
        @staticmethod
        def submit_events(session_end_event = False):
            if not collect_analytics or not persistent.analytics_enabled or _in_replay or not persistent.event_queue:
                return
        
            try:
                event_list_json = json.dumps(persistent.event_queue)
                GameAnalytics.print_verbose(event_list_json)
            except Exception as e:
                print_verbose(f"Failed JSON encoding: {e}")
                return
        
            if event_list_json is None:
                return
        
            if persistent.use_gzip is True:
                event_list_json = GameAnalytics.get_compressed_data(event_list_json.encode("utf-8"))
            else:
                event_list_json = event_list_json.encode("utf-8")
        
            headers = {
                    "Authorization": GameAnalytics.hmac_hash_with_secret(event_list_json, persistent.secret_key),
                    "Content-Type": "application/json"
                    }
        
            if persistent.use_gzip:
                headers["Content-Encoding"] = "gzip"
        
            try:
                events_response = requests.post(persistent.url_events, data=event_list_json, headers=headers, timeout = 15)
                response_dict = events_response.json() if events_response.status_code == 200 or is_dev_environment else None
            except Exception as e:
                print_verbose(f"An error occurred during event submission: {e}")
                return None, None
        
            GameAnalytics.handle_http_error(events_response.status_code, response_dict, "Submit events", session_end_event)
            return response_dict, events_response.status_code
    
        @staticmethod
        def session_start_event():
            GameAnalytics.init()
            if not renpy.get_autoreload():
                event_dict = {"category": "user"}
                GameAnalytics.add_to_event_queue(event_dict)
                GameAnalytics.submit_events()
    
        @staticmethod
        def design_event(event_id, value = None):
            event_id = re.sub(r"[^a-zA-Z0-9:]", "", event_id)
            event_dict = {"category": "design", "event_id": event_id}
            if isinstance(value, (int, float)):
                event_dict["value"] = value
            return event_dict
    
        @staticmethod
        def progression_event(event_id, value = None):
            event_id = re.sub(r"[^a-zA-Z0-9:]", "", event_id)
            event_dict = {"category": "progression", "event_id": event_id, "value": value}
            if isinstance(value, (int, float)):
                event_dict["value"] = value
            return event_dict
    
        @staticmethod
        def resource_event(event_id, amount = None):
            event_id = re.sub(r"[^a-zA-Z0-9:]", "", event_id)
            event_dict = {"category": "resource", "event_id": event_id, "amount": amount}
            if isinstance(amount, (int, float)):
                event_dict["amount"] = amount
            return event_dict
    
        @staticmethod
        def session_end_event():
            if collect_analytics and persistent.analytics_enabled:
                session_end_time = datetime.datetime.utcnow()
                session_length = (session_end_time - persistent.session_start_time).total_seconds()
                session_length = round(session_length)
                GameAnalytics.print_verbose(f"Session lasted {session_length} seconds")
                event_dict = {"category": "session_end", "length": session_length}
                GameAnalytics.add_to_event_queue(event_dict)
                GameAnalytics.submit_events(session_end_event = True)
    
        @staticmethod
        def get_session_end_persistent_path():
            gamedir = renpy.config.gamedir
            save_folder = "saves"
            filename = "ga_persistent"
            return os.path.join(gamedir, save_folder, filename)
    
        @staticmethod
        def write_session_end_persistent():
            file_path = GameAnalytics.get_session_end_persistent_path()
            try:
                with open(file_path, "w") as file:
                    pass
                GameAnalytics.print_verbose("Session end persistent created")
            except Exception as e:
                print_verbose(f"Failed to create session end persistent: {e}")
    
        @staticmethod
        def get_session_end_persistent():
            return os.path.exists(GameAnalytics.get_session_end_persistent_path())
    
        @staticmethod
        def delete_session_end_persistent():
            file_path = GameAnalytics.get_session_end_persistent_path()
            try:
                os.remove(file_path)
                GameAnalytics.print_verbose("Session end persistent deleted")
            except Exception as e:
                print_verbose(f"Failed to delete session end persistent: {e}")
    
        @staticmethod
        def enable_analytics():
            GameAnalytics.add_to_event_queue(GameAnalytics.design_event("preferences:analytics:enabled"))
            persistent.analytics_enabled = True
            GameAnalytics.session_start_event()
    
        @staticmethod
        def disable_analytics():
            GameAnalytics.add_to_event_queue(GameAnalytics.design_event("preferences:analytics:disabled"))
            GameAnalytics.session_end_event()
            persistent.analytics_enabled = False
    
        @staticmethod
        def update_client_ts_offset(server_ts):
            now_ts = datetime.datetime.utcnow()
            client_ts = calendar.timegm(now_ts.timetuple())
            ts_offset = client_ts - server_ts
            GameAnalytics.print_verbose(f"Client TS offset calculated to: {ts_offset}")
            return 0 if ts_offset < 10 else ts_offset
    
        @staticmethod
        def hmac_hash_with_secret(message, key):
            return base64.b64encode(hmac.new(key.encode("utf-8"), message, digestmod=hashlib.sha256).digest())
    
        @staticmethod
        def add_to_event_queue(event_dict):
            if collect_analytics and persistent.analytics_enabled and not _in_replay and not renpy.get_autoreload():
                GameAnalytics.annotate_event_with_default_values(event_dict)
                persistent.event_queue.append(event_dict)
                if len(persistent.event_queue) > 350:
                    GameAnalytics.print_verbose(f"Removed event: {persistent.event_queue[0]}")
                    persistent.event_queue.pop(0)
    
        @staticmethod
        def clear_event_queue():
            persistent.event_queue = []
            GameAnalytics.print_verbose("Cleared event queue")
    
        @staticmethod
        def annotate_event_with_default_values(event_dict):
            now_ts = datetime.datetime.utcnow()
            client_ts = calendar.timegm(now_ts.timetuple()) - persistent.client_ts_offset
        
            default_annotations = {
                    "v": 2,
                    "user_id": persistent.user_id,
                    "client_ts": client_ts,
                    "platform": persistent.platform,
                    "sdk_version": persistent.sdk_version,
                    "os_version": persistent.os_version,
                    "manufacturer": persistent.manufacturer,
                    "device": persistent.device,
                    "session_id": persistent.session_id,
                    "session_num": persistent.session_num,
                    "build": persistent.build_version,
                    "engine_version": persistent.engine_version,
                    "custom_01": persistent.steam_version,
                    "custom_02": persistent.developer,
                    "custom_03": persistent.game_language,
                    }
            event_dict.update(default_annotations)
    
        @staticmethod
        def get_compressed_data(data):
            zip_text_file = BytesIO()
            zipper = gzip.GzipFile(mode="wb", fileobj=zip_text_file)
            zipper.write(data)
            zipper.close()
            return zip_text_file.getvalue()
    
        @ staticmethod
        def get_os_info():
            if renpy.windows:
                version = platform.version().split(".")[-1]
                if int(version) >= 22000:
                    os_version = "11"
                elif int(version) >= 10000:
                    os_version = "10"
                elif int(version) >= 9000:
                    os_version = "8"
                else:
                    os_version = "7"
                platform_name = "windows"
                os_name = f"{platform_name} {os_version}"
            elif renpy.linux:
                version = platform.release().split(".")[0]
                platform_name = "linux"
                os_name = f"{platform_name} {version}"
            elif renpy.macintosh:
                version = platform.mac_ver()[0].split(".")[0]
                platform_name = "mac_osx"
                os_name = f"{platform_name} {version}"
            elif renpy.android:
                from jnius import autoclass
                Build = autoclass("android.os.Build")
                Build_VERSION = autoclass("android.os.Build$VERSION")
                version = Build_VERSION.RELEASE
                platform_name = "android"
                os_name = f"{platform_name} {version}"
            else:
                platform_name = None
                os_name = None
                persistent.analytics_enabled = False
        
            return platform_name, os_name
    
        @staticmethod
        def handle_http_error(status_code, response_dict, context, session_end_event = False):
            status_code_string = f"Returned: {status_code} response code."
            if status_code == 400:
                print_verbose(f"{status_code_string} BAD_REQUEST in {context}.")
                GameAnalytics.print_verbose("Payload found in response. Check fields for issues.")
                GameAnalytics.print_verbose(response_dict)
            elif status_code == 401:
                print_verbose(f"{status_code_string} UNAUTHORIZED in {context}. Check your Authorization code and game keys.")
            elif status_code == 413:
                print_verbose(f"{status_code_string} Request body size is bigger than the limit.")
            elif status_code != 200:
                print_verbose(f"{status_code_string} Request failed in {context}. Possibly offline.")
            else:
                GameAnalytics.print_verbose(f"{context} request successful!")
                if not session_end_event:
                    GameAnalytics.clear_event_queue()
                else:
                    GameAnalytics.write_session_end_persistent()
    
        @staticmethod
        def print_verbose(message):
            if persistent.verbose_log:
                print_verbose(message)
