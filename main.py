# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:20:37 2019

@author: oswar-pc

"""

import os
import sys
import time
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QLineEdit,QListWidgetItem
from PyQt5.QtGui import QIcon
from structure import Tree,Node
fileDir = os.path.realpath('__file__')
fileRel = os.path.join(fileDir, '../Src/archivo.png')
fileRel = os.path.abspath(os.path.realpath(fileRel))

folderDir = os.path.realpath('__file__')
folderRel = os.path.join(folderDir, '../Src/Basic_Ui_14.jpg')
folderRel = os.path.abspath(os.path.realpath(folderRel))
"""
clases correspondientes a la estructura de datos
"""


    
class Simulacion_GUI(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("Simulacion.ui", self)

        self.tree= Tree()
        self.tree2= Tree()

        self.btnfold1.clicked.connect(self.addFolder)
        self.btnfold2.clicked.connect(self.addFolder2)
        self.btnDel1.clicked.connect(self.delFolder)
        self.btnDel2.clicked.connect(self.delFolder2)
        self.btnMovR2.clicked.connect(self.moveElementR)
        self.btnMovL2.clicked.connect(self.moveElementL)
        self.btnMovDer1.clicked.connect(self.moveElementsR)
        self.btnMov1.clicked.connect(self.moveElementsL)
        self.btnArch2.clicked.connect(self.addArchive2)
        self.btnArch1.clicked.connect(self.addArchive)

        self.list1.itemDoubleClicked.connect(self.showElement)
        self.list2.itemDoubleClicked.connect(self.showElement2)
        self.list1.itemClicked.connect(self.return1)
        self.list2.itemClicked.connect(self.return2)
      
    
   
    def moveElementsR(self):
        for i in range(self.list1.count()):
                sel = self.list1.item(i).text()

                if not(sel == "." or sel == ".."):
                     element = self.tree.searchTree(str(sel))
                       
                     self.tree2.addTree(element.name,element.tpe,element.creation)
                     element2 = self.tree2.searchTree(element.name)
                          
                     if(element.value):
                         element2 = self.tree2.searchTree(element.name)
                         element2.value = element.value       
                     
                     lst = self.tree2.current.value.first
                     self.list2.clear()
                     if not(self.line2.text() == "Raiz"):
                         self.list2.addItem(".")
                         self.list2.addItem("..")
                     while(lst.next):
                                 
                         icon = QListWidgetItem(self.list2)
                         icon.setText(lst.name)
                         
                         if(lst.tpe == "Archive"):
                             icon.setIcon(QIcon(fileRel))
                         else:
                             icon.setIcon(QIcon(folderRel))
                             
                         self.list1.addItem(icon)
                         lst = lst.next
                                  
                     icon = QListWidgetItem(self.list2)
                     icon.setText(lst.name)
                     
                     if(lst.tpe == "Archive"):
                         icon.setIcon(QIcon(fileRel))
                     else:
                         icon.setIcon(QIcon(folderRel))
                               
                     self.list1.addItem(icon)
    def moveElementsL(self):
        for i in range(self.list2.count()):
                sel = self.list2.item(i).text()

                if not(sel == "." or sel == ".."):
                     element = self.tree2.searchTree(str(sel))
                       
                     self.tree.addTree(element.name,element.tpe,element.creation)
                     element2 = self.tree.searchTree(element.name)
                          
                     if(element.value):
                         element2 = self.tree.searchTree(element.name)
                         element2.value = element.value       
                          
                     lst = self.tree.current.value.first
                     self.list1.clear()
                     if not(self.line.text() == "Raiz"):
                         self.list1.addItem(".")
                         self.list1.addItem("..")
                     while(lst.next):
                                 
                         icon = QListWidgetItem(self.list1)
                         icon.setText(lst.name)
                         
                         if(lst.tpe == "Archive"):
                             icon.setIcon(QIcon(fileRel))
                         else:
                             icon.setIcon(QIcon(folderRel))
                             
                         self.list1.addItem(icon)
                         lst = lst.next
                                  
                     icon = QListWidgetItem(self.list1)
                     icon.setText(lst.name)
                     
                     if(lst.tpe == "Archive"):
                         icon.setIcon(QIcon(fileRel))
                     else:
                         icon.setIcon(QIcon(folderRel))
                               
                     self.list1.addItem(icon)
    def moveElementR(self): 
        if(self.list1.selectedItems()):
            for i  in range(len(self.list1.selectedItems())):
                sel = self.list1.selectedItems()[i].text()

                if not(sel == "." or sel == ".."):
                     element = self.tree.searchTree(str(sel))
                       
                     self.tree2.addTree(element.name,element.tpe,element.creation)
                     element2 = self.tree2.searchTree(element.name)
                          
                     if(element.value):
                         element2 = self.tree2.searchTree(element.name)
                         element2.value = element.value       
                     
                     lst = self.tree2.current.value.first
                     self.list2.clear()
                     if not(self.line2.text() == "Raiz"):
                         self.list2.addItem(".")
                         self.list2.addItem("..")
                     while(lst.next):
                                 
                         icon = QListWidgetItem(self.list2)
                         icon.setText(lst.name)
                         
                         if(lst.tpe == "Archive"):
                             icon.setIcon(QIcon(fileRel))
                         else:
                             icon.setIcon(QIcon(folderRel))
                             
                         self.list1.addItem(icon)
                         lst = lst.next
                                  
                     icon = QListWidgetItem(self.list2)
                     icon.setText(lst.name)
                     
                     if(lst.tpe == "Archive"):
                         icon.setIcon(QIcon(fileRel))
                     else:
                         icon.setIcon(QIcon(folderRel))
                               
                     self.list1.addItem(icon)
    def moveElementL(self):
        if (self.list2.selectedItems()):
            for i  in range(len(self.list2.selectedItems())):
                sel = self.list2.selectedItems()[i].text()

                if not(sel == "." or sel == ".."):
                     element = self.tree2.searchTree(str(sel))
                       
                     self.tree.addTree(element.name,element.tpe,element.creation)
                     element2 = self.tree.searchTree(element.name)
                          
                     if(element.value):
                         element2 = self.tree.searchTree(element.name)
                         element2.value = element.value       
                          
                     lst = self.tree.current.value.first
                     self.list1.clear()
                     if not(self.line.text() == "Raiz"):
                         self.list1.addItem(".")
                         self.list1.addItem("..")
                     while(lst.next):
                                     
                         icon = QListWidgetItem(self.list1)
                         icon.setText(lst.name)
                         
                         if(lst.tpe == "Archive"):
                             icon.setIcon(QIcon(fileRel))
                         else:
                             icon.setIcon(QIcon(folderRel))
                             
                         self.list1.addItem(icon)
                         lst = lst.next
                                  
                     icon = QListWidgetItem(self.list1)
                     icon.setText(lst.name)
                     
                     if(lst.tpe == "Archive"):
                         icon.setIcon(QIcon(fileRel))
                     else:
                         icon.setIcon(QIcon(folderRel))
                               
                     self.list1.addItem(icon)
    def addCopied(self,nodo, original):
        temp = original.value.first
        name = original.name
        tpe =  original.tpe
        crea = original.creation
        
        if(not nodo.value.first):
            if(nodo.value.first.next):
                while(temp):
                    nodo.value.first = Node(name,tpe,crea, nodo.name)
                    if(temp.first):
                        temp = temp.first
                        nodo = nodo.first
                        self.addCopied(nodo,temp)
                        while(temp.next):
                            if(temp.next):
                                temp = temp.next
                                nodo = nodo.value.first.next
                                if(temp.first):          
                                    self.addCopied(nodo,temp)
                                    self.addCopied(nodo,temp)
                                else:
                                    return
                            else:
                                return
            else:
                self.addCopied(nodo,name)
    def return1(self):
         if(self.list1.currentItem().text() == "." or self.list1.currentItem().text() == ".."):
              if(self.list1.currentItem().text() == ".."):
                  if(not(self.line.text() == "Raiz")):
                      self.returnPrevious()
              else:
                   if(self.list1.currentItem().text() == "."):
                       if(not(self.line.text() == "Raiz")):
                          self.returnRoot()
    def return2(self):
         if(self.list2.currentItem().text() == "." or self.list2.currentItem().text() == ".."):
              if(self.list2.currentItem().text() == ".."):
                  if(not(self.line2.text() == "Raiz")):
                      self.returnPrevious2()
              else:
                   if(self.list2.currentItem().text() == "."):
                       if(not(self.line2.text() == "Raiz")):
                           self.returnRoot2()

    def returnPrevious(self):
       
        
         self.tree.current = self.tree.current.father     
         self.line.setText(self.tree.current.name)
         
         lst = self.tree.current.value.first
         self.list1.clear()
         if not(self.line.text() == "Raiz"):
             self.list1.addItem(".")
             self.list1.addItem("..")
         while(lst.next):
                 
             icon = QListWidgetItem(self.list1)
             icon.setText(lst.name)
         
             if(lst.tpe == "Archive"):
                 icon.setIcon(QIcon(fileRel))
             else:
                 icon.setIcon(QIcon(folderRel))
                                     
             self.list1.addItem(icon)
             lst = lst.next
                 
         icon = QListWidgetItem(self.list1)
         icon.setText(lst.name)
             
         if(lst.tpe == "Archive"):
             icon.setIcon(QIcon(fileRel))
         else:
             icon.setIcon(QIcon(folderRel))
              
         self.list1.addItem(icon)
   
             
    def returnPrevious2(self):
        
        self.tree2.current = self.tree2.current.father     
        self.line2.setText(self.tree2.current.name)
        
        lst = self.tree2.current.value.first
        self.list2.clear()
        if not(self.line2.text() == "Raiz"):
            self.list2.addItem(".")
            self.list2.addItem("..")
        while(lst.next):
                
            icon = QListWidgetItem(self.list2)
            icon.setText(lst.name)
            
            if(lst.tpe == "Archive"):
                icon.setIcon(QIcon(fileRel))
            else:
                icon.setIcon(QIcon(folderRel))
                                    
            self.list1.addItem(icon)
            lst = lst.next
                
        icon = QListWidgetItem(self.list2)
        icon.setText(lst.name)
            
        if(lst.tpe == "Archive"):
            icon.setIcon(QIcon(fileRel))
        else:
            icon.setIcon(QIcon(folderRel))
        
        self.list1.addItem(icon)
    
    
    def returnRoot(self):
       
            self.tree.previous = None
            
            self.tree.current = self.tree.root
            self.line.setText(self.tree.current.name)
            lst = self.tree.current.value.first
            self.list1.clear()
  
            while(lst.next):
                
                    icon = QListWidgetItem(self.list1)
                    icon.setText(lst.name)
            
                    if(lst.tpe == "Archive"):
                        icon.setIcon(QIcon(fileRel))
                    else:
                        icon.setIcon(QIcon(folderRel))
                                    
                    self.list1.addItem(icon)
                    lst = lst.next
                
            icon = QListWidgetItem(self.list1)
            icon.setText(lst.name)
            
            if(lst.tpe == "Archive"):
                icon.setIcon(QIcon(fileRel))
            else:
                icon.setIcon(QIcon(folderRel))
             
            self.list1.addItem(icon)
        
    def returnRoot2(self):
        
        self.tree.previous = None
        
        self.tree2.current = self.tree2.root
        self.line2.setText(self.tree.current.name)
        lst = self.tree2.current.value.first
        self.list2.clear()
 
        while(lst.next):
                
            icon = QListWidgetItem(self.list2)
            icon.setText(lst.name)
            
            if(lst.tpe == "Archive"):
                icon.setIcon(QIcon(fileRel))
            else:
                icon.setIcon(QIcon(folderRel))
                                    
            self.list1.addItem(icon)
            lst = lst.next
                
        icon = QListWidgetItem(self.list2)
        icon.setText(lst.name)
            
        if(lst.tpe == "Archive"):
            icon.setIcon(QIcon(fileRel))
        else:
            icon.setIcon(QIcon(folderRel))
             
        self.list1.addItem(icon)
        
    def addFolder(self):
        
        add, okPressed = QInputDialog.getText(self,"Ingresar", "Nombre: ", QLineEdit.Normal, "")
        if okPressed and add != '':
            
            self.tree.addTree(add,"Folder",time.strftime("%c"))
            
            lst = self.tree.current.value.first
            
            self.list1.clear()
            if not(self.line.text() == "Raiz"):
                self.list1.addItem(".")
                self.list1.addItem("..")
            while(lst.next):
                
                icon = QListWidgetItem(self.list1)
                icon.setText(lst.name)
            
                if(lst.tpe == "Archive"):
                    icon.setIcon(QIcon(fileRel))
                else:
                    icon.setIcon(QIcon(folderRel))
                                    
                self.list1.addItem(icon)
                lst = lst.next
                
            icon = QListWidgetItem(self.list1)
            icon.setText(lst.name)
            
            if(lst.tpe == "Archive"):
                icon.setIcon(QIcon(fileRel))
            else:
                icon.setIcon(QIcon(folderRel))
             
            self.list1.addItem(icon)
    def addFolder2(self):
        add, okPressed = QInputDialog.getText(self,"Ingresar", "Nombre: ", QLineEdit.Normal, "")
        if okPressed and add != '':
               
            self.tree2.addTree(add,"Folder",time.strftime("%c"))

            lst = self.tree2.current.value.first
            
            self.list2.clear()
            if not(self.line2.text() == "Raiz"):
                self.list2.addItem(".")
                self.list2.addItem("..")
            while(lst.next):
                
                icon = QListWidgetItem(self.list2)
                icon.setText(lst.name)
            
                if(lst.tpe == "Archive"):
                    icon.setIcon(QIcon(fileRel))
                else:
                    icon.setIcon(QIcon(folderRel))
             
                self.list2.addItem(icon)
                
                lst = lst.next
            icon = QListWidgetItem(self.list2)
            icon.setText(lst.name)
            
            if(lst.tpe == "Archive"):
                icon.setIcon(QIcon(fileRel))
            else:
                icon.setIcon(QIcon(folderRel))
             
            self.list2.addItem(icon)  
    def addArchive(self):
        
        add, okPressed = QInputDialog.getText(self,"Ingresar", "Nombre: ", QLineEdit.Normal, "")
        if okPressed and add != '':
            
            self.tree.addTree(add + ".oswar","Archive",time.strftime("%c"))
            
            lst = self.tree.current.value.first
            
            self.list1.clear()
            if not(self.line.text() == "Raiz"):
                self.list1.addItem(".")
                self.list1.addItem("..")
            while(lst.next):
                icon = QListWidgetItem(self.list1)
                icon.setText(lst.name)
                if(lst.tpe == "Archive"):
                    icon.setIcon(QIcon(fileRel))
                else:
                    icon.setIcon(QIcon(folderRel))
                
                self.list1.addItem(icon)
                
                lst = lst.next
                
            icon = QListWidgetItem(self.list1)
            icon.setText(lst.name)
            
            if(lst.tpe == "Archive"):
                icon.setIcon(QIcon(fileRel))
            else:
                icon.setIcon(QIcon(folderRel))
                
            self.list1.addItem(icon)
    def addArchive2(self):
        
        add, okPressed = QInputDialog.getText(self,"Ingresar", "Nombre: ", QLineEdit.Normal, "")
        if okPressed and add != '':
               
            self.tree2.addTree(add + ".oswar","Archive",time.strftime("%c"))
     
            lst = self.tree2.current.value.first
            
            self.list2.clear()
            if not(self.line2.text() == "Raiz"):
                self.list2.addItem(".")
                self.list2.addItem("..")
            while(lst.next):
                icon = QListWidgetItem(self.list2)
                icon.setText(lst.name)
            
                if(lst.tpe == "Archive"):
                    icon.setIcon(QIcon(fileRel))
                else:
                    icon.setIcon(QIcon(folderRel))
             
                self.list2.addItem(icon)
                lst = lst.next
                
            icon = QListWidgetItem(self.list2)
            icon.setText(lst.name)
            
            if(lst.tpe == "Archive"):
                icon.setIcon(QIcon(fileRel))
            else:
                icon.setIcon(QIcon(folderRel))
               
            self.list2.addItem(icon)  
    def delFolder(self):
        if(self.list1.selectedItems()):
            i = len(self.list1.selectedItems()) -1
            while(i >= 0):

                sel = self.list1.selectedItems()[i].text()

                if not(self.list1.selectedItems()[i].text() == "." or self.list1.selectedItems()[i].text() == ".."):
                     element = str(sel)
                     self.tree.deleteTree(element)
                i = i-1  
                
            self.list1.clear()
            if not(self.line.text() == "Raiz"):
                self.list1.addItem(".")
                self.list1.addItem("..")
            lst = self.tree.current.value.first
        
            if(lst != None):
                while(lst.next):
                    
                    icon = QListWidgetItem(self.list1)
                    icon.setText(lst.name)
                
                    if(lst.tpe == "Archive"):
                        icon.setIcon(QIcon(fileRel))
                    else:
                        icon.setIcon(QIcon(folderRel))
                                        
                    self.list1.addItem(icon)
                    lst = lst.next
                    
                icon = QListWidgetItem(self.list1)
                icon.setText(lst.name)
                
                if(lst.tpe == "Archive"):
                    icon.setIcon(QIcon(fileRel))
                else:
                    icon.setIcon(QIcon(folderRel))
                 
                self.list1.addItem(icon)
                
    def delFolder2(self):
        if(self.list2.selectedItems()):
            i = len(self.list2.selectedItems()) -1
            while(i >= 0):

                sel = self.list2.selectedItems()[i].text()

                if not(self.list2.selectedItems()[i].text() == "." or self.list2.selectedItems()[i].text() == ".."):
                     element = str(sel)
                     self.tree2.deleteTree(element)
                i = i-1 

            self.list2.clear()
            if not(self.line2.text() == "Raiz"):
                self.list2.addItem(".")
                self.list2.addItem("..")
            lst = self.tree2.current.value.first
            
            if(lst != None):
                while(lst.next):
                    
                    icon = QListWidgetItem(self.list2)
                    icon.setText(lst.name)
                
                    if(lst.tpe == "Archive"):
                        icon.setIcon(QIcon(fileRel))
                    else:
                        icon.setIcon(QIcon(folderRel))
                 
                    self.list2.addItem(icon)
                    
                    lst = lst.next
                icon = QListWidgetItem(self.list2)
                icon.setText(lst.name)
                
                if(lst.tpe == "Archive"):
                    icon.setIcon(QIcon(fileRel))
                else:
                    icon.setIcon(QIcon(folderRel))
                 
                self.list2.addItem(icon)  
                    
    def showElement(self):
         
        if(not(self.list1.currentItem().text() == "." or self.list1.currentItem().text() == "..")):

            if(self.tree.searchTree(str(self.list1.currentItem().text())).tpe != "Archive"):
                
                self.tree.searchTree(str(self.list1.currentItem().text())).father =self.tree.current
            
                self.tree.current = self.tree.searchTree(str(self.list1.currentItem().text()))
                self.line.setText(self.tree.current.name)
            
                lst = self.tree.current.value.first
                self.list1.clear()
                self.list1.addItem(".")
                self.list1.addItem("..")
                if(lst != None):
                    while(lst.next):
                    
                        icon = QListWidgetItem(self.list1)
                        icon.setText(lst.name)
                
                        if(lst.tpe == "Archive"):
                            icon.setIcon(QIcon(fileRel))
                        else:
                            icon.setIcon(QIcon(folderRel))
                                        
                        self.list1.addItem(icon)
                        lst = lst.next
                    
                    icon = QListWidgetItem(self.list1)
                    icon.setText(lst.name)
                
                    if(lst.tpe == "Archive"):
                        icon.setIcon(QIcon(fileRel))
                    else:
                        icon.setIcon(QIcon(folderRel))
                 
                    self.list1.addItem(icon)
            
    def showElement2(self):
       
        if(not(self.list2.currentItem().text() == "." or self.list2.currentItem().text() == "..")):
            if(self.tree2.searchTree(str(self.list2.currentItem().text())).tpe != "Archive"):
                
                self.tree2.searchTree(str(self.list2.currentItem().text())).father =self.tree2.current        
                
                self.tree2.current = self.tree2.searchTree(str(self.list2.currentItem().text()))
                self.line2.setText(self.tree2.current.name)
                
                lst = self.tree2.current.value.first
                self.list2.clear()
                self.list2.addItem(".")
                self.list2.addItem("..")
                if(lst != None):
                    while(lst.next):
                    
                        icon = QListWidgetItem(self.list2)
                        icon.setText(lst.name)
                
                        if(lst.tpe == "Archive"):
                            icon.setIcon(QIcon(fileRel))
                        else:
                            icon.setIcon(QIcon(folderRel))
                 
                        self.list2.addItem(icon)
                    
                        lst = lst.next
                        
                    icon = QListWidgetItem(self.list2)
                    icon.setText(lst.name)
                
                    if(lst.tpe == "Archive"):
                        icon.setIcon(QIcon(fileRel))
                    else:
                        icon.setIcon(QIcon(folderRel))
                 
                    self.list2.addItem(icon)  
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Simulacion_GUI()
    GUI.show()
    sys.exit(app.exec_())
    
    
 
