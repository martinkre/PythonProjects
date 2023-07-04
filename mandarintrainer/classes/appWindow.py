from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTableView
from ui.MainWindow1 import Ui_MainWindow
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
        #self.load_data()
    
    def call_loader():
        app = QApplication(sys.argv)
        window = MyApp()
        window.show()
        sys.exit(app.exec_())

    def load_data(self):
        # Path to your CSV file
        csv_file = './data/mandb.csv'

        # Read CSV data
        with codecs.open(csv_file, "r", encoding="utf-8-sig") as file:
            csv_data = list(csv.reader(file))

            # Set number of rows and columns in the table widget
        


        # Populate the table widget with CSV data
        for row in range(len(csv_data)):
            for col in range(len(csv_data[row])):
                item = QTableView(csv_data[row][col])
                self.ui.tableView(row, col, item)
        

    def exit_application(self):
        QApplication.quit()