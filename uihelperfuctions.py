# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:46:37 2019

@author: kiran
"""
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtWidgets import *
import os



class UIhelp:
    
    def checkpath(self,name):
        val = os.path.exists(name)
        if val == True:
            name = name
            pass
        else:
            self.show_message("Error","Path provided for python script is not valid")
            name = None
        return name 
    
    def getscriptname(self,path):
        path = r'D:\Ansysdev\electronics_qa\testsetlib\Products\EDT_ICEPAK\Scripts\shipped_examples\graphics_card.py'
        slash = []
        dot = []
        for eachidx in range(0,len(path)):
            if '\\' in path[eachidx]:
                slash.append(eachidx)
            if '.' in path[eachidx]:
                dot.append(eachidx)
                
        test_name = path[slash[-1]+1:dot[-1]]  
        return test_name
    
    def checkpythonfile(self,path):
    #path = r'D:\Ansysdev\electronics_qa\testsetlib\Products\EDT_ICEPAK\Scripts\shipped_examples\graphics_card.py'
        skip = False
        try:
            if '.py' in path:
                with open(path) as file:
                    for cnt,line in enumerate(file):
                        if 'Testing.scenario' in line and skip == False:
                            path = None
                            skip = True
                            self.show_message("Error","Python file provided is not compatable to convert, please use a new script")
                path = path
            else:
                path = None   
        except:
                path = None

        return [path,skip]
    
    def show_message(self,title,message):
      QMessageBox.information(None,title,message) 
      
      
   