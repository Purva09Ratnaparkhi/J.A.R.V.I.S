from speech_utils import take_command
from sleep_mode import listen_for_wake_word
from gemini_chat import generate_text
import capabilities
from requests import get
import datetime
from extract_list import extract_list

in_chat_mode = True
ui = None

def chat_mode(ui_ele,mode):
    global in_chat_mode
    in_chat_mode = True
    global ui
    ui = ui_ele
    retry = 0
    
    ui.terminalPrintAndSay("Jarvis  is in chat mode!")
    while in_chat_mode:
        
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
                for func in extracted_list:
                    if func in capabilities.chat_mode_capabilities:
                        function = globals().get(func)
                        function()
                    else:
                        ui.terminalPrintAndSay("This function is not available in chat mode.")
            else:
                ui.terminalPrintAndSay(response)
                
    return None

            
def get_ip_address():
    ip = get('https://api.ipify.org').text
    ui.terminalPrintAndSay(f'Your IP adress is {ip}')
    
def get_time():
    # To get the current time
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    ui.terminalPrintAndSay(f"Sir,The Time is {strTime}")
    
def set_reminder():
    ui.terminalPrintAndSay(f"This feature will be available soon, sorry for your inconvenience.")
    
def get_date():
    # Get the current date and time
    now = datetime.datetime.now()

    # Extract the date part
    today = now.date()

    # Format the date as a string
    formatted_date = today.strftime("%Y-%m-%d")
    ui.terminalPrintAndSay(f"Today's date is {formatted_date}")

def get_temp():
    # To get the current temperature
    ui.terminalPrintAndSay(f"This feature will be available soon, sorry for your inconvenience.")
    
def exit():
    global in_chat_mode
    ui.terminalPrintAndSay("Exiting chat mode")
    in_chat_mode = False
    
