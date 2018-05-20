# -*- coding: utf-8 -*-
# !/usr/bin/env python
             
################################################                   ###    ####
#                                               #                  #  #   #   #
#  coded by      => Cihat Altiparmak            #                  #  #   #   #
#  creating_date => 19.05.2018                  #                  ####   #   #    
#  creating_time => 00.29                       #                  #  #   #   #
#  thank_to      => BDFrostbide and furkantokac #                  #  #   #   #
#  version       => 0.0.2                       #                  #  #   #   #
################################################                   ###    ####
"""
author's message:
 
BU Basit C EDITOR'u bilgisayarı programlamaya uygun olmayan herkes icindir.
Zaman oldukca gelistirilecektir.
Gule gule kullanın:)
"""


import sys
import os

from subprocess import Popen


from PyQt5.QtWidgets import QApplication as app

from PyQt5.QtWidgets import QMainWindow as main_window

from PyQt5.QtWidgets import QPlainTextEdit as text_edit

from PyQt5.QtWidgets import QAction as action

from PyQt5.QtWidgets import QFileDialog as file_dialog

from PyQt5.QtWidgets import QMessageBox as message_box

from PyQt5.QtWidgets import QDialog as Dialog

from PyQt5.QtWidgets import QHBoxLayout as HBoxLayout

from PyQt5.QtWidgets import QVBoxLayout as VBoxLayout

from PyQt5.QtWidgets import QLabel as Label

from PyQt5.QtWidgets import QPushButton as Button

from PyQt5.QtWidgets import QLineEdit as Line




class c_editor():
    open_file = ""
    is_change_file = None
    data_buf = None
    def run(self):
        if os.path.isfile(self.open_file):
            if self.is_change_file:

                if self.question_box(): Popen(["gcc",self.open_file])
                
                else: pass
            else: Popen(["gcc",self.open_file])
        else:
            running_file = self.save_as()
            if bool(running_file): 
                if os.path.isfile(running_file):
                    Popen(["gcc",running_file])

    def copy(self):
        self.text_area.copy()

    def cut(self):
        self.text_area.cut()

    def paste(self):
        self.text_area.paste()

    def new_file(self):
        if self.is_change_file and os.path.isfile(self.open_file):
            button_reply = message_box.question(self.main_wn,"Warning","You have a unsaved file.Do you want to  save changes?",message_box.Cancel|message_box.No|message_box.Yes|message_box.Cancel)  
            if button_reply == message_box.Yes:
                self.save()
                self.open_file = ""
                self.is_change_file = None
                self.main_wn.setWindowTitle("untitled.c")
            if button_reply == message_box.No:
                self.open_file = ""
                self.is_change_file = None
                self.text_area.document().setPlainText("")
                self.main_wn.setWindowTitle("untitled.c")
            if button_reply == message_box.Cancel:
                pass
                       
        else:
            self.text_area.document().setPlainText("")
            self.open_file = ""
            self.is_change_file = None
            self.main_wn.setWindowTitle("untitled.c")
            
    def save(self):
        if os.path.isfile(self.open_file):
            with open(self.open_file,"w") as f:
                f.write(self.text_area.document().toPlainText())
                self.main_wn.setWindowTitle(self.open_file)
        else:
            message_box.about(self.main_wn,"Warning","File didn't open here")
                

    def save_as(self): 
        options = file_dialog.Options()
        options |= file_dialog.DontUseNativeDialog
        file_name,_ = file_dialog.getSaveFileName(self.main_wn,"Save File", "," ,"All Files (*)",options=options)

        try:
            with open(file_name,"w") as f:
                f.write(self.text_area.document().toPlainText())
            return file_name

        except FileNotFoundError:
            pass
    def open(self):
        options = file_dialog.Options()
        options |= file_dialog.DontUseNativeDialog
        file_name,_ = file_dialog.getOpenFileName(self.main_wn,"Open File","","All Files (*)",options=options)
        
        with open(file_name,"r") as f:           
            self.text_area.document().setPlainText(f.read())
        self.open_file = file_name
        self.main_wn.setWindowTitle(file_name)


    def question_box(self):
        
        button_reply = message_box.question(self.main_wn,"Warning","You have a unsaved file.Do you want to  save changes?",message_box.Yes|message_box.Cancel)  
        if button_reply == message_box.Yes:
            self.save()
                
            self.is_change_file = None
            self.main_wn.setWindowTitle(self.open_file)
            return True
        if button_reply == message_box.Cancel:
            return False

       

    def go_to_line(self):
        w = Dialog(self.main_wn)
        line1 = Line()
        line2 = Line()
        lab1 = Label("raw")
        lab2 = Label("column")
        btn = Button("go")

        main_lay = VBoxLayout()

        v1 = HBoxLayout()
        v1.addStretch(1)
        v1.addWidget(lab1)
        v1.addWidget(line1)

        v2 = HBoxLayout()
        v2.addStretch(1)
        v2.addWidget(lab2)
        v2.addWidget(line2)
        
        main_lay.addStretch(1)
        main_lay.addLayout(v1)
        main_lay.addLayout(v2)
        main_lay.addWidget(btn)
        
        
        w.setLayout(main_lay)
        
         
        w.exec_()
    
        

        
        
        

    def correct(self):
        if os.path.isfile(self.open_file):
            self.is_change_file = True
            self.main_wn.setWindowTitle("*"+self.open_file)

    def __init__(self):
        self.app_ = app(sys.argv)
        self.main_wn = main_window()
        menu_bar = self.main_wn.menuBar()
        #---------------------------------------------------
        file_menu = menu_bar.addMenu("File")
        
        new_file_action = action("New File",self.main_wn)
        new_file_action.triggered.connect(self.new_file)

        save_action = action("Save",self.main_wn)
        save_action.triggered.connect(self.save)

        save_as_action = action("Save As",self.main_wn)
        save_as_action.triggered.connect(self.save_as)

        open_action = action("Open",self.main_wn)
        open_action.triggered.connect(self.open)

        go_to_line_action = action("Go To Line",self.main_wn)
        go_to_line_action.triggered.connect(self.go_to_line)
        

        file_menu.addAction(new_file_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addAction(open_action)
        file_menu.addAction(go_to_line_action)
        #----------------------------------------------------------
        edit_menu = menu_bar.addMenu("Edit")

        copy_action = action("Copy all",self.main_wn)
        copy_action.triggered.connect(self.copy)

        cut_action = action("Cut all",self.main_wn)
        cut_action.triggered.connect(self.cut)
        
        paste_action = action("Paste",self.main_wn)
        paste_action.triggered.connect(self.paste)

        edit_menu.addAction(copy_action)
        edit_menu.addAction(cut_action)
        edit_menu.addAction(paste_action)

        #--------------------------------------------------------------
        
        run_menu = menu_bar.addMenu("Run")

        run_action = action("Run",self.main_wn)
        run_action.triggered.connect(self.run)

        run_menu.addAction(run_action)

        #----------------------------------------------------------------


        self.text_area = text_edit()
        help(self.text_area)
        self.main_wn.setCentralWidget(self.text_area)
        self.text_area.textChanged.connect(lambda: self.correct())
        self.main_wn.setWindowTitle("C Compiler")
        self.text_area.document().setPlainText("Type text in here")

        self.main_wn.show()

        sys.exit(self.app_.exec_())


a = c_editor()
