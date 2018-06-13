from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout



class FileCannotOpenErrorDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_iu()

    def init_iu(self):

        warning_lab = QLabel("This file was opened.Cause of Error: this file is binary file or unknown")
        ok_btn = QPushButton("Ok")
        ok_btn.clicked.connect(lambda: self.destroy())

        main_lay = QVBoxLayout()

        main_lay.addWidget(warning_lab)
        main_lay.addWidget(ok_btn)

        self.setLayout(main_lay)

        self.exec_()
