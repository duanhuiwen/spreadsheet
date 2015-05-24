# -*- coding: utf-8 -*--
from PyQt4 import QtCore, QtGui
from PyQt4 import *
from PyQt4.QtCore import pyqtSignature, Qt
from qt import Ui_MainWindow
import sys
import re
import random
import os

class Ui(QtGui.QMainWindow, Ui_MainWindow, QtGui.QWidget):
    def __init__(self, parent=None):       
        QtGui.QMainWindow.__init__(self, parent)  
        self.seletedAreaBgColor = 4
        self.countOpt = 0
        self.setupUi(self)
        self.tableWidget.customContextMenuRequested[QtCore.QPoint].connect(self.tableWidgetContext)
        # self.tableWidget.currentItemChanged.connect(self.hahah)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL('currentItemChanged(QTableWidgetItem*, QTableWidgetItem*)'), self.myCalculation)  
        ## open file 
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFile)
        ## set bg-color
        self.action_5.triggered.connect(self.action5)
        self.action_6.triggered.connect(self.action6)
        self.action_7.triggered.connect(self.action7)
        self.action_8.triggered.connect(self.action8)
        self.action_9.triggered.connect(self.action9)
        self.action_10.triggered.connect(self.action10)
        ## set font-color
        self.action_11.triggered.connect(self.action11)
        self.action_12.triggered.connect(self.action12)
        self.action_13.triggered.connect(self.action13)
        self.action_14.triggered.connect(self.action14)
        self.action_15.triggered.connect(self.action15)  
        self.action_16.triggered.connect(self.action16)          
        self.chMap = dict()
        i = 0
        self.chMap['A'] = i
        i = i + 1
        self.chMap['B'] = i
        i = i + 1
        self.chMap['C'] = i
        i = i + 1
        self.chMap['D'] = i
        i = i + 1
        self.chMap['E'] = i
        i = i + 1
        self.chMap['F'] = i
        i = i + 1
        self.chMap['G'] = i
        i = i + 1
        self.chMap['H'] = i
        i = i + 1
        self.chMap['I'] = i
        i = i + 1
        self.chMap['J'] = i
        i = i + 1
        self.chMap['K'] = i
        i = i + 1
        self.chMap['L'] = i
        i = i + 1
        self.chMap['M'] = i
        i = i + 1
        self.chMap['N'] = i
        i = i + 1
       
    
    def myCalculation(self, nitem, pitem):
        # print "myCalculation"
        if pitem:
            print('pitem',pitem.text())
            print('nitem',nitem)
            if pitem.text():
                text = str(pitem.text())
                # text = processExpr(text)
                s = re.sub(r' ', '',text)
                s = re.sub(r'\t', '',s).upper()
                if s[0] == '=':
                    # print  "try to myCalculation....."
                    patt = re.compile(r"\((.*?)\)", re.I|re.X)
                    rx = re.findall(patt , s)
                    if len(rx) < 1:
                        return
                    if s[1] == 'S' and s[2] == 'U' and s[3] == 'M':
                        cmds = rx[0].split(',')
                        addVal = 0
                        for cmd in cmds:
                            if (len(cmd) < 2):
                                continue
                            c = self.chMap[cmd[0]]
                            r = int(cmd[1:]) - 1
                            it = self.tableWidget.item(r, c) 
                            if it and it.text():
                                addVal = addVal + int(it.text())                        
                        pitem.setText(str(addVal))
                    elif s[1] == 'S' and s[2] == 'U' and s[3] == 'B':
                       print ("suB.....")
                    elif s[1] == 'M' and s[2] == 'U' and s[3] == 'L':
                        print ("MUL....")
                    elif s[1] == 'D' and s[2] == 'I' and s[3] == 'V':
                        print ("div.....")
                print (s)
    # def processExpr(self, expr):

    # def evalMin(self):

    # def evalMax(self):

    def tableWidgetContext(self):        
        popMenu = QtGui.QMenu()       
        about = QtGui.QAction(u'add', self)
        about.triggered.connect(self.add)
        popMenu.addAction(about)
        about = QtGui.QAction(u'minus', self)
        about.triggered.connect(self.sub)
        popMenu.addAction(about)
        about = QtGui.QAction(u'multiply', self)
        about.triggered.connect(self.mul)
        popMenu.addAction(about)
        about = QtGui.QAction(u'divide', self)
        about.triggered.connect(self.div)
        popMenu.addAction(about)
        about = QtGui.QAction(u'min', self)
        about.triggered.connect(self.min)
        popMenu.addAction(about)
        about = QtGui.QAction(u'max', self)
        about.triggered.connect(self.max)
        popMenu.addAction(about)
        popMenu.exec_(QtGui.QCursor.pos())
    def openFile(self):
        print ("open file....")
        filename = QtGui.QFileDialog.getOpenFileName(parent=self, caption='Open file')
        print ('filename:', filename)
        for i in range(25):            
            for j in range(13):
                it1 = self.tableWidget.item(i, j)                
                if it1:
                    self.tableWidget.setItem(i, j, QtGui.QTableWidgetItem(""))
        fl = open(filename, 'r')
        cPos = 0
        rPos = 0 
        for line in fl:
            line = line.strip()
            its =  line.split('~')
            if len(its):
                cPos = 0
                for it in its:
                    tr = it.split('-')
                    rPos = int(tr[0])
                    cPos = int(tr[1])
                    self.tableWidget.setItem(rPos, cPos, QtGui.QTableWidgetItem(tr[2]))
                    cPos = cPos + 1
                rPos = rPos + 1
        fl.close()
    def saveFile(self):
        print ("save file....")
        filename = QtGui.QFileDialog.getSaveFileName(parent=self, caption='Save file')

        print ('filename:', filename)
        
        fl = open(filename, 'w')   
        print ("open....")    
        cnt = ""
        for i in range(25):
            rc = ""
            for j in range(13):
                it1 = self.tableWidget.item(i, j)                
                if it1:
                    if it1.text():
                        if rc == "":
                            rc = str(i) + "-" + str(j) + "-" + it1.text()
                        else:
                            rc = rc + "~" + str(i) + "-" + str(j) + "-" + it1.text()
            if rc == "":                
                pass
            else:                
                cnt = cnt + rc + "\n"

        fl.write(cnt)
        fl.close()
        # print 'filter:', filter
    def operate(self, opt=0):
        # opt = self.countOpt
        rows = set()
        cols = set()
        for idx in self.tableWidget.selectedIndexes():
            rows.add(idx.row())
            cols.add(idx.column())
        lc = len(cols)
        # if len(cols) != 2 and opt < 4:
        #     return
        cls = list(cols)
        c1 = cls[0]
        c2 = cls[1]
        mxCol = max(cols) + 1
        mnCol = min(cols)
        print("mxcol:", mxCol)
        # print mxCol
        # print mnCol
        # print "max cl" + str(mxCol)       
        # print opt
        if opt < 0:
            for row in rows:            
                it1 = self.tableWidget.item(row, c1)            
                it2 = self.tableWidget.item(row, c2)
                if not it1 or not it2:
                    continue
                if not it1.text():
                    continue
                if not it2.text():
                    continue
                if opt == 0:
                    val = str(int(it1.text()) + int(it2.text()))
                elif opt == 1:
                    val = str(int(it1.text()) - int(it2.text()))
                elif opt == 2:
                    val = str(int(it1.text()) * int(it2.text()))
                elif opt == 3:
                    val = str(int(it1.text()) / int(it2.text()))
                elif opt == 4:
                    val = str(min(int(it1.text()), int(it2.text())))
                elif opt == 5:
                    val = str(max(int(it1.text()), int(it2.text())))
                self.tableWidget.setItem(row, mxCol, QtGui. QTableWidgetItem(val))
        else:
            for row in rows:
                it = [] 
                mmn = 9999999999990
                mmx = -9999999999999 
                mnval = mmn
                mxval = mmx 
                
                addVal = 0
                minusVal = 0
                mulVal = 1
                divVal = 1
                minusValF = False
                mulValF = False
                divValF = False
                for col in cols:
                    iti = self.tableWidget.item(row, col)
                    if not iti:
                        continue
                    if not iti.text():
                        continue
                    addVal = addVal + int(iti.text())
                    if not minusValF:
                        minusValF = True
                        minusVal = int(iti.text())
                    else:
                        minusVal = minusVal - int(iti.text())
                    if not divValF:
                        divValF = True
                        divVal = int(iti.text())
                    else:
                        divVal = divVal / float(iti.text())
                    if not mulValF:
                        mulValF = True
                        mulVal = float(iti.text())
                    else:
                        mulVal = mulVal * float(iti.text())
                    mnval = min(mnval, int(iti.text()))
                    mxval = max(mxval, int(iti.text()))
                # print "min " + str(mnval)
                # print "max " + str(mxval)
                # print "addVal " + str(addVal)
                # print "minusVal " + str(minusVal)
                # print "mulVal " + str(mulVal)
                # print "divVal " + str(divVal)
                if opt == 0:
                    self.tableWidget.setItem(row, mxCol, QtGui. QTableWidgetItem(str(addVal)))
                elif opt == 1:
                    self.tableWidget.setItem(row, mxCol, QtGui. QTableWidgetItem(str(minusVal)))
                elif opt == 2:
                    self.tableWidget.setItem(row, mxCol, QtGui. QTableWidgetItem(str(mulVal)))
                elif opt == 3:
                    self.tableWidget.setItem(row, mxCol, QtGui. QTableWidgetItem(str(divVal)))               
                elif opt == 4:
                    self.tableWidget.setItem(row, mxCol, QtGui. QTableWidgetItem(str(mnval)))
                else:
                    self.tableWidget.setItem(row, mxCol, QtGui. QTableWidgetItem(str(mxval)))
      
    def mix(self):
        print ("mix...")       
        rows = set()
        cols = set()
        for idx in self.tableWidget.selectedIndexes():
            rows.add(idx.row())
            cols.add(idx.column())
        if len(cols) != 3:
            return
        cls = list(cols)
        c1 = cls[0]
        c2 = cls[1]
        c3 = cls[2]
        # print c1
        # print c2
        mxCol = max(max(c1, c2), c3) + 1       
        for row in rows:
            it1 = self.tableWidget.item(row, c1)
            it2 = self.tableWidget.item(row, c2)
            it3 = self.tableWidget.item(row, c3)
            if not it1 or not it2 or not it3:
                continue
            if not it1.text():
                continue
            if not it2.text():
                continue
            if not it3.text():
                continue
            it1 = self.tableWidget.item(row, c1)
            it2 = self.tableWidget.item(row, c2)
            it3 = self.tableWidget.item(row, c3)
            val1 = max(int(it1.text()), int(it2.text()))
            val = str(val1 + int(it3.text()))      
            self.tableWidget.setItem(row, mxCol, QtGui.QTableWidgetItem(val))
        print (rows)
        print (cols)
    def add(self, opt=0):
        print ("add...")       
        self.operate(0)        
    def sub(self):
        print ("sub..." )       
        self.operate(1)
    def mul(self):
        print ("mul...")        
        self.operate(2)
    def div(self):
        print ("div...")        
        self.operate(3)
    def min(self):
        print ("min...")       
        self.operate(4)
    def max(self):
        print ("max...")       
        self.operate(5)
    def addItem(self):
        print ("addItem....")
        print (self.tableWidget.selectedItems())
        pass  
    def close():
        pass  
    def changSelectedAreadBgcolor(self, opt = 0):        
        for idx in self.tableWidget.selectedIndexes():
            item = self.tableWidget.item(idx.row(), idx.column())
            if not item:
                self.tableWidget.setItem(idx.row(), idx.column(), QtGui.QTableWidgetItem(""))
                item = self.tableWidget.item(idx.row(), idx.column())    
            if opt == 0:
                item.setBackgroundColor(QtGui.QColor(255,0,0)) 
            elif opt == 1:
                item.setBackgroundColor(QtGui.QColor(0,0,255))
            elif opt == 2:
                item.setBackgroundColor(QtGui.QColor(255,255,0)) 
            elif opt == 3:
                item.setBackgroundColor(QtGui.QColor(0,0,0)) 
            elif opt == 4:
                item.setBackgroundColor(QtGui.QColor(255,255,255)) 
            elif opt == 5:
                item.setBackgroundColor(QtGui.QColor(255,0,255))
    def changSelectedAreadFontcolor(self, opt=4):
         for idx in self.tableWidget.selectedIndexes():
            item = self.tableWidget.item(idx.row(), idx.column())
            if not item:
                self.tableWidget.setItem(idx.row(), idx.column(), QtGui.QTableWidgetItem(""))
                item = self.tableWidget.item(idx.row(), idx.column())    
            if opt == 0:
                item.setTextColor(QtGui.QColor(255,0,0)) 
            elif opt == 1:
                item.setTextColor(QtGui.QColor(0,0,255))
            elif opt == 2:
                item.setTextColor(QtGui.QColor(255,255,0)) 
            elif opt == 3:
                item.setTextColor(QtGui.QColor(0,0,0)) 
            elif opt == 4:
                item.setTextColor(QtGui.QColor(255,255,255)) 
            elif opt == 5:
                item.setTextColor(QtGui.QColor(255,0,255))

    def action5(self, opt=0): #bg-color: red
        print ("in action5..")   
        self.changSelectedAreadBgcolor(0)   
    def action6(self): #bg-color: blue
        print ("in action6..")        
        self.changSelectedAreadBgcolor(1)   
             
    def action7(self): #bg-color: yellow
        print ("in action7..")             
        self.changSelectedAreadBgcolor(2)    
    def action8(self): #bg-color: black
        print ("in action8..")        
        self.changSelectedAreadBgcolor(3)          
            
    def action9(self): #bg-color: black
        print ("in action9..")       
        self.changSelectedAreadBgcolor(4)               
    def action10(self): #bg-color: zise
        print ("in action10..")     
        self.changSelectedAreadBgcolor(5)     

    def action11(self): #font-color: red
        print ("in action11..")   
        self.changSelectedAreadFontcolor(0)    
    def action12(self): #font-color: red
        print ("in action12..")   
        self.changSelectedAreadFontcolor(1)    
    def action13(self): #font-color: red
        print ("in action13..")   
        self.changSelectedAreadFontcolor(2)    
    def action14(self): #font-color: red
        print ("in action14..")   
        self.changSelectedAreadFontcolor(3)  
    def action15(self): #font-color: red
        print ("in action15..")   
        self.changSelectedAreadFontcolor(4)     
    def action16(self): #font-color: red
        print ("in action16..")   
        self.changSelectedAreadFontcolor(5)     
  
    
    def actionHandler(self):  
        print ('action handler')  
if __name__ == '__main__': 
      
    app = QtGui.QApplication(sys.argv)
    window = Ui()   
    window.show()    
    sys.exit(app.exec_())
