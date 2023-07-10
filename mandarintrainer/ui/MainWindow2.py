# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 562)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SideMenu = QtWidgets.QWidget(self.centralwidget)
        self.SideMenu.setMaximumSize(QtCore.QSize(391, 16777215))
        self.SideMenu.setStyleSheet(".QWidget {\n"
"    background-color: #adbacc\n"
"    \n"
"}\n"
"\n"
".QLineEdit {\n"
"    background-color: #333333;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f1f2;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"    color: #f0f1f2\n"
"\n"
"}\n"
"\n"
".QPushButton {\n"
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
".QPushButton:hover {\n"
"    color: #054269;\n"
"    background-color: #1973ab;\n"
"\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"    background-color: #054269;\n"
"    color: #adbacc;\n"
"\n"
"}\n"
"\n"
".QPushButton:checked {\n"
"    background-color: #40794f;\n"
"    color: #f0f1f2;\n"
"    border-color: #00cc00;\n"
"    \n"
"}\n"
"\n"
".QPushButton:checked:hover {\n"
"    background-color: #40aa4f;\n"
"    color: #f0f1f2;\n"
"    border-color: #00ff00;\n"
"    \n"
"}")
        self.SideMenu.setObjectName("SideMenu")
        self.gridLayout = QtWidgets.QGridLayout(self.SideMenu)
        self.gridLayout.setContentsMargins(-1, 9, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.SideMenu)
        self.pushButton_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.SideMenu)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.SideMenu)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.le_editor = QtWidgets.QWidget(self.SideMenu)
        self.le_editor.setEnabled(True)
        self.le_editor.setStyleSheet(".QPushButton {\n"
"    background-color: #0d2d53;\n"
"    color: #f0f1f2;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #f0f1f2;\n"
"    font: bold 14px;\n"
"    min-width: 1em;\n"
"    padding: 6px;\n"
"    \n"
"}\n"
"\n"
".QPushButton:hover {\n"
"    color: #054269;\n"
"    background-color: #1973ab;\n"
"\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"    background-color: #054269;\n"
"    color: #adbacc;\n"
"\n"
"}\n"
"\n"
".QPushButton:checked {\n"
"    background-color: #40794f;\n"
"    color: #f0f1f2;\n"
"    border-color: #00cc00;\n"
"    \n"
"}\n"
"\n"
".QPushButton:checked:hover {\n"
"    background-color: #40aa4f;\n"
"    color: #f0f1f2;\n"
"    border-color: #00ff00;\n"
"    \n"
"}")
        self.le_editor.setObjectName("le_editor")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.le_editor)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.le_editor)
        self.lineEdit.setMinimumSize(QtCore.QSize(99, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.pushButton_confirm = QtWidgets.QPushButton(self.le_editor)
        self.pushButton_confirm.setMinimumSize(QtCore.QSize(31, 0))
        self.pushButton_confirm.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.horizontalLayout_5.addWidget(self.pushButton_confirm)
        self.pushButton_cancel = QtWidgets.QPushButton(self.le_editor)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(31, 0))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_5.addWidget(self.pushButton_cancel)
        self.verticalLayout.addWidget(self.le_editor)
        self.pushButton_4 = QtWidgets.QPushButton(self.SideMenu)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.SideMenu)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(5, 2)
        self.verticalLayout.setStretch(6, 2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.SideMenu)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(391, 270))
        self.widget.setStyleSheet("QWidget {\n"
"    background-color: #333333\n"
"\n"
"}")
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.thatTable = QtWidgets.QTableView(self.widget)
        self.thatTable.setStyleSheet(".QTableView {\n"
"    color: #cccccc;\n"
"\n"
"}")
        self.thatTable.setObjectName("thatTable")
        self.gridLayout_3.addWidget(self.thatTable, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSide_Menu = QtWidgets.QAction(MainWindow)
        self.actionSide_Menu.setCheckable(True)
        self.actionSide_Menu.setChecked(True)
        self.actionSide_Menu.setObjectName("actionSide_Menu")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuView.addAction(self.actionSide_Menu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_confirm.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_cancel.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionSide_Menu.setText(_translate("MainWindow", "Side Menu"))
