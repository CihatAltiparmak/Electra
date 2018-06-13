from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QComboBox
from syntaxer import Syntax_Patcher
import json

class Colorize(QDialog):

    def  __init__(self, highlight=None, parent=None):
        super().__init__()
        self.highlight = highlight    
        
        self.json_data = Syntax_Patcher.c_parcher()
        self.data_real = self.json_data["data_types"]["color"]
        self.keyword_real = self.json_data["keywords"]["color"]
        self.data_default = self.json_data["data_types"]["color"] 
        self.keyword_default = self.json_data["keywords"]["color"]
        self.init_iu()

    def init_iu(self):

        w = QDialog()

        main_lay = QVBoxLayout()

        data_types_lab = QLabel("Data Type Color")
        keywords_lab = QLabel("Keywords Color")

        data_types_combo = QComboBox(self)
        data_types_combo.addItem("red")
        data_types_combo.addItem("blue")
        data_types_combo.addItem("green")
        data_types_combo.addItem("yellow")
        data_types_combo.addItem("white")
        data_types_combo.addItem("magenta")
        data_types_combo.addItem("cyan")
        data_types_combo.activated[str].connect(self.setDataTypesColor)        

        keywords_combo = QComboBox(self)
        keywords_combo.addItem("red")
        keywords_combo.addItem("blue")
        keywords_combo.addItem("green")
        keywords_combo.addItem("yellow")
        keywords_combo.addItem("white")
        keywords_combo.addItem("magenta")
        keywords_combo.addItem("cyan")
        keywords_combo.activated[str].connect(self.setKeywordsColor)
        
        save_button = QPushButton("Save")       
        cancel_button = QPushButton("Cancel")

        save_button.clicked.connect(lambda: self.save_manage(True)) 
        cancel_button.clicked.connect(lambda: self.save_manage(False))

        v1 = QHBoxLayout()
        v1.addStretch(1)
        v1.addWidget(data_types_lab)
        v1.addWidget(data_types_combo)

        v2 = QHBoxLayout()
        v2.addStretch(1)
        v2.addWidget(keywords_lab)
        v2.addWidget(keywords_combo)

        v3 = QHBoxLayout()
        v3.addStretch(1)
        v3.addWidget(save_button)
        v3.addWidget(cancel_button)

        main_lay.addStretch(1)
        main_lay.addLayout(v1)
        main_lay.addLayout(v2)
        main_lay.addLayout(v3)
        
        self.setLayout(main_lay)
        self.exec_() 

    def save_manage(self, option):
        if option:
            self.json_data["data_types"]["color"] = self.data_real
            self.highlight.data_types_format.setForeground(self.highlight.give_color(self.data_real))

            self.json_data["keywords"]["color"] = self.keyword_real
            self.highlight.keyword_format.setForeground(self.highlight.give_color(self.keyword_real))
            with open("./syntax_definitions/c_keywords.json","w") as f:
                f.write(json.dumps(self.json_data))   
            self.highlight._reinit__()
            self.destroy() 

        else:
            self.json_data["data_types"]["color"] = self.data_default
            self.highlight.data_types_format.setForeground(self.highlight.give_color(self.data_default))

            self.json_data["keywords"]["color"] = self.keyword_default
            self.highlight.keyword_format.setForeground(self.highlight.give_color(self.keyword_default))
            self.destroy() 


    def setDataTypesColor(self, text):
        self.data_real = text
        self.highlight.data_types_format.setForeground(self.highlight.give_color(text))
        

    def setKeywordsColor(self, text):
        self.keyword_real = text
        self.highlight.keyword_format.setForeground(self.highlight.give_color(text))
        





 

