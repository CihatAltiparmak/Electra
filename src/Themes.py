from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QRadioButton
import json

class Themes(QDialog):

    def __init__(self, area=None, parent=None):
        super().__init__()
        self.area = area
       
        with open("settings.json") as f:           
            self.settings_data = json.loads(f.read())
            self.default_theme = self.settings_data["theme"]

        self.real_theme = None
        self.init_iu()

    def init_iu(self):
        main_lay = QVBoxLayout()

        dark_theme = QRadioButton("dark")
        light_theme = QRadioButton("light")
        default_theme = QRadioButton("default")
        default_theme.setChecked(True)
        dark_theme.toggled.connect(lambda: self.select_theme("dark"))
        light_theme.toggled.connect(lambda: self.select_theme("light"))
        default_theme.toggled.connect(lambda: self.select_theme("default"))        

        save_button = QPushButton("Save")
        cancel_button = QPushButton("Cancel")
        save_button.clicked.connect(lambda: self.save_manage(True))
        cancel_button.clicked.connect(lambda: self.save_manage(False))


        v1 = QVBoxLayout()
        v1.addStretch(1)
        v1.addWidget(default_theme)
        v1.addWidget(dark_theme)
        v1.addWidget(light_theme)

        v2 = QHBoxLayout()
        v2.addStretch(1)
        v2.addWidget(save_button)
        v2.addWidget(cancel_button)
        
        main_lay.addStretch(1)
        main_lay.addLayout(v1)
        main_lay.addLayout(v2)

        self.setLayout(main_lay)

        self.exec_()

    def select_theme(self, which):
        if which == "light":
            self.real_theme = "#9999"
            self.area.setStyleSheet("QPlainTextEdit {background-color: #999; color: #00FF00; font-family: Courier;}")
            
        if which == "default":
            self.real_theme = "#333"
            self.area.setStyleSheet("QPlainTextEdit {background-color: #333; color: #00FF00; font-family: Courier;}")
        
        if which == "dark":
            self.real_theme = "#000"
            self.area.setStyleSheet("QPlainTextEdit {background-color: #000; color: #00FF00; font-family: Courier;}")

    def save_manage(self,option):

        if option:
            with open("settings.json","w") as json_file:
                
                self.settings_data["theme"] = self.real_theme
                json_file.write(json.dumps(self.settings_data))
            self.destroy()
        
        else:
            
            self.area.setStyleSheet("background-color: {};".format(self.default_theme))
            self.destroy()

    
