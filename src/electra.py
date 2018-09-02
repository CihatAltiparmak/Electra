# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cihat/Masaüstü/MyProjects/electraYeniden/ui/electra (kopya).ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from text_area import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(864, 659)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        #self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit = My_Text_Area(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(0, 400))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 600))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setStyleSheet("background-color: rgba(34, 15, 15, 209);\n"
"selection-background-color: rgba(70, 105, 147, 204);\n"
"color: rgba(225, 195, 36, 209);\n"
"font: 9pt \"Monospace\";")
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.plainTextEdit.setTabStopWidth(40)
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setMinimumSize(QtCore.QSize(0, 100))
        self.plainTextEdit_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.plainTextEdit_2.setStyleSheet("background-color: rgba(0, 0, 0, 131);\n"
"selection-background-color: rgba(244, 206, 100, 230);\n"
"font: 12pt \"Monospace\";")
        self.plainTextEdit_2.setTabStopWidth(40)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout.addWidget(self.plainTextEdit_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 864, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSelect_all = QtWidgets.QAction(MainWindow)
        self.actionSelect_all.setObjectName("actionSelect_all")
        self.actionJust_compile_but_don_t_run = QtWidgets.QAction(MainWindow)
        self.actionJust_compile_but_don_t_run.setObjectName("actionJust_compile_but_don_t_run")
        self.actionCompile_and_run = QtWidgets.QAction(MainWindow)
        self.actionCompile_and_run.setObjectName("actionCompile_and_run")
        self.actionJust_run = QtWidgets.QAction(MainWindow)
        self.actionJust_run.setObjectName("actionJust_run")
        self.actionAuthor = QtWidgets.QAction(MainWindow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionSelect_all)
        self.menuRun.addAction(self.actionJust_compile_but_don_t_run)
        self.menuRun.addAction(self.actionCompile_and_run)
        self.menuRun.addAction(self.actionJust_run)
        self.menuAbout.addAction(self.actionAuthor)
        self.menuAbout.addAction(self.actionVersion)
        self.menuAbout.addAction(self.actionLicense)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuRun.setTitle(_translate("MainWindow", "run"))
        self.menuAbout.setTitle(_translate("MainWindow", "about"))
        self.actionOpen.setText(_translate("MainWindow", "open"))
        self.actionNew.setText(_translate("MainWindow", "new"))
        self.actionSave.setText(_translate("MainWindow", "save"))
        self.actionSave_as.setText(_translate("MainWindow", "save as"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionSelect_all.setText(_translate("MainWindow", "select all"))
        self.actionJust_compile_but_don_t_run.setText(_translate("MainWindow", "just compile but don\'t run"))
        self.actionCompile_and_run.setText(_translate("MainWindow", "compile and run"))
        self.actionJust_run.setText(_translate("MainWindow", "just run"))
        self.actionAuthor.setText(_translate("MainWindow", "author"))
        self.actionVersion.setText(_translate("MainWindow", "version"))
        self.actionLicense.setText(_translate("MainWindow", "license"))
