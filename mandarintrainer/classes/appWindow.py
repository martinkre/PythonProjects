from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTableView
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
        self.ui.pushButton_4.setText("Activated")
        self.ui.pushButton_4.pressed.connect(self.checker_button)

        self.load_data()
        self.build_text()
    
    def call_loader():
        app = QApplication(sys.argv)
        window = MyApp()
        window.show()
        sys.exit(app.exec_())

    def checker_button(self):
        
        
        if self.ui.pushButton_4.isChecked():
            #self.ui.pushButton_4.setChecked = 0
            self.ui.pushButton_4.setText("Deactivated")
        else:
            #self.ui.pushButton_4.setChecked = 1
            self.ui.pushButton_4.setText("Activated")

    def build_text(self):
        self.ui.pushButton.setText("Exit")
        self.ui.pushButton_2.setText("Top 100")
        self.ui.pushButton_3.setText("Numbers")
        self.ui.pushButton_5.setText("Weekdays")
        
        self.ui.pushButton.pressed.connect(self.exit_application)
        #self.ui.pushButton_2.pressed.connect()
        #self.ui.pushButton_3.pressed.connect()
        #self.ui.pushButton_5.pressed.connect()
        

    def load_data(self):
        # Path to your CSV file
        csv_file = './data/numdb.csv'

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