# -*- coding: utf-8 -*-

################################################                   ###    ####
#                                               #                  #  #   #   #
#  coded by      => Cihat Altiparmak            #                  #  #   #   #
#  creating_date => 19.05.2018                  #                  ####   #   #
#  creating_time => 00.29                       #                  #  #   #   #
#  thank_to      => BDFrostbide and furkantokac #                  #  #   #   #
#  version       => 1.0.0                       #                  #  #   #   #
################################################                   ###    ####
"""
author's message:

BU Basit C EDITOR'u bilgisayarı programlamaya uygun olmayan herkes icindir.
Zaman oldukca gelistirilecektir.
Gule gule kullanın:)
"""
 

import sys
import os
import json
from subprocess import Popen
from functools import partial
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QFileDialog, \
    QDialog, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QAction, \
    QMessageBox
from PyQt5.QtGui import QIcon, QTextCursor, QFont

from text_area import My_Text_Area
from brusher import c_highlighter
from Themes import Themes
from ColorizePopup import Colorize
from errorPopups import FileCannotOpenErrorDialog
from programmingChoices import Lang

__author__ = "Cihat Altiparmak"
__version__ = "0.0.2"



class Electra(QMainWindow):
    def __init__(self):
        super().__init__()
        self.open_file = ""
        self.is_change_file = False

        with open("settings.json") as f:
            self.settings_data = json.loads(f.read())

        self.init_iu()

    def init_iu(self):
        # ---> Menu Bar
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("File")

        new_file_action = QAction("New File", self)
        new_file_action.triggered.connect(self.new_file)
        file_menu.addAction(new_file_action)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save)
        file_menu.addAction(save_action)

        save_as_action = QAction("Save As", self)
        save_as_action.triggered.connect(self.save_as)
        file_menu.addAction(save_as_action)

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open)
        file_menu.addAction(open_action)

        go_to_line_action = QAction("Go To Line", self)
        go_to_line_action.triggered.connect(self.go_to_line)
        file_menu.addAction(go_to_line_action)

        # Edit menu
        edit_menu = menu_bar.addMenu("Edit")

        copy_action = QAction("Copy all", self)
        copy_action.triggered.connect(self.copy)
        edit_menu.addAction(copy_action)

        cut_action = QAction("Cut all", self)
        cut_action.triggered.connect(self.cut)
        edit_menu.addAction(cut_action)

        paste_action = QAction("Paste", self)
        paste_action.triggered.connect(self.paste)
        edit_menu.addAction(paste_action)

        # Run menu
        run_menu = menu_bar.addMenu("Run")

        run_action = QAction("Run", self)
        run_action.triggered.connect(self.run)
        run_menu.addAction(run_action)

        # Settings menu
        settings_menu = menu_bar.addMenu("Settings")

        programming_lang_action = QAction("select the programming language", self)
        programming_lang_action.triggered.connect(self.select_programming_lang)
        settings_menu.addAction(programming_lang_action)

        tab_width_action = QAction("Tab Width", self)
        tab_width_action.triggered.connect(self.set_tab_width)
        settings_menu.addAction(tab_width_action)

        theme_action = QAction("Theme", self)
        theme_action.triggered.connect(self.set_theme)
        settings_menu.addAction(theme_action)

        colorize_action = QAction("Keyword Colorize", self)
        colorize_action.triggered.connect(self.set_colorize)
        settings_menu.addAction(colorize_action)

        # ---> Text area
        
        self.text_area = My_Text_Area()  # QPlainTextEdit()
        self.setCentralWidget(self.text_area)
        self.text_area.textChanged.connect(lambda: self.correct())
        self.text_area.setStyleSheet("QPlainTextEdit {background-color: " + self.settings_data["theme"] + ";" + "color: #00FF00; font-family: Courier;}")

        self.highlighter = c_highlighter.C_Highlighter(self.text_area.document())
        
        
        # ---> File Tree View
        
        # ---> Setting Layout

        
    def run(self):
        if os.path.isfile(self.open_file):
            if self.is_change_file:
                if self.question_box():
                    with open("settings.json") as f:
                        json_data = json.loads(f.read())
                    self.lang_running(json_data["default_programming_lang"], self.open_file)
                    #Popen(["gcc", self.open_file])
                else:
                    pass
            else:
                with open("settings.json") as f:
                    json_data = json.loads(f.read())
                    self.lang_running(json_data["default_programming_lang"], self.open_file)
                #Popen(["gcc", self.open_file])
        else:
            running_file = self.save_as()
            if bool(running_file):
                if os.path.isfile(running_file):
                    with open("settings.json") as f:
                        json_data = json.loads(f.read())
                    self.lang_running(json_data["default_programming_lang"], running_file)
                    #Popen(["gcc", running_file])

    def copy(self):
        self.text_area.copy()

    def cut(self):
        self.text_area.cut()

    def paste(self):
        self.text_area.paste()

    def new_file(self):
        if self.is_change_file and os.path.isfile(self.open_file):
            button_reply = QMessageBox.question(self, "Warning",
                                                "You have a unsaved file. Do you want to save changes?",
                                                QMessageBox.Cancel | QMessageBox.No | QMessageBox.Yes | QMessageBox.Cancel)
            if button_reply == QMessageBox.Yes:
                self.save()
                self.open_file = ""
                self.is_change_file = False
                self.setWindowTitle("untitled.c")
            elif button_reply == QMessageBox.No:
                self.open_file = ""
                self.is_change_file = False
                self.text_area.document().setPlainText("")
                self.setWindowTitle("untitled.c")
            elif button_reply == QMessageBox.Cancel:
                pass
        else:
            self.text_area.document().setPlainText("")
            self.open_file = ""
            self.is_change_file = False
            self.setWindowTitle("untitled.c")

    def save(self):
        if os.path.isfile(self.open_file):
            with open(self.open_file, "w") as f:
                f.write(self.text_area.document().toPlainText())
                self.setWindowTitle(self.open_file)
        else:
            QMessageBox.about(self, "Warning", "File didn't open here")

    def save_as(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", ",", "All Files (*)", options=options)

        try:
            with open(file_name, "w") as f:
                f.write(self.text_area.document().toPlainText())
            return file_name
        except FileNotFoundError:
            pass

    def open(self):
        if self.is_change_file and os.path.isfile(self.open_file):
            button_reply = QMessageBox.question(self, "Warning",
                                                "You have a unsaved file. Do you want to save changes?",
                                                QMessageBox.Cancel | QMessageBox.No | QMessageBox.Yes | QMessageBox.Cancel)
            if button_reply == QMessageBox.Yes:
                self.save()

            elif button_reply == QMessageBox.No:
                pass
            elif button_reply == QMessageBox.Cancel:
                return

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)", options=options)
        try:
            with open(file_name, "r") as f:
                self.text_area.document().setPlainText(f.read())
        except UnicodeDecodeError:
            a = FileCannotOpenErrorDialog()
        self.open_file = file_name
        self.setWindowTitle(file_name)

    def question_box(self):
        button_reply = QMessageBox.question(self, "Warning",
                                            "You have a unsaved file.Do you want to  save changes?",
                                            QMessageBox.Yes | QMessageBox.Cancel)
        if button_reply == QMessageBox.Yes:
            self.save()

            self.is_change_file = False
            self.setWindowTitle(self.open_file)
            return True
        if button_reply == QMessageBox.Cancel:
            return False

        #if button_reply == QMessageBox.No:
            #pass

    def go_to_line(self):
        w = QDialog(self)
        row_line = QLineEdit()
        column_line = QLineEdit()
        lab1 = QLabel("raw")
        lab2 = QLabel("column")
        btn = QPushButton("go")
        btn.clicked.connect(partial(self.text_area._go_to_line, row_line, column_line, w))

        main_lay = QVBoxLayout()

        v1 = QHBoxLayout()
        v1.addStretch(1)
        v1.addWidget(lab1)
        v1.addWidget(row_line)

        v2 = QHBoxLayout()
        v2.addStretch(1)
        v2.addWidget(lab2)
        v2.addWidget(column_line)

        main_lay.addStretch(1)
        main_lay.addLayout(v1)
        main_lay.addLayout(v2)
        main_lay.addWidget(btn)

        w.setLayout(main_lay)

        w.exec_()

    def correct(self):

        if os.path.isfile(self.open_file):
            self.is_change_file = True
            self.setWindowTitle("*" + self.open_file)

    
    def select_programming_lang(self):
        a = Lang()

    def set_tab_width(self):
        w = QDialog(self)

        space_data = QLineEdit()
        lab = QLabel("Tab Width")
        save_button = QPushButton("Save")
        cancel_button = QPushButton("Cancel")

        save_button.clicked.connect(partial(self.text_area._set_tab_width, space_data, w))
        cancel_button.clicked.connect(w.destroy)

        main_lay = QVBoxLayout()

        k1 = QHBoxLayout()
        k1.addStretch(1)
        k1.addWidget(lab)
        k1.addWidget(space_data)

        k2 = QHBoxLayout()
        k2.addStretch(1)
        k2.addWidget(save_button)
        k2.addWidget(cancel_button)

        main_lay.addStretch(1)
        main_lay.addLayout(k1)
        main_lay.addLayout(k2)

        w.setLayout(main_lay)

        w.exec_()
        

    def set_theme(self):
        a = Themes(area=self.text_area, parent=None)
        
    def set_colorize(self):
        a = Colorize(highlight=self.highlighter, parent=None)

    def lang_running(self, lang, file_):
        if lang == "python2":
            Popen(["python2", file_])

        elif lang == "python3":
            Popen(["python3", file_])

        elif lang == "java":
            Popen(["java", file_])  #bakilacak

        elif lang == "c":
            Popen(["gcc", file_])


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myapp = Electra()
    myapp.setWindowTitle("Electra")
    myapp.setWindowIcon(QIcon("./res/appicon.png"))
    myapp.resize(600, 600)
    myapp.show()

    sys.exit(app.exec_())
