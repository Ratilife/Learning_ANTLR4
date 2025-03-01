import PySimpleGUI as sg
from antlr4 import *
from Python3.PythonLexer import PythonLexer
from CSharNew.CSharpLexer import CSharpLexer



def apply_syntax_highlighting_PY(text_widget, text):
    # Очистка форматирования
    text_widget.Widget.delete("1.0", sg.tk.END)
    text_widget.Widget.insert(sg.tk.END, text)

    # Создаем лексер ANTLR
    lexer = PythonLexer(InputStream(text))
    token = lexer.nextToken()
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

def apply_syntax_highlighting_CShar(text_widget, text):
    # Очистка форматирования
    text_widget.Widget.delete("1.0", sg.tk.END)
    text_widget.Widget.insert(sg.tk.END, text)

    # Создаем лексер ANTLR
    lexer = CSharpLexer(InputStream(text))
    token = lexer.nextToken()

    
    # Цвета для подсветки
    colors = {
                'SINGLE_LINE_DOC_COMMENT'     : 'green',   
                'EMPTY_DELIMITED_DOC_COMMENT' :  '#006400',
                'DELIMITED_DOC_COMMENT'       : '#006400', 
                'SINGLE_LINE_COMMENT'         : '#006400',
                'DELIMITED_COMMENT'           : '#006400', 
                'SHARP'                       : 'orange',                    

                'ABSTRACT'   : '#00008B',                #Объявление классов и интерфейсов
                'ADD'        : '#8B0000',                #Управляющие конструкции
                'ALIAS'      : '#8B0000',                #Другие ключевые слова
                'ARGLIST'    : 'blue',                   #Объявление переменных
                'AS'         : '#8B0000',                #Операторы и выражения
                'ASCENDING'  : 'blue',                   #Объявление переменных
                'ASYNC'      : '#DC143C',                #Асинхронность
                'AWAIT'      : '#DC143C',                #Асинхронность
                'BASE'       : '#00008B',                #Объявление классов и интерфейсов
                'BOOL'       : 'purple',                 #Типы данных
                'BREAK'      : '#8B0000',                #Управление потоком выполнения
                'BY'         : '#C0C0C0',                #Управление данными и выборка
                'BYTE'       : 'purple',                 #Типы данных
                'CASE'       : '#8B0000',                #Условные конструкции
                'CATCH'      : '#8B0000',                #Управляющие конструкции
                'CHAR'       : 'purple',                 #Типы данных
                'CHECKED'    : '#8B0000',                # Другие ключевые слова
                'CLASS'      : '#00008B',                #Объявление классов и интерфейсов
                'CONST'      : 'blue',                   # Другие ключевые слова
                'CONTINUE'   : '#8B0000',                #Управление потоком выполнения
                'DECIMAL'    : 'purple',                 #Типы данных
                'DEFAULT'    : '#8B0000',                #Условные конструкции
                'DELEGATE'   : '#FFDB58',                #Делегаты и события               
                'DESCENDING' : 'blue',                   #Объявление переменных
                'DO'         : '#8B0000',                #Циклы
                'DOUBLE'     : 'purple',                 #Типы данных
                'DYNAMIC'    : 'purple',                 #Типы данных
                'ELSE'       : '#8B0000',                #Условные конструкции
                'ENUM'       : '#00008B',                #Объявление классов и интерфейсов
                'EQUALS'     : '#8B0000',                #Операторы и выражения
                'EVENT'      : '#FFDB58',                #Делегаты и события
                'EXPLICIT'   : 'explicit',               #Преобразования типов
                'EXTERN'     : 'blue',                   #Объявление переменных
                'FALSE'      : '#FF8C00',                #Объявление типов
                'FINALLY'    : '#8B0000',                #Управляющие конструкции
                'FIXED'      : 'blue',                   #Объявление переменных
                'FLOAT'      : 'purple',                 #Типы данных
                'FOR'        : '#8B0000',                #Циклы
                'FOREACH'    : '#8B0000',                #Циклы
                'FROM'       : '#C0C0C0',                #Управление данными и выборка
                'GET'        : 'blue',                   #Объявление переменных
                'GOTO'       : '#8B0000',                #Управляющие конструкции
                'GROUP'      : '#C0C0C0',                #Управление данными и выборка
                'IF'         : '#8B0000',                #Условные конструкции
                'IMPLICIT'   : 'implicit',               #Преобразования типов
                'IN'         : '#8B0000',                #Операторы и выражения
                'INT'        : 'purple',                 #Типы данных
                'INTERFACE'  : '#00008B',                #Объявление классов и интерфейсов
                'INTERNAL'   : '#FF8C00',                #Модификаторы доступа
                'INTO'       : '#C0C0C0',                #Управление данными и выборка
                'IS'         :'#8B0000',                 #Операторы и выражения
                'JOIN'       : '#C0C0C0',                #Управление данными и выборка
                'LET'        : '#C0C0C0',                #Управление данными и выборка
                'LOCK'       : '#8B0000',                #Управляющие конструкции
                'LONG'       : 'purple',                 #Типы данных
                'NAMEOF'     : 'blue',                   #Объявление переменных
                'NAMESPACE'  : 'blue',                   #Объявление переменных
                'NEW'        : 'blue',                   #Объявление переменных
                'NULL_'      : '#FF8C00',                #Объявление типов
                'OBJECT'     : 'purple',                 #Типы данных
                'ON'         : '#8B0000',                #Операторы и выражения
                'OPERATOR'   : '#00008B',                #Объявление классов и интерфейсов
                'ORDERBY'    : '#C0C0C0',                #Управление данными и выборка
                'OUT'        : '#8B0000',                #Управление потоком выполнения
                'OVERRIDE'   : '#00008B',                #Объявление классов и интерфейсов
                'PARAMS'     : 'params',                 #Управление доступом и структурирование кода
                'PARTIAL'    : '#00008B',                #Объявление классов и интерфейсов
                'PRIVATE'    : '#FF8C00',                #Модификаторы доступа
                'PROTECTED'  : '#FF8C00',                #Модификаторы доступа
                'PUBLIC'     : '#FF8C00',                #Модификаторы доступа
                'READONLY'   : '#8B0000',                # Другие ключевые слова
                'REF'        : '#8B0000',                #Управление потоком выполнения
                'REMOVE'     : '#8B0000',                #Управление потоком выполнения
                'RETURN'     : '#8B0000',                #Управление потоком выполнения
                'SBYTE'      : 'purple',                 #Типы данных
                'SEALED'     : '#00008B',                #Объявление классов и интерфейсов
                'SELECT'     : '#C0C0C0',                #Управление данными и выборка
                'SET'        : 'blue',                   #Объявление переменных
                'SHORT'      : 'purple',                 #Типы данных
                'SIZEOF'     : '#8B0000',                #Управление потоком выполнения
                'STACKALLOC' : '#8B0000',                #Управление потоком выполнения
                'STATIC'     : '#00008B',                #Объявление классов и интерфейсов
                'STRING'     : 'purple',                 #Типы данных
                'STRUCT'     : '#00008B',                #Объявление классов и интерфейсов
                'SWITCH'     : '#8B0000',                #Условные конструкции
                'THIS'       : '#00008B',                #Объявление классов и интерфейсов
                'THROW'      : '#8B0000',                #Управляющие конструкции
                'TRUE'       : '#FF8C00',                #Объявление типов
                'TRY'        : '#8B0000',                #Управляющие конструкции
                'TYPEOF'     : 'blue',                   #Объявление переменных
                'UINT'       : 'purple',                 #Типы данных
                'ULONG'      : 'purple',                 #Типы данных
                'UNCHECKED'  : 'blue',                   #Объявление переменных
                'UNMANAGED'  : 'blue',                   #Объявление переменных
                'UNSAFE'     : 'blue',                   #Объявление переменных
                'USHORT'     : 'purple',                 #Типы данных
                'USING'      : 'blue',                   #Объявление переменных
                'VAR'        : 'blue',                   #Объявление переменных
                'VIRTUAL'    : '#00008B',                #Объявление классов и интерфейсов
                'VOID'       : '#00008B',                #Объявление классов и интерфейсов
                'VOLATILE'   : '#8B0000',                # Другие ключевые слова
                'WHEN'       : '#8B0000',                #Условные конструкции
                'WHERE'      : '#C0C0C0',                #Управление данными и выборка
                'WHILE'      : '#8B0000',                #Циклы
                'YIELD'      : '#8B0000',                # Другие ключевые слова
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

textPy = "Введите код Python:"
textCharp = "Введите код C#:"
# Radio кнопки создаются внутри Frame
radio_frame = sg.Frame(layout=[
    [sg.Radio('Python', "RADIO1", key="RADIO_PY", default=True, size=(10, 1)),
     sg.Radio('C#', "RADIO1", key="RADIO_CSHARP")]  # Добавляем ключи
],
    title='Языки', title_color='blue',)
 
layout = [
    [sg.Text(textPy, key="-TEXT_LABEL-")],  # Изначально отображаем текст для Python
    [radio_frame],
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


window = sg.Window("Python/С# Syntax Highlighter", layout, finalize=True)

# Настройка переноса текста для Multiline
text_widget = window["-TEXT-"]
text_widget.Widget.configure(wrap="word")

# Функция для выбора языка и обновления текста
def update_language(window, values):
    if values["RADIO_PY"]:  # Используем ключ Python Radio
        window["-TEXT_LABEL-"].update(textPy)
        return "Python"
    else:  # Используем ключ C# Radio
        window["-TEXT_LABEL-"].update(textCharp)
        return "C#"


# Обработка событий
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    selected_language = update_language(window, values)  # Обновляем язык
    if event == "-TEXT-":  # Событие изменения текста (включает копирование/вставку)
        text = values["-TEXT-"]
        # Убираем вызов подсветки здесь, чтобы избежать проблем с вставкой
        continue
        
    elif event == "Подсветить синтаксис":  # Явная кнопка для подсветки
        text = values["-TEXT-"]
        
        
        # Выбор функции подсветки в зависимости от языка
        if selected_language == "Python":
            apply_syntax_highlighting_PY(text_widget, text)
        else:
            apply_syntax_highlighting_CShar(text_widget, text)
    '''
    # Обновление текста в зависимости от выбранного языка
    if event in ("RADIO1", "RADIO2"):  # Проверяем, изменился ли выбор языка
        if window["RADIO1"].get():  # Если выбран Python
            window["-TEXT-"].update("")  # Очищаем текстовое поле
            window["-TEXT-"].Widget.configure(wrap="word")  # Настройка переноса текста
            window["-TEXT-"].update(textPy)  # Обновляем текст
        else:  # Если выбран C#
            window["-TEXT-"].update("")  # Очищаем текстовое поле
            window["-TEXT-"].Widget.configure(wrap="word")  # Настройка переноса текста
            window["-TEXT-"].update(textCharp)  # Обновляем текст
    '''        
window.close()