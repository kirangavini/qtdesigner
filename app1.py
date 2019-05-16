# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:48:22 2019

@author: kiran
"""

import sys
from PyQt5 import QtWidgets,uic

def check_fun(word):
    if type(word) == str:
        print('working')
       # sys.exit(1)

def Convert():
    check_fun(dlg.lineEdit.text())
    dlg.lineEdit_2.setText(str(float(dlg.lineEdit.text())*0.8))



app = QtWidgets.QApplication([])
dlg = uic.loadUi("converter.ui")

dlg.lineEdit.setPlaceholderText("Euro")
dlg.pushButton.clicked.connect(Convert)
dlg.lineEdit.returnPressed.connect(Convert)
dlg.lineEdit_2.setReadOnly(True)
dlg.show()
app.exec()


