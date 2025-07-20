from speech_utils import take_command
from sleep_mode import listen_for_wake_word
from gemini_command import generate_text
import capabilities
from extract_list import extract_list
import subprocess
import time
import webbrowser
import keyboard
import pyscreeze
import os
# from image_generator import image_generator

in_command_mode = True
ui = None

def command_mode(ui_ele,mode):
    global in_command_mode
    global ui
    ui = ui_ele
    retry = 0
    in_command_mode = True
   
    ui.terminalPrintAndSay("Jarvis  is in command mode!")
    while in_command_mode:
        print("in")
        query = take_command(ui).lower()
        print(query)
        if query == "none":
            retry += 1
            if(retry  > 4):
                ui.terminalPrintAndSay("Jarvis entering sleep mode")
                listen_for_wake_word()
                ui.terminalPrintAndSay('Jarvis is awake')
                retry=0
            else:
                ui.terminalPrintAndSay("Please say again!")
        else:
            retry = 0
            response = generate_text(query)
            if(response[0:4]=="func"):
                extracted_list = extract_list(response)
                i = 0
                print(extracted_list)
                while i < len(extracted_list):
                    if extracted_list[i] in capabilities.command_mode_capabilities['with_args']:
                        print(extracted_list[i])
                        print(extracted_list[i+1])
                        
                        function = globals().get(extracted_list[i])
                        function(extracted_list[i+1])
                        i +=2
                    elif extracted_list[i] in capabilities.command_mode_capabilities['without_args']:
                        function = globals().get(extracted_list[i])
                        function()
                        i+=1
                    else:
                        ui.terminalPrintAndSay("This function is not available in command mode.")
                        break
            else:
                ui.terminalPrintAndSay(response)
                
    return None

def close_app(app_name):
    try:
        result = subprocess.run(
            ['taskkill', '/f', '/im', f'{app_name}.exe'],
            capture_output=True,  
            text=True,            
            check=True            
        )
        ui.terminalPrint(result.stdout)
    except subprocess.CalledProcessError as e:
        error_message = e.stderr.strip()  
        ui.terminalPrint(error_message)

    time.sleep(1)

def open_app(app_name, wait_time=5):
    try:
        # Simulate pressing the Windows key to open the Start menu
        keyboard.send('windows')
        time.sleep(1)  # Wait for the Start menu to open

        # Type the application name
        keyboard.write(app_name)
        time.sleep(1)  # Wait for the application name to be entered

        # Press Enter to open the application
        keyboard.send('enter')

        # Wait for a specified amount of time to let the app open
        ui.terminalPrint(f"Waiting forp {wait_time} seconds for {app_name} to open.")
        time.sleep(wait_time)  # This wait time can be adjusted

    except Exception as e:
        ui.terminlPrint("Error while opening the application:", str(e))
        
def open_youtube():
    ui.terminalPrintAndSay('Ok Sir, Opening YouTube for you!')
    webbrowser.open('https://www.youtube.com')
    ui.terminalPrintAndSay('Done Sir!')
    
def search_on_youtube(search):
    web = 'https://www.youtube.com/results?search_query=' + search
    webbrowser.open(web)
    ui.terminalPrintAndSay('Done Sir!')
    
def pause_video():
    keyboard.press('k')
        
def restart_video():
    keyboard.press('0')
    
def mute_video():
    keyboard.press('m')
    
def skip_video():
    keyboard.press('1')
    
def back_video():
    keyboard.press('j')
    
def fullscreen_video():
    keyboard.press('f')
    
def film_mode():
    keyboard.press('t')

def close_tab():
    keyboard.press('ctrl + w')
    
def close_youtube():
    keyboard.press('ctrl + w') 
    
def open_new_tab():
    keyboard.press_and_release('ctrl + t')

def open_new_window():
    keyboard.press_and_release('ctrl + n')
    
def open_history():
    keyboard.press_and_release('ctrl + h')
    
def open_download():
    keyboard.press_and_release('ctrl + j')
    
def open_recently_closed_tab():
        keyboard.press_and_release('ctrl + shift + t')
        
def search_on_internet(search_string):
    search_url = f"https://www.google.com/search?q={search_string}"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(search_url)
    print(f"Searching for: {search_string}")
    
def open_browser():
    ui.terminalPrintAndSay('Sir, what should I search on google')
    oy = take_command(ui).lower()
    webbrowser.open(f"{oy}")

def take_screenshot():
    screenshot = pyscreeze.screenshot()
    screenshot.save('screenshot.png')

def shutdown_sys():
    ui.terminalPrintAndSay('shutting down')
    os.system("shutdown /s /t 5")
    
def restart_sys():
    ui.terminalPrintAndSay('restarting')
    os.system("restart /s /t 5")
    
def exit():
    global in_command_mode
    ui.terminalPrintAndSay("Exiting command mode")
    in_command_mode = False
    
# def generate_image(prompt):
#     ui.terminalPrintAndSay("Generating image please wait.")
#     image_generator(prompt)
#     ui.terminalPrintAndSay("Image generated.")