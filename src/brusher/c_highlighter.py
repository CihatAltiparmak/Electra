#!/usr/bin/env python

from PyQt5.QtCore import QFile, QRegExp, Qt
from PyQt5.QtGui import QFont, QSyntaxHighlighter, QTextCharFormat, QColor
from syntaxer import Syntax_Patcher


class C_Highlighter(QSyntaxHighlighter):

    def __init__(self, parent=None):

        super(C_Highlighter, self).__init__(parent)
        self.parent = parent

        parcher = Syntax_Patcher()
        keyword_patterns = parcher.c_parcher()


        # -----------------> data types format

        data_types_patterns = parcher.c_parcher()

        self.data_types_format = QTextCharFormat()
        self.data_types_format.setForeground(self.give_color(data_types_patterns["data_types"]["color"]))    #yellow
        self.data_types_format.setFontWeight(QFont.ExtraBold)

        self.highlight_rules = [(QRegExp(pattern), self.data_types_format) for pattern in data_types_patterns["data_types"]["words"]]
        #print("data_types_uzunlugu: ",len(data_types_patterns["data_types"]["words"]))
        

        # -----------------> function format

        func_format = QTextCharFormat()
        func_format.setForeground(Qt.red)
        func_format.setFontWeight(QFont.Bold)

        self.highlight_rules.append((QRegExp("\\b[A-Za-z0-9_]+(?=\\()"), func_format))

        # -----------------> keyword format

        self.keyword_format = QTextCharFormat()
        self.keyword_format.setForeground(self.give_color(keyword_patterns["keywords"]["color"]))  #white
        self.keyword_format.setFontWeight(QFont.Bold)
        
        for pattern in keyword_patterns["keywords"]["words"]:
            self.highlight_rules.append((QRegExp(pattern), self.keyword_format))
            

        # -----------------> single line comment format

        single_comment_format = QTextCharFormat()
        single_comment_format.setForeground(QColor(0,0,0,100))
        single_comment_format.setFontWeight(QFont.Courier)

        self.highlight_rules.append((QRegExp("//[^\n]*"), single_comment_format))

        # -----------------> multiline comment format

        self.multi_comment_format = QTextCharFormat()
        self.multi_comment_format.setForeground(Qt.cyan)
        self.multi_comment_format.setFontWeight(QFont.Courier)

        # -----------------> single line string format

        str_format = QTextCharFormat()
        str_format.setForeground(Qt.magenta)
        str_format.setFontWeight(QFont.DemiBold)

        self.highlight_rules.append((QRegExp("\".*\""), str_format))
        self.commentStart = QRegExp("/\\*")
        self.commentEnd = QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, format_ in self.highlight_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)

            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format_)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)
        startIndex = 0

        if self.previousBlockState() != 1:
            startIndex = self.commentStart.indexIn(text, startIndex)

        while startIndex >= 0:
            endIndex = self.commentEnd.indexIn(text, startIndex)
            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEnd.matchedLength()
            self.setFormat(startIndex, commentLength, self.multi_comment_format)
            startIndex = self.commentStart.indexIn(text, startIndex + commentLength);


    def give_color(self, color):

        if color == "red":
            return Qt.red 

        if color == "blue":
            return Qt.blue

        if color == "green":
            return Qt.green

        if color == "yellow":
            return Qt.yellow

        if color == "white":
            return Qt.white

        if color == "magenta":
            return Qt.magenta

        if color == "cyan":
            return Qt.cyan

    def _reinit__(self):
        self.__init__(parent = self.parent)

