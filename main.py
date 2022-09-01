from ast import Break, Pass
from cProfile import label
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QFileDialog, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
from pytube import YouTube

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "YoTo"
        self.left = 500
        self.top = 500
        self.width = 400
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Textbox title
        self.label = QLabel("Pass in YouTube URL:", self)
        self.label.setFont(QFont("Helvetica", 12))
        self.label.move(20, 20)
        self.label.resize(280, 40)

        #Textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 60)
        self.textbox.resize(280, 40)

        #Get local dir_path
        self.dir_path =""
        self.button_file = QPushButton("Select folder", self)
        self.button_file.move(20, 105)

        #Create button in the window
        self.button = QPushButton("Download file", self)
        self.button.move(20, 140)

        #Fce con. button
        self.button_file.clicked.connect(self.click_file)
        self.button.clicked.connect(self.click_download)

        self.show()
    
    def click_file (self):
        self.dir_path = QFileDialog.getExistingDirectory(self,"Choose Directory","C:\\Users\\deino\\Downloads")

    @pyqtSlot()
    def click_download (self):

        #Exceptions - no URL passed
        if self.textbox.text() == "":
            QMessageBox.question(self,"Error", "Please insert Youtube URL!", QMessageBox.Ok, QMessageBox.Ok)
            return

        if self.dir_path == "":
            QMessageBox.question(self,"Error", "Choose download directory!", QMessageBox.Ok, QMessageBox.Ok)
            return    

        textboxValue = self.textbox.text()
        yt = YouTube(textboxValue)
        yd = yt.streams.get_highest_resolution()
        yd.download(self.dir_path)
        QMessageBox.question(self,"Downloading file", "Downloaded: " + yt.title, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
        print(self.dir_path)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())