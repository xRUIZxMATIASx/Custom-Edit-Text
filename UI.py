from PyQt5 import QtCore, QtWidgets, QtGui
import ctypes
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QColorDialog, QFormLayout, QLineEdit, QPushButton, QInputDialog, \
    QWidget, QHBoxLayout, QDialog

from Restore import Restore
from Settings import Settings

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

class Ui_EditText(object):

    restore = None
    originalText = ""
    settings = None
    Text = None

    def setupUi(self, EditText):
        EditText.setObjectName("EditText")
        EditText.resize(width-500, height-500)
        self.settings = Settings()
        self.centralwidget = QtWidgets.QWidget(EditText)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Text.setObjectName("Text")
        self.Text.textChanged.connect(self.changed_Text)
        self.Text.setStyleSheet("color: " + self.settings.getColorText() + ";"+"background-color: "+self.settings.getBackgroundColor()+";"+"font: "+self.settings.getSizeFont()+"pt Comic Sans MS")
        self.verticalLayout.addWidget(self.Text)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.words = QtWidgets.QLabel(self.centralwidget)
        self.words.setObjectName("words")
        self.horizontalLayout.addWidget(self.words)
        self.letters = QtWidgets.QLabel(self.centralwidget)
        self.letters.setObjectName("letters")
        self.horizontalLayout.addWidget(self.letters)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 2)
        EditText.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EditText)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 877, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTool = QtWidgets.QMenu(self.menubar)
        self.menuTool.setObjectName("menuTool")
        EditText.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EditText)
        self.statusbar.setObjectName("statusbar")
        EditText.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(EditText)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.triggered.connect(self.new_Listener)
        self.actionOpen = QtWidgets.QAction(EditText)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.file_open)
        self.actionClose = QtWidgets.QAction(EditText)
        self.actionClose.setObjectName("actionClose")
        self.actionClose.triggered.connect(self.close_Listener)
        self.actionSave = QtWidgets.QAction(EditText)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.file_save)
        self.actionTextColor = QtWidgets.QAction(EditText)
        self.actionTextColor.setObjectName("actionTextColor")
        self.actionTextColor.triggered.connect(self.textColor_Listener)
        self.actionBackgroundColor = QtWidgets.QAction(EditText)
        self.actionBackgroundColor.setObjectName("actionTextColor")
        self.actionBackgroundColor.triggered.connect(self.backgroundColor_Listener)
        self.actionSizeFont = QtWidgets.QAction(EditText)
        self.actionSizeFont.setObjectName("actionSizeFont")
        self.actionSizeFont.triggered.connect(self.actionSizeFont_Listener)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menuTool.addAction(self.actionTextColor)
        self.menuTool.addAction(self.actionBackgroundColor)
        self.menuTool.addAction(self.actionSizeFont)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())
        self.retranslateUi(EditText)
        QtCore.QMetaObject.connectSlotsByName(EditText)

        self.restore = Restore()
        file = open("temp", "r")
        lines = file.readlines()
        if len(lines) != 0:
            restore = QMessageBox()
            restore.setWindowTitle("EditText")
            restore.setText("Do you want to restore data?")
            restore.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            restore = restore.exec()
            text = ""
            if restore == QMessageBox.Yes:
                for x in lines:
                    text = text + x
                self.Text.setPlainText(text)
            elif restore == QMessageBox.Cancel:
                self.restore.delete()


    def retranslateUi(self, EditText):
        _translate = QtCore.QCoreApplication.translate
        EditText.setWindowTitle(_translate("EditText", "EditText"))
        self.words.setText(_translate("EditText", "Words: 0"))
        self.letters.setText(_translate("EditText", "Letters: 0"))
        self.label.setText(_translate("EditText", "UTF-8"))
        self.menuFile.setTitle(_translate("EditText", "File"))
        self.menuTool.setTitle(_translate("EditText", "Tools"))
        self.actionNew.setText(_translate("EditText", "New"))
        self.actionOpen.setText(_translate("EditText", "Open"))
        self.actionClose.setText(_translate("EditText", "Close"))
        self.actionSave.setText(_translate("EditText", "Save"))
        self.actionTextColor.setText(_translate("EditText", "Text Color"))
        self.actionBackgroundColor.setText(_translate("EditText", "Background Color"))
        self.actionSizeFont.setText(_translate("EditText", "Size Font"))

    def changed_Text(self):
        self.words.setText("Words: "+str(self.count_Words(self.Text.toPlainText())))
        self.letters.setText("Letters: "+str(self.count_Letters(self.Text.toPlainText())))
        self.restore.push(self.Text.toPlainText())

    def count_Words(self, text):
        words = text.split()
        return len(words)

    def count_Letters(self, text):
        characters = list(text)
        count = 0
        for x in characters:
            if not (x == "\n" or x == " "):
                count += 1
        return count

    def close_Listener(self):
        close = QMessageBox()
        close.setWindowTitle("EditText")
        close.setText("You sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Save | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            exit()
        elif close == QMessageBox.Save:
            self.file_save(True)
        elif close == QMessageBox.Cancel:
            pass

    def file_open(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        if dlg.exec_():
            filename = dlg.selectedFiles()
            text = ""
            try:
                file = open(filename[0], "r")
                for x in file.readlines():
                    text = text + x
                self.Text.setPlainText(text)
                self.Text.moveCursor(QTextCursor.End)
                self.originalText = text
                file.close()
            except:
                print("Can not open file")

    def file_save(self, wants_exit):
        dlg = QFileDialog()
        try:
            filenames = dlg.getSaveFileName()
            file = open(filenames[0], "w")
            file.write(self.Text.toPlainText())
            self.originalText = self.Text.toPlainText()
            self.restore.saved()
            file.close()
        except:
            print("Canceled")
        if wants_exit:
            exit()

    def new_Listener(self):
        if self.originalText == self.Text.toPlainText():
            self.Text.setPlainText("")
        else:
            close = QMessageBox()
            close.setWindowTitle("EditText")
            close.setText("You sure?")
            close.setStandardButtons(QMessageBox.Yes | QMessageBox.Save | QMessageBox.Cancel)
            close = close.exec()

            if close == QMessageBox.Yes:
                self.Text.setPlainText("")
            elif close == QMessageBox.Save:
                self.file_save(True)
            elif close == QMessageBox.Cancel:
                pass

    def textColor_Listener(self):
        color = QColorDialog.getColor()
        self.Text.setStyleSheet("color: "+color.name()+";"+"background-color: " + self.settings.getColorText() + ";"+"font: "+self.settings.getSizeFont()+"pt Comic Sans MS")
        self.settings.setColorText(color.name())

    def backgroundColor_Listener(self):
        color = QColorDialog.getColor()
        self.Text.setStyleSheet("color: " + self.settings.getColorText() + ";"+"background-color: " + color.name() + ";"+"font: "+self.settings.getSizeFont()+"pt Comic Sans MS")
        self.settings.setBackground(color.name())

    def actionSizeFont_Listener(self):
        self.dialog = QWidget()
        self.getSize()

    def getSize(self):
        i, okPressed = QInputDialog.getInt(self.dialog, "Get integer", "Percentage:", int(self.settings.getSizeFont()), 5, 100, 1)
        if okPressed:
            try:
                self.Text.setStyleSheet("color: " + self.settings.getColorText() + ";" + "background-color: " + self.settings.getBackgroundColor() + ";" + "font: " + str(i) + "pt Comic Sans MS")
                self.settings.setSizeFont(str(i))
            except Exception as e:
                print(e)


