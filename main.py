from PyQt5.QtWidgets import QApplication
from ui_setup import Main
# from assistant import startExecution
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Main()  # Create the Main window instance
    main_window.show()
    sys.exit(app.exec_())
