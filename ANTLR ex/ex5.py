from antlr4 import *
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt5.QtCore import Qt
from Python3.PythonLexer import PythonLexer

class PythonSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.styles = {
            'keyword': self.create_format('blue', 'bold'),
            'string': self.create_format('green'),
            'comment': self.create_format('gray', 'italic'),
            'default': self.create_format('black'),
        }

    def create_format(self, color, style=''):
        fmt = QTextCharFormat()
        fmt.setForeground(QColor(color))
        if 'bold' in style:
            fmt.setFontWeight(QFont.Bold)  # Исправлено
        if 'italic' in style:
            fmt.setFontItalic(True)
        return fmt

    def highlightBlock(self, text):
        lexer = PythonLexer(InputStream(text))
        token = lexer.nextToken()
        keywords = {"def", "class", "if", "else", "elif", "for", "while", "import", "from", "return", "print"}  # Ключевые слова Python

        while token.type != Token.EOF:
            token_text = token.text
            start_index = token.start
            length = len(token_text)

            if token_text in keywords:  # Проверяем, является ли токен ключевым словом
                self.setFormat(start_index, length, self.styles['keyword'])
            elif token.type == PythonLexer.STRING:
                self.setFormat(start_index, length, self.styles['string'])
            elif token.type == PythonLexer.COMMENT:
                self.setFormat(start_index, length, self.styles['comment'])
            else:
                self.setFormat(start_index, length, self.styles['default'])

            token = lexer.nextToken()
