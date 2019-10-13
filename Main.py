from UI import Ui_EditText
from PyQt5 import QtWidgets

class Main:

    ui = None

    def __init__(self):
        if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            app.aboutToQuit.connect(self.try_Quit)
            EditText = QtWidgets.QMainWindow()
            self.ui = Ui_EditText()
            self.ui.setupUi(EditText)
            EditText.show()
            sys.exit(app.exec_())

    def try_Quit(self):
        print("Bye")

Main()
