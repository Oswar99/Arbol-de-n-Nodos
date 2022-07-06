# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:20:37 2019

@author: oswar-pc

"""
import time

class LinkedList:

  def __init__(self):
      self.first = None
      self.last = None
      self.location = None
      self.lenght = 0   
  
  def addLinkedList(self,ide,tpe,creation):
        if(not self.first):
           self.first = Node(ide,tpe,creation)
           self.last = self.first
           self.lenght = self.lenght + 1
          
           
        else:
          if(not self.searchLinkedList(ide)):
               temp = self.first
           
               while(temp.next):
                   temp = temp.next
              
           
               temp.next = Node(ide,tpe,creation)
               self.lenght = self.lenght + 1
               self.last = temp.next
               self.last.previous = temp
    
               
  def deleteLinkedList(self,id):
   if(self.first):
        if(self.first.name == id):
            self.first = self.first.next
          
            return True
        else:
            temp = self.first
            ant = None

            while(temp.next):
                if(temp.name == id):
                    if(temp.previous):
                        ant = temp.previous
                        ant.next = None
                    temp = temp.next
                    temp.previous = None
                    temp.previous = ant
                    ant.next = temp
                    while(ant.previous):
                        ant = ant.previous
                    
                    self.first = ant
                    self.lenght = self.lenght - 1
                    return True
                else:
                    temp = temp.next
                
            temp = temp.previous
            temp.next = None  
            return True
    
  def searchLinkedList(self, name):
      if(not self.first):
          return
      else:
          temp = self.first
          if(temp.name == name):
             return temp
          else:
             while((not temp.name == name) and temp.next):
                temp = temp.next
            
             if(temp.name == name):
                 return temp
             else:
                 return
                    
    
class Node:

   def __init__(self, ide, tpe, creation):
       self.value = LinkedList()
       self.father = LinkedList()
       self.name = ide
       self.tpe = tpe
       self.creation = creation
       self.next = None
       self.previous = None
   
class Tree:

   def __init__(self):
       self.root = Node("Raiz","folder", time.strftime("%c"))
       self.current = self.root
   
   def addTree(self, ide,tpe,creation):
       parent = self.current.value
       parent.addLinkedList(ide,tpe,creation)
    

   def deleteTree(self, element):
        parent = self.current.value
        parent.deleteLinkedList(element)
       
   
   def searchTree(self, name):
      parent = self.current.value
      r = parent.searchLinkedList(name)
      return r
 
