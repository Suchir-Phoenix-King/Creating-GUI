# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:30:34 2022

@author: PC_RC
"""

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Creating using Classes 2")
root.geometry("900x600")
root.configure(background="lightblue")

component_list = ["label", "dropdown", "button"]
dropdown = ttk.Combobox(root, state = "readonly", values = component_list)
dropdown.pack()

class CreateElements:
    
    def __init__(self):
        print("This is CreateElements class")
        
    def createLabel(self):
        label = Label(root, text = "A | L-A-B-E-L | H-A-S | B-E-E-N | C-R-E-A-T-E-D", fg = "darkblue", bg = "lightblue")
        label.pack()
    
    def createButton(self):
        btn = Button(root, text = "B-U-T-T-O-N", command = self.message, bg = "darkblue", fg = "lightblue")
        btn.pack(padx = 20, pady = 10)
        
    def createDropDown(self):
        the_list = ["random", "don't click", "digital"]
        created_dropdown = ttk.Combobox(root, state = "readonly", values = the_list)
        created_dropdown.pack()
        
    def choose():
        global dropdown
        element = dropdown.get()
        if (element == "label"):
            createLabel()
        elif (element == "button"):
            createButton()
        elif (element == "dropdown"):
            createDropDown()
        
    def message(self):
        print("YOU HAVE CREATED ME, A BUTTON USING THE HOLY BUTTON")


obj_of_CreateElements = CreateElements()

btn = Button(root, text = "I | A-M | T-H-E | R-O-B-O | B-U-T-T-O-N | C-L-I-C-K | M-E", command = obj_of_CreateElements.choose())
btn.pack(padx = "10", pady = "20")

root.mainloop()