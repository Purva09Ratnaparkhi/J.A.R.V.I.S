from speech_utils import take_command
from sleep_mode import listen_for_wake_word
from gemini_code import generate_text
import capabilities
from requests import get
import pyperclip
import time
from extract_list import extract_list
import keyboard
import code_generator

in_code_mode = True
ui = None

def code_mode(ui_ele,mode):
    global in_code_mode
    in_code_mode = True
    global ui
    ui = ui_ele
    retry = 0
    open_app("vscode")
    ui.terminalPrintAndSay("Jarvis is in Code mode!")
    while in_code_mode:
        
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
                    if extracted_list[i] in capabilities.code_mode_capabilities['with_args']:
                        print(extracted_list[i])
                        print(extracted_list[i+1])
                        
                        function = globals().get(extracted_list[i])
                        function(extracted_list[i+1])
                        i +=2
                    elif extracted_list[i] in capabilities.code_mode_capabilities['without_args']:
                        function = globals().get(extracted_list[i])
                        function()
                        i+=1
                    else:
                        ui.terminalPrintAndSay("This function is not available in code mode.")
                        break
            else:
                ui.terminalPrintAndSay(response)
                
    return None
                

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
        ui.terminalPrint(f"Waiting for {wait_time} seconds for {app_name} to open.")
        time.sleep(wait_time)  # This wait time can be adjusted

    except Exception as e:
        ui.terminlPrint("Error while opening the application:", str(e))
        
def new_file():
    keyboard.press_and_release('ctrl + n')
    keyboard.press_and_release('ctrl + s')
    ui.terminalPrintAndSay(f"Please can you tell me the file name with extension.")
    query = "none"
    retry = 0
    while query == "none":
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
    query = query.replace("dot",".")
    query = query.replace(" ","")
    for i in query:
        keyboard.press_and_release(i)
    keyboard.press_and_release("enter")


def new_project():
    keyboard.press_and_release('ctrl+shift+n')

def generate_code(prompt):
    code = code_generator.generate_code(prompt)
    pyperclip.copy(code)
    keyboard.press_and_release('ctrl+v')
    
def save_file():
    keyboard.press_and_release('ctrl+s')
    
def close_file():
    keyboard.press_and_release('ctrl+w')
    
def exit():
    global in_code_mode
    keyboard.press_and_release('ctrl+s')
    time.sleep(0.5)
    ui.terminalPrintAndSay("Exiting code mode")
    in_code_mode = False
    
def run_code():
    keyboard.press_and_release('ctrl+F5')