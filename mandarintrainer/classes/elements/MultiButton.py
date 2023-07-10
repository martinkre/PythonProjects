from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QPushButton, QHBoxLayout, QLabel, QLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from ui.MainWindow2 import Ui_MainWindow

import sys, csv, codecs


class MultiButton(QPushButton, QHBoxLayout):
    def __init__(self, Text, parent = None):
        super(MultiButton, self).__init__()
        self.setupbt(Text)


    def hide_edit_buttons(self):
        b1 = self.new_button
        b2 = self.new_button2
     

        b1.hide()
        b2.hide()
        

    def show_edit_buttons(self):
        b1 = self.new_button
        b2 = self.new_button2
        

        b1.show()
        b2.show()
        


    def setupbt(self, Text):
        self.vertLayout = QHBoxLayout(self)
        self.vertLayout.setObjectName("vertLayout")
        self.vertLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.setStyleSheet ("\n"

    "MultiButton {\n"
"    background-color: #0d2d53;\n"
"    color: #f0f1f2;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f1f2;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"    \n"
"}\n"
"\n"
"MultiButton:hover {\n"
"    color: #054269;\n"
"    background-color: #1973ab;\n"
"\n"
"}\n"
"\n"
"MultiButton:pressed {\n"
"    background-color: #054269;\n"
"    color: #adbacc;\n"
"\n"
"}\n"
"\n"
                      
    
    "        .QPushButton {\n"
    "           min-width: 1em;\n"
    "           max-width: 10em; "
    "           padding: 1px;"
    "           font-size: 10px;"
    "           border-radius: 5px"
    "}"
        )
        self.vertLayout.setAlignment(Qt.AlignRight)
        self.setText(Text)
        
        
        self.vertLayout.setContentsMargins(1, 1, 5, 1)
        self.vertLayout.setSpacing(6)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.vertLayout.addItem(spacerItem)

        self.new_button = QPushButton(self)
        self.new_button.setText("E")
        self.vertLayout.addWidget(self.new_button)
        self.new_button2 = QPushButton(self)
        self.new_button2.setText("X")
        self.vertLayout.addWidget(self.new_button2)
        
        self.hide_edit_buttons()
        self.show()

    def delete(self):
        
        self.destroy()

