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
    dlg.tableWidget.clearSelection()
    while(dlg.tableWidget.rowCount ()>0):
        dlg.tableWidget.removeRow(0)
        dlg.tableWidget.clearSelection()

def addUser():
        name = dlg.lineEdit.text()
        date = dlg.lineEdit_date.text()
        admin = dlg.checkBox.isChecked()
        a = 0
        if admin:
            a = 1
        if name.strip(" ") != "" and date.strip(" ") != "":    
            users = (name,int(date),a)
            helper.insert("INSERT INTO users (name,year,admin) VALUES(?,?,?)",users)
            clearData()
            loadData()
        else:
            show_message("Error")
            
def show_message(title="Test", message="Test"):
    QMessageBox.information(None, title, message)            

def selectionChanged():
    selected_row = getSelectedRowId()
    user_id = getSelectionUserId()
    name = dlg.tableWidget.item(selected_row,1).text()
    date = dlg.tableWidget.item(selected_row,2).text()
    admin = dlg.tableWidget.item(selected_row,3).text()
    if admin == "1":
        dlg.checkBox.setChecked(True)
    else:
        dlg.checkBox.setChecked(False)
    dlg.lineEdit.setText(name)
    dlg.lineEdit_date.setText(date)
    
def getSelectedRowId(): 
    return dlg.tableWidget.currentRow()

def getSelectionUserId():
    return dlg.tableWidget.item(getSelectedRowId(),0).text()    


def deleteUser():
    id_delete = getSelectionUserId()
    helper.delete("DELETE FROM users WHERE id ="+id_delete)
    refresh()


def refresh():
    clearData()
    loadData()

def updateUser():
        id_update = getSelectionUserId()
        name = dlg.lineEdit.text()
        date = dlg.lineEdit_date.text()
        admin = dlg.checkBox.isChecked()
        a = 0
        if admin:
            a = 1
        if name.strip(" ") != "" and date.strip(" ") != "":    
            users = (name,int(date),a)
            helper.edit("UPDATE users SET name=?, year =?, admin=? WHERE id="+id_update,users)
            clearData()
            loadData()
        else:
            show_message("Error")   

dlg.tableWidget.itemSelectionChanged.connect(selectionChanged)
        
dlg.pushButton_2.clicked.connect(addUser)



dlg.pushButton_delete.clicked.connect(deleteUser)

dlg.pushButton_update.clicked.connect(updateUser)

dlg.pushButton.clicked.connect(loadData)

dlg.show()
app.exec()
        
        
        



dlg.show()
app.exec()