from PyQt5 import uic
import re
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QAction, QMainWindow
from PyQt5.QtGui import QColor
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor, QClipboard

position = 0

Form, Window = uic.loadUiType("gui.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


import re

def remove_tags_and_comments():
    text = form.textEdit.toPlainText()
    text = re.sub(r'<summary>.*?</summary>', '', text, flags=re.DOTALL)
    text = re.sub(r'#.*', '', text)
    text = re.sub(r'(?s)<!--.*?-->', '', text)
    text = re.sub(r'/\*[\s\S]*?\*/', '', text)
    text = re.sub(r'""".*?"""', '', text, flags=re.DOTALL)
    text = re.sub(r"'''.*?'''", '', text, flags=re.DOTALL)
    text = re.sub(r'//.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'/\*[\s\S]*', '', text)
    text = re.sub(r'<.*', '', text, flags=re.DOTALL)
    text = "\n".join([line for line in text.split("\n") if line.strip() != ""])
    form.textEdit.setPlainText(text)
    clear_formatting()


def cleare_field():
    form.textEdit.clear()


def clear_formatting():
    plain_text = form.textEdit.toPlainText()
    plain_text = re.sub('<.*?>', '', plain_text)
    form.textEdit.setPlainText(plain_text)
    char_format = QTextCharFormat()
    char_format.setForeground(QColor("black"))

    text_cursor = form.textEdit.textCursor()
    text_cursor.setPosition(0)
    text_cursor.setPosition(len(plain_text), QTextCursor.KeepAnchor)
    text_format = QTextCharFormat()
    text_format.setForeground(QColor(Qt.black))
    text_cursor.setCharFormat(text_format)
    form.textEdit.setTextCursor(text_cursor)

def copy_text():
    clipboard = QApplication.clipboard()
    plain_text = form.textEdit.toPlainText()
    clipboard.setText(plain_text, QClipboard.Clipboard)

def past_text():
    clipboard = QApplication.clipboard()
    form.textEdit.setPlainText(clipboard.text())

form.pushButton.clicked.connect(remove_tags_and_comments)
form.pushButton_2.clicked.connect(copy_text)
form.pushButton_3.clicked.connect(past_text)
form.pushButton_4.clicked.connect(cleare_field)
form.pushButton_5.clicked.connect(clear_formatting)


app.exec_()
