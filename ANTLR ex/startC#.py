from antlr4 import *
from CShar.CSharpLexer import CSharpLexer
from CShar.CSharpParser import CSharpParser

# Чтение исходного файла C#
input_stream = FileStream("C#Example.cs")
lexer = CSharpLexer(input_stream)
token_stream = CommonTokenStream(lexer)

# Парсинг
parser = CSharpParser(token_stream)
tree = parser.compilation_unit()  # Пример, нужно использовать правильный стартовый узел

# Выводим дерево синтаксического разбора
print(tree.toStringTree(recog=parser))
