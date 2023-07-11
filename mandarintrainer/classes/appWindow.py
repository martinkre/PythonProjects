from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QPushButton, QHBoxLayout, QLabel, QLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from ui.MainWindow2 import Ui_MainWindow
from classes.elements.MultiButton import MultiButton

import sys, csv, codecs


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the user interface from Qt Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Mandarin Trainer App")
        self.containter = []

        

        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.exit_application)
        
        self.ui.actionExit.triggered.connect(self.exit_application)
        

        self.ui.actionSide_Menu.triggered.connect(self.toggle_side_menu)
        
        

        #self.load_data()
        self.build_text()

    def populate_containter(self,i):
        #for i in self.ui.SideMenu.findChildren(MultiButton):
            #self.containter.clear()
        self.containter.append(i)

                
    def hide_tiny_buttons(self):
        for mb in self.containter:
            mb.hide_edit_buttons()

    def show_tiny_buttons(self):
        for mb in self.containter:
            mb.show_edit_buttons()

    def delete_button(self, id):
        pass


    def toggle_side_menu(self):
        sm = self.ui.SideMenu
        button = self.ui.actionSide_Menu
        if button.isChecked():
            sm.show()
        else:
            sm.hide()
        

    def call_loader():
        app = QApplication(sys.argv)
        window = MyApp()
        window.show()
        sys.exit(app.exec_())         
            

    def build_text(self):
        self.ui.pushButton.setText("Exit")
        self.ui.pushButton_2.setText("Top 100")
        self.ui.pushButton_3.setText("Numbers")
        self.ui.pushButton_5.setText("Weekdays")
        self.ui.pushButton_4.setText("Edit Mode")
        self.ui.pushButton_confirm.setText("OK")
        self.ui.pushButton_cancel.setText("Cancel")

        self.button_add = QPushButton(self.ui.SideMenu)
        self.ui.verticalLayout.insertWidget(3, self.button_add)
        self.button_add.setText("+")
        self.button_add.hide()
        self.ui.le_editor.hide()

        

        # self.bb = MultiButton(Text="X", parent=self.ui.SideMenu)
        # self.ui.verticalLayout.insertWidget(3, self.bb)

        fp_top100 = "./data/mandb.csv"
        fp_numbers = "./data/numdb.csv"
        fp_weekdays = "./data/weekdays.csv"
        
        self.ui.pushButton.pressed.connect(self.exit_application)
        self.ui.pushButton_2.pressed.connect(lambda: self.load_data(fp_top100,2))

        self.ui.pushButton_3.pressed.connect(lambda: self.load_data(fp_numbers,3))
        self.ui.pushButton_5.pressed.connect(lambda: self.load_data(fp_weekdays,5))
        self.button_add.pressed.connect(lambda: self.add_items("Unnamed"))
        
        self.ui.pushButton_4.pressed.connect(self.checker_button)


    def checker_button(self):
        
        if self.ui.pushButton_4.isChecked():
            #self.ui.pushButton_4.setChecked = 0
            self.ui.pushButton_4.setText("Edit Mode")
            self.button_add.hide()

            self.ui.le_editor.hide()
            self.hide_tiny_buttons()
            
            

        else:
            #self.ui.pushButton_4.setChecked = 1
            self.ui.pushButton_4.setText("Edit activated")
            self.button_add.show()
            self.ui.le_editor.show()
            #self.populate_containter()
            self.show_tiny_buttons()


    def active_button(self):
        self.ui.pushButton_2.setCheckable(True)
        self.ui.pushButton_2.setChecked(True)
        self.ui.pushButton_2.setStyleSheet(".QPushButton:checked {\n"
                                            "    color: #054269;"
                                            "	background-color: #1973ab;"
                                            "}\n")

    def add_items(self, name):
        new_button = MultiButton(name, self.ui.SideMenu)
        
        self.populate_containter(new_button)
        self.show_tiny_buttons()
        new_button.new_button2.pressed.connect(lambda: new_button.hide())
        self.ui.verticalLayout.insertWidget(3, new_button)
        

    def load_data(self, filepath, button_number):
        # Path to your CSV file
        csv_file = filepath #'./data/mandb.csv'

        # Read CSV data
        with codecs.open(csv_file, "r", encoding="utf-8-sig") as file:
            csv_data = list(csv.reader(file))
        
        model = QStandardItemModel()
        self.ui.thatTable.setModel(model)
        self.ui.thatTable.horizontalHeader().setStretchLastSection(True)

        with open(csv_file, "r") as fileInput:
            for i, row in enumerate(csv_data):
                if i == 0:
                    model.setHorizontalHeaderLabels([r.strip().strip('"') for r in row])
                else:
                    items = [
                        QStandardItem(field.strip())
                        for field in row
                    ]
                    model.appendRow(items)


        self.ui.thatTable.show()
        
        

    def exit_application(self):
        QApplication.quit()