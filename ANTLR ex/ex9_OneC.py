import PySimpleGUI as sg
from antlr4 import *
from OneC.BSLLexer import BSLLexer

def apply_syntax_highlighting(text_widget, text):
    # Очистка форматирования
    text_widget.Widget.delete("1.0", sg.tk.END)
    text_widget.Widget.insert(sg.tk.END, text)

    # Создаем лексер ANTLR
    lexer = BSLLexer(InputStream(text))
    token = lexer.nextToken()

     # Цвета для подсветки
    colors = {
        'DOT': 'red',
        'LBRACK': 'red',
        'RBRACK': 'red',
        'LPAREN': 'red',
        'RPAREN': 'red',
        'COLON': 'red',
        'SEMICOLON':'red',
        'COMMA': 'red',
        'ASSIGN': 'red',
        'PLUS': 'red',
        'MINUS': 'red',
        'LESS_OR_EQUAL': 'red',
        'NOT_EQUAL': 'red',
        'LESS': 'red',
        'GREATER_OR_EQUAL': 'red',
        'GREATER': 'red',
        'MUL': 'red',
        'QUOTIENT': 'red',
        'MODULO': 'red',
        'QUESTION': 'red',
        'AMPERSAND': 'brown',
        'PREPROC_DELETE' : 'red',
        'PREPROC_INSERT' : 'red',
        'PREPROC_ENDINSERT'  : 'red',
        'TRUE'  : 'red',
        'FALSE'  : 'red',
        'UNDEFINED'  : 'red',
        'NULL'  : 'red',
        'PROCEDURE_KEYWORD': 'red',   
        'FUNCTION_KEYWORD': 'red',
        'ENDPROCEDURE_KEYWORD': 'red',
        'ENDFUNCTION_KEYWORD': 'red',
        'EXPORT_KEYWORD': 'red',
        'VAL_KEYWORD': 'red',
        'ENDIF_KEYWORD': 'red',
        'ENDDO_KEYWORD': 'red',
        'IF_KEYWORD': 'red',
        'ELSIF_KEYWORD': 'red',
        'ELSE_KEYWORD': 'red',
        'THEN_KEYWORD': 'red',
        'WHILE_KEYWORD': 'red',
        'DO_KEYWORD': 'red',
        'FOR_KEYWORD': 'red',
        'TO_KEYWORD': 'red',
        'EACH_KEYWORD': 'red',
        'IN_KEYWORD': 'red',
        'TRY_KEYWORD': 'red',
        'EXCEPT_KEYWORD': 'red',
        'ENDTRY_KEYWORD': 'red',
        'RETURN_KEYWORD': 'red',
        'CONTINUE_KEYWORD': 'red',
        'RAISE_KEYWORD': 'red',
        'VAR_KEYWORD': 'red',
        'NOT_KEYWORD': 'red',
        'OR_KEYWORD': 'red',
        'AND_KEYWORD': 'red',
        'NEW_KEYWORD': 'red',
        'GOTO_KEYWORD': 'red',
        'BREAK_KEYWORD': 'red',
        'EXECUTE_KEYWORD': 'red',
        'ADDHANDLER_KEYWORD': 'red',
        'REMOVEHANDLER_KEYWORD': 'red',
        'ASYNC_KEYWORD': 'red',

        'DECIMAL': '#9400D3',
        'FLOAT': '#9400D3',
        'STRING': 'black',
        'UNKNOWN': '#9400D3',
        'IDENTIFIER': 'blue',
        'LINE_COMMENT': 'green',
        'PREPROC_USE_KEYWORD' : 'brown',
        'PREPROC_REGION': 'brown',
        'PREPROC_END_REGION': 'red',
        'PREPROC_NOT_KEYWORD' : 'red',
        'PREPROC_OR_KEYWORD': 'red',
        'PREPROC_AND_KEYWORD': 'red',
        'PREPROC_IF_KEYWORD': 'red',
        'PREPROC_THEN_KEYWORD': 'red',
        'PREPROC_ELSIF_KEYWORD': 'red',
        'PREPROC_ENDIF_KEYWORD': 'red',
        'PREPROC_ELSE_KEYWORD': 'red',
        'PREPROC_MOBILEAPPCLIENT_SYMBOL': 'brown',
        'PREPROC_MOBILEAPPSERVER_SYMBOL': 'brown',
        'PREPROC_MOBILECLIENT_SYMBOL': 'brown',
        'PREPROC_THICKCLIENTORDINARYAPPLICATION_SYMBOL': 'brown',
        'PREPROC_THICKCLIENTMANAGEDAPPLICATION_SYMBOL': 'brown',
        'PREPROC_EXTERNALCONNECTION_SYMBOL': 'brown',
        'PREPROC_THINCLIENT_SYMBOL': 'brown',
        'PREPROC_WEBCLIENT_SYMBOL': 'brown',
        'PREPROC_ATCLIENT_SYMBOL': 'brown',
        'PREPROC_CLIENT_SYMBOL': 'brown',
        'PREPROC_ATSERVER_SYMBOL': 'brown',
        'PREPROC_SERVER_SYMBOL': 'brown',
        'PREPROC_MOBILE_STANDALONE_SERVER': 'brown',
        'ANNOTATION_ATSERVERNOCONTEXT_SYMBOL': 'brown',
        'ANNOTATION_ATCLIENTATSERVERNOCONTEXT_SYMBOL': 'brown',
        'ANNOTATION_ATCLIENTATSERVER_SYMBOL': 'brown',
        'ANNOTATION_ATCLIENT_SYMBOL': 'brown',
        'ANNOTATION_ATSERVER_SYMBOL': 'brown',
        'ANNOTATION_BEFORE_SYMBOL': 'brown',
        'ANNOTATION_AFTER_SYMBOL': 'brown',
        'ANNOTATION_AROUND_SYMBOL': 'brown',
        'ANNOTATION_CHANGEANDVALIDATE_SYMBOL': 'brown',
        'ANNOTATION_CUSTOM_SYMBOL': 'brown',
        'ANNOTATION_WHITE_SPACE': 'brown',
        'ANNOTATION_UNKNOWN': 'brown',

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
    [sg.Text("Введите код на 1С:")],
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

window = sg.Window("1C Syntax Highlighter", layout, finalize=True)

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
