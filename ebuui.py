# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:51:29 2019

@author: kiran
"""

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
import os
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtGui import QIcon
from uihelperfuctions import UIhelp




    
def get_required_paths():
    Products_path = None
    parts_path = None
    folder_name = None
    script_list = []
    script_list.append(None)
    script_list.append(False)
    uihelpfn = UIhelp()
    if not dlg.lineEdit.text() == "": 
            Products_path = uihelpfn.checkpath(dlg.lineEdit.text())  
    if not dlg.lineEdit_2.text() == "":
        parts_path =  uihelpfn.checkpath(dlg.lineEdit_2.text())      
    if not dlg.lineEdit_3.text() == "":
        folder_name = dlg.lineEdit_3.text()         
    if not dlg.lineEdit_4.text() == "":
        script_list = uihelpfn.checkpythonfile(uihelpfn.checkpath(dlg.lineEdit_4.text()))  
    if dlg.lineEdit_5.text() == "":
        test_name =  dlg.lineEdit_5.setText(uihelpfn.getscriptname(script_list[0]))
    else:
        test_name = dlg.lineEdit_5.text()
    validation_flag = dlg.checkBox.isChecked()
    move_flag = dlg.checkBox_2.isChecked()
    if (Products_path == None) or (parts_path == None) or (folder_name == None) or (script_list[0] == None):
        if script_list[1] == True:
            pass
        else:
            if Products_path == None: 
                uihelpfn.show_message("Error","Paths provided for products path is incorrect/does not exist")
            if parts_path == None:
                uihelpfn.show_message("Error","Paths provided for parts path is incorrect/does not exist")
            if folder_name == None:
                uihelpfn.show_message("Error","Folder name is not supported")
            if script_list[0] == None:
                uihelpfn.show_message("Error","Paths provided for script path is incorrect/does not exist") 
    else:      
        pathp = os.path.join(Products_path,'ARM_TESTS')
        paths = os.path.join(Products_path,'Scripts') 
        if os.path.exists(os.path.join(pathp,folder_name)) == False:
            os.makedirs(os.path.join(pathp,folder_name))
            uihelpfn.show_message("Info","New folder created in ARM_TESTS")
            if os.path.exists(os.path.join(paths,folder_name)) == False:
                os.makedirs(os.path.join(paths,folder_name))
                uihelpfn.show_message("Info","New folder created in Scripts")
        if os.path.exists(os.path.join(parts_path,folder_name)) == False:
            os.makedirs(os.path.join(parts_path,folder_name)) 
            uihelpfn.show_message("Info","New folder created in parts")
            
        username = os.getlogin()
        cpath = r'C:\Users'
        userslocation = os.path.join(cpath,username)
        documentslocation = os.path.join(userslocation,'Documents')
        filename = 'tcconfig.json'
        savelocation = os.path.join(documentslocation,filename)
        with open(savelocation,'w') as file:
            data = {}
            data["products_path"] = Products_path
            data["parts_path"] = parts_path
            data["folder_name"] = folder_name
            data["script_path"] = script_list[0]
            data["validation_flag"] = validation_flag
            data["move_flag"] = move_flag
            data["test_name"] = test_name
            json.dump(data,file) 
        text = str(Products_path) + str(parts_path) + str(folder_name) + str(script_list[0]) + str(validation_flag) +str(move_flag)
        uihelpfn.show_message("Success",text)
     

def main():   
    username = os.getlogin()
    cpath = r'C:\Users'
    userslocation = os.path.join(cpath,username)
    documentslocation = os.path.join(userslocation,'Documents')
    filename = 'tcconfig.json'
    uihelpfn = UIhelp()
    savelocation = os.path.join(documentslocation,filename)
    if os.path.exists(savelocation):
       with open(savelocation,'r') as file:
        data = json.load(file)
        dlg.lineEdit.setText(data["products_path"])
        dlg.lineEdit_2.setText(data["parts_path"])
        dlg.lineEdit_3.setText(data["folder_name"])
        dlg.lineEdit_4.setText(data["script_path"]) 
        dlg.lineEdit_5.setText(uihelpfn.getscriptname(data["script_path"]))
        if data["validation_flag"] == True:
             dlg.checkBox.setChecked(True)
        if data["move_flag"] == True:
            dlg.checkBox_2.setChecked(True)
            

import subprocess
file = r'C:\Users\kiran\Desktop\test.txt'
location = '"' + r'C:\Program Files (x86)\Notepad++\notepad++.exe' + '"'
location = location + ' ' + file

location = r'D:\ui'
p = subprocess.Popen(location)

os.system(location)


import subprocess
subprocess.Popen(r'explorer /select,'+ location)

p = subprocess.Popen([location,file], shell=True)
p.terminate()
p.wait()

subprocess.teminate([location,file])
    
    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    dlg = uic.loadUi("ebutc.ui")
    
    main()
        
    dlg.pushButton.clicked.connect(get_required_paths)
    dlg.lineEdit.returnPressed.connect(get_required_paths)


    dlg.show()
    app.exec()


