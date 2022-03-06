# -*- coding: cp1251 -*-
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidget, QListWidgetItem, QMessageBox, QWidget
from PyQt5.QtCore import Qt, QMimeData, QStringListModel, QModelIndex, pyqtSignal
from pathlib import Path
import pyautogui
from time import sleep
from keyboard import write



class prog(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def redraw(self):
        slm = QStringListModel()
        slm.setStringList(open(self.FILE_PATH).read().splitlines())
        self.listview.setModel(slm)
        print("redraw")

    def initUI(self):
        self.FILE_PATH = Path('Data.txt')
        layout = QVBoxLayout()
        text_input_button = QPushButton('Добавить')
        file_input_button = QPushButton("Файл")

        self.listview = QListView()
        self.listview.clicked.connect(self.clicked)
        text_input_button.clicked.connect(self.showDialog)
        file_input_button.clicked.connect(self.file_input)

        layout.addWidget(file_input_button)
        layout.addWidget(self.listview)
        layout.addWidget(text_input_button)
        self.setLayout(layout)
        self.setWindowTitle("MainWindow")
        self.setGeometry(600, 600, 560, 300)

        self.redraw()

    def clicked(self, ind):
        posX, posY = pyautogui.position()
        pyautogui.click(1800, 550)
        sleep(0.5)
        write(ind.data())
        pyautogui.moveTo(posX, posY)

    def file_input(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "")

        self.FILE_PATH = str(fname[0])
        self.redraw()
    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your text:')

        if ok:
            print(text)
            with open(self.FILE_PATH, "a+") as file:
                lastLines = len(file.readlines())
                file.seek(lastLines, 0)
                file.write(text + "\n")
            self.redraw()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Alt:
            self.redraw()
        elif e.key() == Qt.Key_F1:
            print(5)
            msg = QMessageBox()
            msg.setWindowTitle("Documentation")
            msg.setText("Инструкция")
            msg.setStandardButtons(QMessageBox.Cancel)
            msg.setDetailedText('''1. Программа располагается на левой части экрана, а на правой Word.\n
2.Для печати 1 раз кликаешь на блок текста\n
3.При выборе файла использовать исключительно .txt формат''')
            msg.exec_()



# self.qList[qModelIndex.row()] имя блока листа TODO
