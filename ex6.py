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
            'number': self.create_format('orange'),
            'variable': self.create_format('purple'),
            'default': self.create_format('black'),
        }

    def create_format(self, color, style=''):
        fmt = QTextCharFormat()
        fmt.setForeground(QColor(color))
        if 'bold' in style:
            fmt.setFontWeight(QFont.Bold)
        if 'italic' in style:
            fmt.setFontItalic(True)
        return fmt

    def highlightBlock(self, text):
        lexer = PythonLexer(InputStream(text))
        token = lexer.nextToken()

        # Ключевые слова Python
        keywords = {"def", "class", "if", "else", "elif", "for", "while", "import", "from", "return", "print"}

        while token.type != Token.EOF:
            token_text = token.text
            start_index = token.start
            length = len(token_text)

            # Подсветка для ключевых слов
            if token_text in keywords:
                self.setFormat(start_index, length, self.styles['keyword'])
            
            # Подсветка для строковых литералов
            elif token.type == PythonLexer.STRING:
                self.setFormat(start_index, length, self.styles['string'])
            
            # Подсветка для комментариев
            elif token.type == PythonLexer.COMMENT:
                self.setFormat(start_index, length, self.styles['comment'])

            # Подсветка для числовых значений
            elif token.type == PythonLexer.NUMBER:
                self.setFormat(start_index, length, self.styles['number'])

            # Подсветка для переменных (идентификаторов)
            elif token.type == PythonLexer.ID:
                if token_text not in keywords:  # Игнорируем ключевые слова
                    self.setFormat(start_index, length, self.styles['variable'])
            
            # Подсветка для прочих токенов (например, операторы, знаки препинания)
            else:
                self.setFormat(start_index, length, self.styles['default'])

            token = lexer.nextToken()
