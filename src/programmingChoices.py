from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QRadioButton
import json


class Lang(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        with open("settings.json") as f:
            self.json_data = json.loads(f.read()) 
            #self.default_lang = self.json_data["default_programming_lang"]
            self.real_lang = self.json_data["default_programming_lang"]
        self.init_iu()

    def init_iu(self):

        python2_radio = QRadioButton("Python2")
        python3_radio = QRadioButton("Python3")
        java_radio = QRadioButton("Java")
        c_radio = QRadioButton("C lang")
        c_radio.setChecked(True)

        python2_radio.toggled.connect(lambda: self.set_python2())
        python3_radio.toggled.connect(lambda: self.set_python3())
        java_radio.toggled.connect(lambda: self.set_java())
        c_radio.toggled.connect(lambda: self.set_c())

        save_button = QPushButton("Save")
        cancel_button = QPushButton("Cancel")

        save_button.clicked.connect(lambda: self.save_manage(True))
        cancel_button.clicked.connect(lambda: self.save_manage(False))

        v1 = QHBoxLayout()
        v1.addWidget(save_button)
        v1.addWidget(cancel_button)

        main_lay = QVBoxLayout()

        main_lay.addWidget(python2_radio)
        main_lay.addWidget(python3_radio)
        main_lay.addWidget(java_radio)
        main_lay.addWidget(c_radio)

        main_lay.addLayout(v1)

        self.setLayout(main_lay)

        self.exec_()

    def set_python2(self):
        self.real_lang = "python2"

    def set_python3(self):
        self.real_lang = "python3"

    def set_java(self):
        self.real_lang = "java"

    def set_c(self):
        self.real_lang = "c"

    def save_manage(self, option):
        if option: 
            with open("settings.json", "w") as f:
                self.json_data["default_programming_lang"] = self.real_lang               
                f.write(json.dumps(self.json_data))

            self.destroy()

        else: 
            self.destroy()
