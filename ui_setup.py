from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMovie
from jarvis import Ui_mainGUI
# from assistant import startExecution
from speech_utils import take_command, engine
from assistant import MainThread 

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainGUI()
        self.ui.setupUi(self)
        self.ui.startbutton.clicked.connect(self.startTask)
        self.ui.stopbutton.clicked.connect(self.close)
        
        # Create the MainThread instance and pass 'self' (QMainWindow instance)
        self.startExecution = MainThread(self)

        # Connect the signals
        self.startExecution.query_received.connect(self.terminalPrint)

    def startTask(self):
        self.setGif("GUI\\B.G\\vecteezy_technology-background-video-4k-hd-resolution_22653051_155.gif", self.ui.bg)
        self.setGif("GUI\\B.G\\Hero_Template.gif", self.ui.graph)
        self.setGif("GUI\\B.G\\Earth.gif", self.ui.earth)
        self.startExecution.start()

    def setGif(self, movie_path, target_widget):
        movie = QMovie(movie_path)
        target_widget.setMovie(movie)
        movie.start()

    def terminalPrintAndSay(self, text):
        engine.say(text)
        print(text)
        engine.runAndWait()
        self.ui.area.appendPlainText(text)

    def terminalPrint(self, txt):
        self.ui.area.appendPlainText(txt)
