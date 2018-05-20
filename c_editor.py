# -*- coding: utf-8 -*-
# !/usr/bin/env python

#######################################            ###    ####
#                                     #            #  #   #   #
#  coded by      => Cihat Altiparmak  #            #  #   #   #
#  creating_date => 19.05.2018        #            ####   #   #    
#  creating_time => 00.29             #            #  #   #   #
#  thank_to      => BDFrostbide       #            #  #   #   #
#                                     #            #  #   #   #
#######################################            ###    ####
"""
author's message:

BU Basit C EDITOR'u bilgisayarı programlamaya uygun olmayan herkes icindir.
Zaman oldukca gelistirilecektir.
Gule gule kullanın:)
"""

import tkinter as tk
from functools import partial
from tkinter import *
import os
from tkinter import filedialog, messagebox

from subprocess import PIPE, Popen, call, check_output
import sys


class operate():
    def __init__(self):
        self.is_file_open = False
        self.is_new_file = True

    def exit_(self):
        if self.is_file_open:
            with open(self.file_.name, "r") as f:
                file_content = f.read()
            print(text_area.get(1.0, END))
            if file_content == text_area.get(1.0, END):
                pcr.destroy()
            else:
                response = messagebox.askquestion("uyari",
                                                  "dosyanizda birtakim degisiklikler yapıldı.Kaydetmek istiyor musunuz?")
                print(response)
                if response == "yes":
                    self.save()
                    pcr.destroy()
                else:
                    pcr.destroy()
        else:
            pcr.destroy()

    def new_file(self):
        if self.is_file_open:
            with open(self.file_.name, "r") as f:
                file_content = f.read()
            print(text_area.get(1.0, END))
            if file_content == text_area.get(1.0, END):
                text_area.delete(1.0, END)
                self.file_ = ""
            else:
                response = messagebox.askquestion("uyari",
                                                  "Acılmıs bir dosyaniz var ve dosyanizda birtakim degisiklikler yapıldı.Kaydetmek istiyor musunuz?")
                print(response)
                if response == "yes":
                    self.save()
                    text_area.delete(1.0, END)
                    self.file_ = ""
                else:
                    text_area.delete(1.0, END)
                    self.file_ = ""
        else:
            text_area.delete(1.0, END)
            self.file_ = ""

    def save_as(self):
        try:
            file_ = filedialog.asksaveasfile()
            with file_ as f:
                f.write(text_area.get(1.0, END))
                self.is_file_open = True
                self.file_ = file_
        except:
            pass

    def save(self):
        try:
            with open(self.file_.name, "w") as f:
                f.write(text_area.get(1.0, END))
        except:
            if self.is_new_file:
                self.save_as()
            else:
                messagebox.showwarning("uyari", "herhangi bir dosya acilmamis.")

    def open(self):
        try:
            self.file_ = filedialog.askopenfile()
            with self.file_ as f:
                file_ = self.file_

                text_area.delete(1.0, END)
                text_area.insert(1.0, file_.read())
                self.is_file_open = True
        except:
            pass

    def run(self):
        if self.is_file_open:
            self.save()

            a = Popen(["gcc", self.file_.name], stdout=PIPE)

        else:
            self.save_as()
            directory, file_name = os.path.split(self.file_.name)
            a = Popen(["gcc", self.file_.name], stdout=PIPE)

    def copy(self):
        text_area.event_generate("<<Copy>>")

    def cut(self):
        text_area.event_generate("<<Cut>>")

    def paste(self):
        text_area.event_generate("<<Paste>>")

    def go_to_line(self):
        location_window = Tk()
        self.entry1 = Entry(location_window)
        self.entry2 = Entry(location_window)
        lab1 = Label(location_window, text="1.etiket")
        lab2 = Label(location_window, text="2.etiket")
        btn = Button(location_window, text="go", command=partial(self._go_to_line, location_window))
        self.entry1.grid(row=0, column=0)
        lab1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=0)
        lab2.grid(row=1, column=1)
        btn.grid(row=2, column=0)

    def _go_to_line(self, drame):
        row = self.entry1.get()
        column = self.entry2.get()

        text_area.mark_set(INSERT, row + "." + column)
        text_area.focus_set()
        drame.destroy()

opr = operate()

pcr = Tk()
pcr.protocol("WM_DELETE_WINDOW", opr.exit_)
pcr.title = "C IDLE 0.0.1"

menu_bar = Menu(pcr)
pcr.config(menu=menu_bar)

file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="file", menu=file_menu)
# -------------------------------------------------------------
file_menu.add_command(label="new file", command=opr.new_file)
file_menu.add_command(label="save", command=opr.save)
file_menu.add_command(label="save as", command=partial(opr.save_as))
file_menu.add_command(label="open", command=partial(opr.open))
file_menu.add_command(label="go to line", command=opr.go_to_line)
# -------------------------------------------------------------
edit_menu = Menu(menu_bar)
menu_bar.add_cascade(label="edit", menu=edit_menu)
edit_menu.add_command(label="copy", command=opr.copy)
edit_menu.add_command(label="cut", command=opr.cut)
edit_menu.add_command(label="paste", command=opr.paste)
# ----------------------------------------------------------------
run_menu = Menu(menu_bar)
menu_bar.add_cascade(label="run", menu=run_menu)
run_menu.add_command(label="run", command=opr.run)
# --------------------------------------------------------------
text_area = Text(pcr)
txt = Scrollbar(text_area)

text_area.grid(sticky=N + E + S + W)

pcr.grid_rowconfigure(0, weight=1)
pcr.grid_columnconfigure(0, weight=1)

pcr.mainloop()
