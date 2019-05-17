# -*- coding: utf-8 -*-
"""
Created on Wed May 15 21:48:17 2019

@author: kiran
"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

#from SqliteHelper import *
from sqlitehelperclass import *

app = QtWidgets.QApplication([])
dlg = uic.loadUi("tablewidget.ui")


helper = SqliteHelper("test.db")

def loadData():
    
    users = helper.select("SELECT * FROM users")
    for row_number,user in enumerate(users):
        dlg.tableWidget.insertRow(row_number)
        for column_number,data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(str(data))
            dlg.tableWidget.setItem(row_number,column_number,cell)
            
            
def clearData():
    while(dlg.tableWidget.rowCount ()>0):
        dlg.tableWidget.removeRow(0)

def addUser():
        name = dlg.lineEdit.text()
        date = dlg.lineEdit_date.text()
        admin = dlg.checkBox.isChecked()
        a = 0
        if admin:
            a = 1
        users = (name,int(date),a)
        helper.insert("INSERT INTO users (name,year,admin) VALUES(?,?,?)",users)
        clearData()
        loadData()


        
dlg.pushButton_2.clicked.connect(addUser)

dlg.pushButton.clicked.connect(loadData)

dlg.show()
app.exec()
        
        
        



dlg.show()
app.exec()