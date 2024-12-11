import PySimpleGUI as sg
from antlr4 import *
from Python3.PythonLexer import PythonLexer


def apply_syntax_highlighting(text_widget, text):
    # Очистка форматирования
    text_widget.Widget.delete("1.0", sg.tk.END)
    text_widget.Widget.insert(sg.tk.END, text)

    # Создаем лексер ANTLR
    lexer = PythonLexer(InputStream(text))
    token = lexer.nextToken()

    '''
        Красный: 'red'
        Зеленый: 'green'
        Синий: 'blue'
        Желтый: 'yellow'
        Оранжевый: 'orange'
        Фиолетовый: 'purple'
        Коричневый: 'brown'
        Серый: 'gray'
        Черный: 'black'
        Белый: 'white'

        Светло-синий:   '#ADD8E6'
        Светло-зеленый: '#90EE90'
        Светло-желтый:  '#FFFFE0'
        Коралловый:     '#FF7F50'
        Лавандовый:     '#E6E6FA'
        Бирюзовый:      '#40E0D0'
        СэддлБраун:	    '#8B4513'
        Чирок:	        '#008080'
        Темно-оранжевый:'#FF8C00'
        Светло-Морской Зеленый:	'#20B2AA'
    '''
    # Цвета для подсветки
    colors = {
        'NAME'     : '#FF7F50',
        'KEYWORD'  : 'blue',
        'STRING'   : 'brown',
        'NUMBER'   : 'purple',
        'COMMENT'  : 'green',
        'DEFAULT'  : 'black',
        'AWAIT'    :  'blue',
        'ELSE'     : 'blue',
        'IMPORT'   : 'blue',
        'PASS'     : 'blue',
        'BREAK'    : 'blue',
        'EXCEPT'   : 'blue',
        'IN'       : 'blue',
        'RAISE'    : 'blue',
        'CLASS'    : 'blue',
        'FINALLY'  : 'blue',
        'IS'       : 'blue',
        'RETURN'   : 'blue',
        'AND'      : 'blue',
        'CONTINUE' : 'blue',
        'FOR'      : 'blue',
        'LAMBDA'   : 'blue',
        'TRY'      : 'blue',
        'AS'       : 'blue',
        'DEF'      : 'blue',
        'FROM'     : 'blue',
        'NONLOCAL' : 'blue',
        'WHILE'    : 'blue',
        'ASSERT'   : 'blue',
        'DEL'      : 'blue',
        'GLOBAL'   : 'blue',
        'NOT'      : 'blue',
        'WITH'     : 'blue',
        'ASYNC'    : 'blue',
        'ELIF'     : 'blue',
        'IF'       : 'blue',
        'OR'       : 'blue',
        'YIELD'    : 'blue',
    }

    # Проходим по токенам
    while token.type != Token.EOF:
        token_type = lexer.symbolicNames[token.type]
        if token_type in colors:
            # Находим нужный фрагмент текста
            start_line, start_column = token.line, token.column
            end_line = start_line
            end_column = start_column + len(token.text)

            # Формируем строки для Tkinter тегов
            start_tag = f"{start_line}.{start_column}"
            end_tag = f"{end_line}.{end_column}"

            # Добавляем тег и настраиваем форматирование
            text_widget.Widget.tag_add(token_type, start_tag, end_tag)
            text_widget.Widget.tag_configure(token_type, foreground=colors[token_type])

        token = lexer.nextToken()


# Создаем интерфейс
layout = [
    [sg.Text("Введите код Python:")],
    [
        sg.Multiline(
            size=(80, 20),
            key="-TEXT-",
            enable_events=True,
            font=("Courier", 12),
            autoscroll=False,
        )
    ],
    [sg.Button("Подсветить синтаксис")],
]

window = sg.Window("Python Syntax Highlighter", layout, finalize=True)

# Настройка переноса текста для Multiline
text_widget = window["-TEXT-"]
text_widget.Widget.configure(wrap="word")

# Обработка событий
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "-TEXT-":  # Событие изменения текста (включает копирование/вставку)
        text = values["-TEXT-"]
        apply_syntax_highlighting(text_widget, text)
    elif event == "Подсветить синтаксис":  # Явная кнопка для подсветки
        text = values["-TEXT-"]
        apply_syntax_highlighting(text_widget, text)

window.close()
