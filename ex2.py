import PySimpleGUI as sg
from antlr4 import *
from tkinter import Text
from Python3.PythonLexer import PythonLexer

# Функция подсветки текста
def apply_syntax_highlighting(text_widget, lexer):
    # Удаление всех предыдущих тегов
    for tag in text_widget.tag_names():
        text_widget.tag_delete(tag)

    # Определение стилей
    styles = {
        'keyword': {'foreground': 'blue', 'font': ('Consolas', 10, 'bold')},
        'string': {'foreground': 'green'},
        'comment': {'foreground': 'gray', 'font': ('Consolas', 10, 'italic')},
        'default': {'foreground': 'black'},
    }

    # Добавление тегов для каждого стиля
    for style, config in styles.items():
        text_widget.tag_configure(style, **config)

    # Применение подсветки токенов
    text = text_widget.get("1.0", "end-1c")
    lexer.inputStream = InputStream(text)
    token = lexer.nextToken()
    while token.type != Token.EOF:
        token_type = lexer.symbolicNames[token.type]

        # Назначение стиля токену
        if token_type in ["DEF", "CLASS", "IF", "ELSE", "WHILE"]:  # Ключевые слова Python
            tag = 'keyword'
        elif token_type == "STRING":
            tag = 'string'
        elif token_type == "COMMENT":
            tag = 'comment'
        else:
            tag = 'default'

        # Получаем позиции токена
        start = token.start  # Начальный индекс токена
        stop = token.stop + 1  # Конечный индекс токена
        # Подсветка токена
        #start_index = f"1.0+{token.startIndex}c"
        #end_index = f"1.0+{token.stopIndex + 1}c"
        start_index = f"1.0+{start}c"
        end_index = f"1.0+{stop}c"
        text_widget.tag_add(tag, start_index, end_index)

        token = lexer.nextToken()

# Основное окно
layout = [[sg.Text("Редактор с подсветкой синтаксиса:")],
          [sg.Multiline(size=(80, 20), key='-EDITOR-', font=('Consolas', 10), expand_x=True, expand_y=True)],
          [sg.Button("Подсветить")],
          [sg.Button("Выход")]]

window = sg.Window("Редактор с подсветкой", layout, finalize=True)

# Получение Tkinter-объекта Text
editor_widget = window['-EDITOR-'].Widget

# Подключение лексера ANTLR
lexer = PythonLexer(InputStream(""))

# Основной цикл обработки событий
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Выход":
        break
    if event == "Подсветить":
        apply_syntax_highlighting(editor_widget, lexer)

window.close()
