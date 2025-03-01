from antlr4 import *
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt5.QtCore import Qt
from Python3.PythonLexer import PythonLexer

# Класс PythonSyntaxHighlighter отвечает за подсветку синтаксиса для Python-кода
class PythonSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        """
        Инициализация объекта подсветки синтаксиса для документа.
        
        Этот метод создает словарь стилей для различных типов синтаксиса (ключевые слова, строки, комментарии и т.д.)
        и вызывает инициализацию родительского класса QSyntaxHighlighter.

        :param document: QTextDocument, документ, в котором будет применяться подсветка
        """
        super().__init__(document)
        self.styles = {
            'keyword': self.create_format('blue', 'bold'),      # Синий цвет и полужирное начертание для ключевых слов
            'string': self.create_format('green'),              # Зеленый цвет для строковых литералов
            'comment': self.create_format('gray', 'italic'),    # Серый цвет и курсив для комментариев
            'number': self.create_format('orange'),             # Оранжевый цвет для числовых значений
            'variable': self.create_format('purple'),           # Фиолетовый цвет для переменных
            'default': self.create_format('black'),             # Черный цвет по умолчанию для остальных токенов
        }

    def create_format(self, color, style=''):
        """
        Создает формат для подсветки текста в зависимости от заданных стилей.

        :param color: Цвет текста (например, 'blue', 'green' и т.д.)
        :param style: Стиль текста (например, 'bold' или 'italic')
        :return: QTextCharFormat объект, который хранит информацию о формате текста
        """
        fmt = QTextCharFormat()
        fmt.setForeground(QColor(color))                                    # Устанавливаем цвет текста
        if 'bold' in style:
            fmt.setFontWeight(QFont.Bold)                                   # Если задан стиль 'bold', делаем текст полужирным
        if 'italic' in style:
            fmt.setFontItalic(True)                                         # Если задан стиль 'italic', делаем текст курсивом
        return fmt

    def highlightBlock(self, text):
        """
        Метод, который вызывается для каждого блока текста в документе.
        Этот метод анализирует текст с помощью лексера PythonLexer и применяет соответствующий стиль
        в зависимости от типа токена (ключевое слово, строка, комментарий и т.д.).

        :param text: Строка текста, которую нужно подсветить
        """
        lexer = PythonLexer(InputStream(text))          # Инициализируем лексер для анализа текста
        token = lexer.nextToken()                       # Получаем первый токен

        # Ключевые слова Python
        keywords = {'False', 'None', 'True', 'and', 'as', 'assert', 'async', "await", 
                    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
                    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
                    'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'}

        while token.type != Token.EOF:                  # Пока не достигнут конец текста
            token_text = token.text                     # Текст текущего токена
            start_index = token.start                   # Начальная позиция токена
            length = len(token_text)                    # Длина токена

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
            elif token.type == PythonLexer.NAME:  # Используйте NAME для идентификаторов
                if token_text not in keywords:  # Игнорируем ключевые слова
                    self.setFormat(start_index, length, self.styles['variable'])
            
            # Подсветка для прочих токенов (например, операторы, знаки препинания)
            else:
                self.setFormat(start_index, length, self.styles['default'])

            token = lexer.nextToken()  # Переходим к следующему токену
