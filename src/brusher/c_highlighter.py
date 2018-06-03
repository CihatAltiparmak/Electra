#!/usr/bin/env python

from PyQt5.QtCore import QFile, QRegExp, Qt
from PyQt5.QtGui import QFont, QSyntaxHighlighter, QTextCharFormat
from syntaxer import Syntax_Patcher


class C_Highlighter(QSyntaxHighlighter):

    def __init__(self, parent=None):

        super(C_Highlighter, self).__init__(parent)

        # -----------------> keyword format

        keyword_format = QTextCharFormat()
        keyword_format.setForeground(Qt.darkBlue)
        keyword_format.setFontWeight(QFont.Bold)
        parcher = Syntax_Patcher()
        keyword_patterns = parcher.c_parcher()["keywords"]

        self.highlight_rules = [(QRegExp(pattern), keyword_format) for pattern in keyword_patterns]

        # -----------------> data types format

        data_types_format = QTextCharFormat()
        data_types_format.setForeground(Qt.yellow)
        data_types_format.setFontWeight(QFont.ExtraBold)

        data_types_patterns = parcher.c_parcher()["data_types"]

        for pattern in data_types_patterns:
            self.highlight_rules.append((QRegExp(pattern), data_types_format))

        # -----------------> function format

        func_format = QTextCharFormat()
        func_format.setForeground(Qt.red)
        func_format.setFontWeight(QFont.Bold)

        self.highlight_rules.append((QRegExp("\\b[A-Za-z0-9_]+(?=\\()"), func_format))

        # -----------------> single line comment format

        single_comment_format = QTextCharFormat()
        single_comment_format.setForeground(Qt.green)
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
