from PyQt5.QtWidgets import QWidget,QApplication, QMainWindow, QStackedLayout, QPushButton,QGridLayout, QHBoxLayout, QLabel, QLayout, QSpacerItem, QSizePolicy, QLineEdit
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QRect

class MainButton(QPushButton):
    def __init__(self, name, parent):
        super().__init__(parent=parent)
        self.setText(name)

class MyLineEdit(QLineEdit):
    def __init__(self, name, parent):
        super().__init__(parent=parent)
        self.setText(name)
        self.setAlignment(Qt.AlignCenter)

class EditWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        
        
        self.layout = QHBoxLayout(self)
        self.layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        # self.spacerItem = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # self.layout.addItem(self.spacerItem)
        
        # self.layout.setSpacing(6)
        # self.le_text = QLineEdit()
        # self.le_text.setAlignment(Qt.AlignCenter)
        # self.buttonconfirm = QPushButton(self)
        # self.buttonconfirm.setText("Y")
        #self.buttonconfirm.pressed.connect(lambda: self.change_itemname())

        # self.layout.addWidget(self.le_text)
        # self.layout.addWidget(self.buttonconfirm)

        self.spacerItem = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout.addItem(self.spacerItem)

        self.new_button = QPushButton(self)
        self.new_button.setText("Save")
        self.layout.addWidget(self.new_button)
        self.new_button2 = QPushButton(self)
        self.new_button2.setText("X")
        self.layout.addWidget(self.new_button2)
        self.hide_lineedit()

        self.spacerItem = QSpacerItem(5, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout.addItem(self.spacerItem)


    def hide_lineedit(self):
        #self.le_text.hide()
        #self.buttonconfirm.hide()
        pass
    
    def show_lineedit(self):
        #self.le_text.show()
        #self.buttonconfirm.show()
        pass

    def hide_edit_buttons(self):
        self.new_button.hide()
        self.new_button2.hide()
        self.hide_lineedit()

    def show_edit_buttons(self):
        self.new_button.show()
        self.new_button2.show()

    

class MultiButton(QWidget):
    def __init__(self, Text, parent = None):
        super().__init__(parent=parent)
        self.main_button_name = Text
        #self.parent = parent
        
        
        self.main_button = MainButton(Text, self)
        self.edit_widget = EditWidget(self)
        self.line_edit = MyLineEdit(Text, self)
        
        #self.edit_widget.show()
        self.edit_widget.new_button2.pressed.connect(lambda: self.hide())
        #self.edit_widget.buttonconfirm.pressed.connect(lambda: self.change_itemname())
        self.line_edit.returnPressed.connect(lambda: self.change_itemname())
        self.edit_widget.new_button.pressed.connect(lambda: self.change_itemname())


        #self.edit_widget.le_text.returnPressed.connect(lambda: self.change_itemname())             
        #self.edit_widget.le_text.setText(self.main_button.text())

        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.main_button, 1,1)
        self.layout.addWidget(self.line_edit, 1,1)
        self.layout.addWidget(self.edit_widget, 1,1, Qt.AlignRight)
        self.line_edit.hide()
        #self.myoverlay = QHBoxLayout(self)
        #self.myoverlay.addWidget(self.edit_widget)
        self.edit_widget.raise_()
        #self.setup_main_button(self.main_button_name)
        #self.setup_edit_buttons()
        self.mystyle = '../elements/css/mystyle.css'
        self.load_style()


    def switch_button_with_lineedit(self, a1):
        if a1 == True:
            self.line_edit.show()
            self.main_button.hide()
        elif a1 == False:
            self.line_edit.hide()
            self.main_button.show()

    def load_style(self):
        with open("C:/Users/mk2/python/Project1/mandarintrainer/classes/elements/css/mystyle.css","r") as fh:
            self.setStyleSheet(fh.read())
            #print(fh)

    def setup_main_button(self, name):
        self.main_button_widget = QWidget(self)
        self.background = QHBoxLayout()
        self.main_button = QPushButton(name)
        self.main_button.setAccessibleName("main_button")
        self.background.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.background.setContentsMargins(0,0,0,0)
        self.background.setAlignment(Qt.AlignCenter)
        self.background.addWidget(self.main_button)
        self.main_button_widget.setLayout(self.background)
        self.main_button.pressed.connect(lambda: print("alafösldkjf"))
        
       
    

    def toggle_main_button(self, a1):
        if a1 == True:
            self.main_button.setEnabled(True)
        elif a1 == False:
            self.main_button.setDisabled(True)
            


    def hide_edit_buttons(self):
        #self.edit_widget.hide()
        #b2 = self.new_button2
        
        #b1.hide()
        #b2.hide()
        #self.hide_lineedit()
        pass

    def show_edit_buttons(self):
        #self.edit_widget.show()
        

        #b1 = self.new_button
        #b2 = self.new_button2

        #b1.show()
        #b2.show()
        pass
        
        

    def hide_lineedit(self):
        le1 = self.le_text
        b1 = self.buttonconfirm
        b1.hide()
        le1.hide()

    def show_lineedit(self):
        le1 = self.le_text
        b1 = self.buttonconfirm
        le1.show()
        b1.show()


    def change_itemname(self):
        
        new_name = self.line_edit.text()
        self.main_button.setText(new_name)
        #self.switch_button_with_lineedit(False)


    def setup_edit_buttons(self):
        
        self.edit_widget = QWidget(self)
        
        self.vertLayout = QHBoxLayout()
        self.vertLayout.setObjectName("vertLayout")
        self.vertLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.vertLayout.setAlignment(Qt.AlignRight)
        self.spacerItem = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.vertLayout.addItem(self.spacerItem)
        self.vertLayout.setContentsMargins(1, 1, 5, 1)
        self.vertLayout.setSpacing(6)
        self.le_text = QLineEdit("Text")
        self.le_text.setAlignment(Qt.AlignCenter)
        self.le_text.returnPressed.connect(lambda: self.change_itemname())             
        self.buttonconfirm = QPushButton(self)
        self.buttonconfirm.setText("Y")
        self.buttonconfirm.pressed.connect(lambda: self.change_itemname())
        self.vertLayout.addWidget(self.le_text)
        self.vertLayout.addWidget(self.buttonconfirm)
        self.spacerItem = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.vertLayout.addItem(self.spacerItem)

        self.new_button = QPushButton(self)
        self.new_button.setText("Edit")
        self.new_button.pressed.connect(lambda: self.show_lineedit())
        self.vertLayout.addWidget(self.new_button)
        self.new_button2 = QPushButton(self)
        self.new_button2.setText("X")
        self.new_button2.pressed.connect(lambda: self.hide())
        self.vertLayout.addWidget(self.new_button2)
        
        
        self.hide_edit_buttons()
        self.edit_widget.setLayout(self.vertLayout)
        self.edit_widget.raise_
        

    def delete(self):
        
        self.destroy()


