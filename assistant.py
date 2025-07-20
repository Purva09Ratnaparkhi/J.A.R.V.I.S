from PyQt5.QtCore import QThread, pyqtSignal
from speech_utils import take_command
import datetime
from chat_mode import chat_mode
from sleep_mode import listen_for_wake_word
from command_mode  import command_mode
from code_mode import code_mode


ui = None
class MainThread(QThread):
    query_received = pyqtSignal(str)

    def __init__(self, uie):
        global ui
        super(MainThread, self).__init__()
        ui = uie # Store the reference to the UI

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        main()
        

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        ui.terminalPrintAndSay("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        ui.terminalPrintAndSay("Good Afternoon Sir")

    else:
        ui.terminalPrintAndSay("Good Evening!")

    ui.terminalPrintAndSay("I am Jarvis Sir....")
    

# Main execution
def main():
    mode = None
    wishMe()
    retry = 0
    exit = False
    while not exit:
        if(mode == None):
            if(retry <1):
                ui.terminalPrintAndSay("Please select the mode from below:\n1 Chat mode\n2 Code mode\n3 Command mode")
            else:
                ui.terminalPrintAndSay("You need to select mode to continue.")
        query = take_command(ui).lower()
        print(query)
        if 'chat mode' in query or 'chat' in query:
            retry = 0
            mode = 'chat_mode'
            mode = chat_mode(mode=mode,ui_ele=ui)
            
        elif 'command mode' in query or "command" in  query:
            retry = 0
            mode = 'command_mode'
            mode = command_mode(ui,mode)
        elif 'code mode' in query or 'code' in query:
            retry = 0
            mode =  'code_mode'
            mode = code_mode(ui,mode)
        elif 'exit' in query or 'bye' in query or 'stop'  in query:
            retry = 0
            quit_jarvis()
        else:
            retry += 1
            if(retry  > 4):
                ui.terminalPrintAndSay("Jarvis entering sleep mode")
                listen_for_wake_word()
                ui.terminalPrintAndSay('Jarvis is awake')
                retry=0
            else:
                ui.terminalPrintAndSay("Please say again!")

        
def quit_jarvis():
    ui.terminalPrintAndSay("Jarvis is Exiting")
    from PyQt5.QtWidgets import QApplication
    QApplication.quit()