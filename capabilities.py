chat_mode_capabilities = ["get_ip_address","get_time","set_reminder","get_temp","exit","get_date"]
command_mode_capabilities = {
    'with_args':["open_app","close_app","search_on_youtube","search_on_internet"],
    'without_args':['open_youtube',"pause_video","restart_video","mute_video","skip_video","back_video",
                    "fullscreen_video","film_mode","close_tab","close_youtube","search_on_internet",
                    "open_browser","open_recently_closed_tab","open_download","open_history",
                    "open_new_window","open_new_tab","take_screenshot","shutdown_sys","restart_sys","exit"]
    }
code_mode_capabilities = {
    "with_args": ["generate_code"],
    "without_args":["new_file","new_project","save_file","exit","close_file","run_code"]
}