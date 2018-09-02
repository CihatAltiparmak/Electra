from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from electra import Ui_MainWindow as electraTextEdit
import sys
import c_highlighter

class saveSignal(QObject):
    pass

class runSignal(QObject):
    pass

class newFileOpen(QObject):
    pass

class electraMyEditor(QMainWindow):

    new_file_lock = False
    def __init__(self):
        super().__init__()
        self.ui = electraTextEdit()
        self.ui.setupUi(self)
        # ----> connect funcs to actions
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionNew.triggered.connect(self.create_new_file)
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionSave_as.triggered.connect(self.save_as)
        self.ui.actionCopy.triggered.connect(self.copyClipboard)
        self.ui.actionCut.triggered.connect(self.cutClipboard)
        self.ui.actionPaste.triggered.connect(self.pasteClipboard)
        self.ui.actionSelect_all.triggered.connect(self.selectAllClipboard)
        self.ui.actionJust_compile_but_don_t_run.triggered.connect(self.run)
        self.ui.actionJust_run.triggered.connect(self.run)
        self.ui.actionJust_compile_but_don_t_run.triggered.connect(self.run)
        self.ui.actionJust_run.triggered.connect(self.run)
        
        self.highlighter = c_highlighter.C_Highlighter(self.ui.plainTextEdit.document())

    def open_file(self):
        pass
    
    def create_new_file(self):
        pass

    def save(self):
        pass

    def save_as(self):
        pass

    def control(self):
        pass

    def copyClipboard(self):
        pass

    def pasteClipboard(self):
        pass

    def cutClipboard(self):
        pass

    def selectAllClipboard(self):
        pass

    def run(self):
        pass

app = QApplication([])
win = electraMyEditor()
win.show()
sys.exit(app.exec_())
