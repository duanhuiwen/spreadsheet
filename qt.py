# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created: Sat May 16 21:42:18 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(728, 600)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setRowCount(25)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(22, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(23, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(24, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.action_5 = QtGui.QAction(MainWindow)
        self.action_5.setObjectName(_fromUtf8("action_5"))
        self.action_6 = QtGui.QAction(MainWindow)
        self.action_6.setObjectName(_fromUtf8("action_6"))
        self.action_7 = QtGui.QAction(MainWindow)
        self.action_7.setObjectName(_fromUtf8("action_7"))
        self.action_8 = QtGui.QAction(MainWindow)
        self.action_8.setObjectName(_fromUtf8("action_8"))
        self.action_9 = QtGui.QAction(MainWindow)
        self.action_9.setObjectName(_fromUtf8("action_9"))
        self.action_10 = QtGui.QAction(MainWindow)
        self.action_10.setObjectName(_fromUtf8("action_10"))
        self.action_11 = QtGui.QAction(MainWindow)
        self.action_11.setObjectName(_fromUtf8("action_11"))
        self.action_12 = QtGui.QAction(MainWindow)
        self.action_12.setObjectName(_fromUtf8("action_12"))
        self.action_13 = QtGui.QAction(MainWindow)
        self.action_13.setObjectName(_fromUtf8("action_13"))
        self.action_14 = QtGui.QAction(MainWindow)
        self.action_14.setObjectName(_fromUtf8("action_14"))
        self.action_15 = QtGui.QAction(MainWindow)
        self.action_15.setObjectName(_fromUtf8("action_15"))
        self.action_16 = QtGui.QAction(MainWindow)
        self.action_16.setObjectName(_fromUtf8("action_16"))
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionSave)
        self.menu_2.addSeparator()
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_5)
        self.menu_2.addAction(self.action_6)
        self.menu_2.addAction(self.action_7)
        self.menu_2.addAction(self.action_8)
        self.menu_2.addAction(self.action_9)
        self.menu_2.addAction(self.action_10)
        self.menu_3.addAction(self.action_11)
        self.menu_3.addAction(self.action_12)
        self.menu_3.addAction(self.action_13)
        self.menu_3.addAction(self.action_14)
        self.menu_3.addAction(self.action_15)
        self.menu_3.addAction(self.action_16)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "pExcel", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4", None))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5", None))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6", None))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7", None))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8", None))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9", None))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10", None))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11", None))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "12", None))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "13", None))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "14", None))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15", None))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "16", None))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "17", None))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "18", None))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "20", None))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "21", None))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "22", None))
        item = self.tableWidget.verticalHeaderItem(21)
        item.setText(_translate("MainWindow", "23", None))
        item = self.tableWidget.verticalHeaderItem(22)
        item.setText(_translate("MainWindow", "24", None))
        item = self.tableWidget.verticalHeaderItem(23)
        item.setText(_translate("MainWindow", "25", None))
        item = self.tableWidget.verticalHeaderItem(24)
        item.setText(_translate("MainWindow", "26", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "A", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "B", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "C", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "D", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "E", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "F", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "G", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "H", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "I", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "J", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "K", None))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "L", None))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "M", None))
        self.menu.setTitle(_translate("MainWindow", "File", None))
        self.menu_2.setTitle(_translate("MainWindow", "BG-color", None))
        self.menu_3.setTitle(_translate("MainWindow", "font-color", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.action_5.setText(_translate("MainWindow", "red", None))
        self.action_6.setText(_translate("MainWindow", "blue", None))
        self.action_7.setText(_translate("MainWindow", "yellow", None))
        self.action_8.setText(_translate("MainWindow", "black", None))
        self.action_9.setText(_translate("MainWindow", "white", None))
        self.action_10.setText(_translate("MainWindow", "purple", None))
        self.action_11.setText(_translate("MainWindow", "red", None))
        self.action_12.setText(_translate("MainWindow", "blue", None))
        self.action_13.setText(_translate("MainWindow", "yellow", None))
        self.action_14.setText(_translate("MainWindow", "black", None))
        self.action_15.setText(_translate("MainWindow", "white", None))
        self.action_16.setText(_translate("MainWindow", "purple", None))

