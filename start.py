import sys
from antlr4 import *
from Python3.PythonLexer import PythonLexer
from Python3.PythonParser import PythonParser

# Задайте путь к файлу Python, который хотите распарсить
input_file = "example.py"

# Чтение файла
input_stream = FileStream(input_file, encoding='utf-8')

# Лексический анализ
lexer = PythonLexer(input_stream)
token_stream = CommonTokenStream(lexer)

# Синтаксический анализ
parser = PythonParser(token_stream)
tree = parser.file_input()  # Для файла Python

# Печать дерева (в отладочных целях)
print(tree.toStringTree(recog=parser))
