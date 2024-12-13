from antlr4 import Lexer
from antlr4.InputStream import InputStream
'''
Этот код представляет собой базовый лексер для языка C#, который использует ANTLR4 для обработки строк с интерполяцией и вербатимных строк. Давайте разберем его функциональность:

Переменные:

interpolatedStringLevel: Уровень вложенности строк с интерполяцией. Каждый раз, когда начинается строка с интерполяцией (например, @$"..."), уровень увеличивается.
interpolatedVerbatiums: Список, используемый как стек для отслеживания, является ли текущая строка вербатимной (т.е., использует ли она символы для экранирования, как @"...").
curlyLevels: Список, который отслеживает уровень вложенности фигурных скобок в строках с интерполяцией.
verbatium: Флаг, указывающий, является ли текущая строка вербатимной.
Методы:

on_interpolated_regular_string_start: Метод вызывается, когда встречается строка с обычной интерполяцией, увеличивает уровень вложенности и добавляет False в список interpolatedVerbatiums (показывает, что это не вербатимная строка).
on_interpolated_verbatium_string_start: Вызывается, когда начинается вербатимная строка с интерполяцией, увеличивает уровень вложенности и добавляет True в список interpolatedVerbatiums.
on_open_brace: Обрабатывает открывающую фигурную скобку { внутри строки с интерполяцией, увеличивает уровень вложенности фигурных скобок.
on_close_brace: Обрабатывает закрывающую фигурную скобку } внутри строки с интерполяцией. Если уровень вложенности фигурных скобок достигает нуля, это означает, что строка с интерполяцией закончена.
on_colon: Обрабатывает двоеточие : в строках с интерполяцией, проверяя, нужно ли переключиться в режим обработки строк с форматированием.
open_brace_inside: Увеличивает уровень вложенности фигурных скобок внутри строки с интерполяцией.
on_double_quote_inside: Обрабатывает закрывающую кавычку внутри строки с интерполяцией, уменьшая уровень вложенности строк с интерполяцией.
on_close_brace_inside: Уменьшает уровень вложенности фигурных скобок.
is_regular_char_inside: Проверяет, является ли текущий символ обычным символом внутри строки, если строка не вербатимная.
is_verbatium_double_quote_inside: Проверяет, является ли текущая строка вербатимной, основываясь на значении флага verbatium.
Этот лексер использует стек для отслеживания уровней вложенности строк с интерполяцией и фигурных скобок, чтобы правильно обрабатывать и различать разные виды строк (обычные и вербатимные) в языке C#.
'''
class CSharpLexerBase(Lexer):
    def __init__(self, input: InputStream, output=None, errorOutput=None):
        super().__init__(input, output, errorOutput)
        self._input = input
        self.interpolatedStringLevel = 0
        self.interpolatedVerbatiums = []  # Используем список как стек
        self.curlyLevels = []  # Используем список как стек
        self.verbatium = False

    def on_interpolated_regular_string_start(self):
        self.interpolatedStringLevel += 1
        self.interpolatedVerbatiums.append(False)
        self.verbatium = False

    def on_interpolated_verbatium_string_start(self):
        self.interpolatedStringLevel += 1
        self.interpolatedVerbatiums.append(True)
        self.verbatium = True

    def on_open_brace(self):
        if self.interpolatedStringLevel > 0:
            if self.curlyLevels:
                self.curlyLevels[-1] += 1
            else:
                self.curlyLevels.append(1)

    def on_close_brace(self):
        if self.interpolatedStringLevel > 0:
            if self.curlyLevels:
                self.curlyLevels[-1] -= 1
                if self.curlyLevels[-1] == 0:
                    self.curlyLevels.pop()
                    self.skip()
                    self.popMode()

    def on_colon(self):
        if self.interpolatedStringLevel > 0:
            ind = 1
            switchToFormatString = True
            while chr(self._input.LA(ind)) != '}':
                if self._input.LA(ind) in (ord(':'), ord(')')):
                    switchToFormatString = False
                    break
                ind += 1

            if switchToFormatString:
                self.mode(self.INTERPOLATION_FORMAT)

    def open_brace_inside(self):
        self.curlyLevels.append(1)

    def on_double_quote_inside(self):
        self.interpolatedStringLevel -= 1
        if self.interpolatedVerbatiums:
            self.interpolatedVerbatiums.pop()
        self.verbatium = self.interpolatedVerbatiums[-1] if self.interpolatedVerbatiums else False

    def on_close_brace_inside(self):
        if self.curlyLevels:
            self.curlyLevels.pop()

    def is_regular_char_inside(self):
        return not self.verbatium

    def is_verbatium_double_quote_inside(self):
        return self.verbatium
