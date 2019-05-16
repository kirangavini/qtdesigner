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


def loadData():
    helper = SqliteHelper("test.db")
    users = helper.select("SELECT * FROM users")

    for row_number,user in enumerate(users):
        dlg.tableWidget.insertRow(row_number)
        for column_number,data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(str(data))
            dlg.tableWidget.setItem(row_number,column_number,cell)
        
dlg.pushButton.clicked.connect(loadData)


dlg.show()
app.exec()