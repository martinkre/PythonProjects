from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QPushButton
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from ui.MainWindow2 import Ui_MainWindow

import sys, csv, codecs

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the user interface from Qt Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Mandarin Trainer App")
        
        

        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.exit_application)
        
        self.ui.actionExit.triggered.connect(self.exit_application)
        

        self.ui.actionSide_Menu.triggered.connect(self.toggle_side_menu)
        
        

        #self.load_data()
        self.build_text()
    
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

    def checker_button(self):
        
        
        if self.ui.pushButton_4.isChecked():
            #self.ui.pushButton_4.setChecked = 0
            self.ui.pushButton_4.setText("Edit deactivated")
            self.button_add.hide()
        else:
            #self.ui.pushButton_4.setChecked = 1
            self.ui.pushButton_4.setText("Edit activated")
            self.button_add.show()
            
                    
            

    def build_text(self):
        self.ui.pushButton.setText("Exit")
        self.ui.pushButton_2.setText("Top 100")
        self.ui.pushButton_3.setText("Numbers")
        self.ui.pushButton_5.setText("Weekdays")
        self.ui.pushButton_4.setText("Edit activated")

        self.button_add = QPushButton(self.ui.SideMenu)
        self.ui.verticalLayout.insertWidget(3, self.button_add)
        self.button_add.setText("+")

        fp_top100 = "./data/mandb.csv"
        fp_numbers = "./data/numdb.csv"
        fp_weekdays = "./data/weekdays.csv"
        
        self.ui.pushButton.pressed.connect(self.exit_application)
        self.ui.pushButton_2.pressed.connect(lambda: self.load_data(fp_top100))
        self.ui.pushButton_3.pressed.connect(lambda: self.load_data(fp_numbers))
        self.ui.pushButton_5.pressed.connect(lambda: self.load_data(fp_weekdays))
        self.button_add.pressed.connect(lambda: self.add_items("test"))
        
        self.ui.pushButton_4.pressed.connect(self.checker_button)


    def add_items(self, name):
        new_button = QPushButton(self.ui.SideMenu)
        new_button.setText(name)
        self.ui.verticalLayout.insertWidget(3, new_button)
        

    def load_data(self, filepath):
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