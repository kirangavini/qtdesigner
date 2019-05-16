# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 23:02:57 2019

@author: kiran
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:48:22 2019

@author: kiran
"""

import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import json


app = QtWidgets.QApplication([])
dlg = uic.loadUi("listwidget.ui")



def addItem():
    if not dlg.lineEdit.text() == "":
        dlg.listWidget.addItem(dlg.lineEdit.text())      
        show_message("status","Item added to list")
        with open('data.json','r') as file:
            data = json.load(file)
            data["items"].append(dlg.lineEdit.text())
        with open('data.json','w') as file:
            json.dump(data,file) 
            show_message("Status","File saved")
        dlg.lineEdit.setText("")    
    else: 
        msg = QMessageBox()       
        msg.setIcon(QMessageBox.Critical)
        msg.setText("I/p O/P error")
        msg.setInformativeText("provide a value")
        msg.setWindowTitle("Error")
        msg.exec_()

        
def show_message(title,message):
      QMessageBox.information(None,title,message)      

def main():
    with open('data.json','r') as file:
        data = json.load(file)
    for item in data["items"]:
        dlg.listWidget.addItem(item)
    print(data)    
    

if __name__ == "__main__":
    main()
        
dlg.pushButton.clicked.connect(addItem)
dlg.lineEdit.returnPressed.connect(addItem)


dlg.show()
app.exec()


