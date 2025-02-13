import PySimpleGUI as sg
from antlr4 import *
from java.Java20Lexer import Java20Lexer

def apply_syntax_highlighting(text_widget, text):
    # Очистка форматирования
    text_widget.Widget.delete("1.0", sg.tk.END)
    text_widget.Widget.insert(sg.tk.END, text)

    # Создаем лексер ANTLR
    lexer = Java20Lexer(InputStream(text))
    token = lexer.nextToken()

     # Цвета для подсветки
    colors = {
        'EXPORTS':     #Экспортирует пакет с модулем
        'MODULE':
        'OACA':             #'<>'
        'OPEN':
        'OPENS':
        'PERMITS':          #запечатанный класс
        'PROVIDES':
        'RECORD':
        'REQUIRES':             #requires 
        'SEALED':
        'TO':
        'TRANSITIVE':
        'USES':                 #указания зависимости модуля от сервиса.
        'VAR':                  #переменные
        'WITH':
        'YIELD':

        'ABSTRACT':     #модификатор
        'ASSERT':
        'BOOLEAN':      #тип данных
        'BREAK':
        'BYTE':         #тип данных
        'CASE':
        'CATCH':
        'CHAR':         #тип данных
        'CLASS':
        'CONST':        #определяет класс
        'CONTINUE':
        'DEFAULT':
        'DO':
        'DOUBLE':       #тип данных
        'ELSE':
        'ENUM':         #объявляет перечисляемый (неизменяемый) тип
        'EXTENDS':      #расширяет класс (указывает, что класс унаследован от другого класса)
        'FINAL':        #модификатор
        'FINALLY':      #Модификатор 
        'FLOAT':        #тип данных
        'FOR':
        'IF':
        'GOTO':
        'IMPLEMENTS':       #Реализует интерфейс
        'IMPORT':           #Используется для импорта пакета, класса или интерфейса
        'INSTANCEOF':       #Проверяет, является ли объект экземпляром определенного класса или интерфейса
        'INT':              #тип данных
        'INTERFACE':        #Используется для объявления особого типа класса, который содержит только абстрактные методы
        'LONG':             #тип данных
        'NATIVE':           #указывает, что метод не реализован в том же исходном файле Java (но на другом языке)
        'NEW':              #создаёт новые объекты
        'PACKAGE':          #Объявляет пакет
        'PRIVATE':          #модификатор
        'PROTECTED':        #модификатор 
        'PUBLIC':           #модификатор 
        'RETURN':           #модификатор 
        'SHORT':            #тип данных
        'STATIC':           #модификатор 
        'STRICTFP':         #ограничивает точность и округление вычислений с плавающей запятой
        'SUPER':            #относится к объектам суперкласса (родительского)
        'SWITCH':           
        'SYNCHRONIZED':     #модификатор 
        'THIS':             # ссылается на текущий объект в методе или конструкторе
        'THROW':
        'THROWS':
        'TRANSIENT':        ##модификатор
        'TRY':
        'VOID':             #указывает, что метод не должен иметь возвращаемого значения           
        'VOLATILE':         #указывает, что атрибут не кэшируется локально в потоке и всегда читается из «основной памяти». 
        'WHILE':
        'UNDER_SCORE':
        'COMMENT':

        'NullLiteral'

        'LPAREN'     : '(';
        'RPAREN'     : ')';
        'LBRACE'     : '{';
        'RBRACE'     : '}';
        'LBRACK'     : '[';
        'RBRACK'     : ']';
        'SEMI'       : ';';
        'COMMA'      : ',';
        'DOT'        : '.';
        'ELLIPSIS'   : '...';
        'AT'         : '@';
        'COLONCOLON' : '::';
        'ASSIGN'   : '=';
        'GT'       : '>';
        'LT'       : '<';
        'BANG'     : '!';
        'TILDE'    : '~';
        'QUESTION' : '?';
        'COLON'    : ':';
        'ARROW'    : '->';
        'EQUAL'    : '==';
        'LE'       : '<=';
        'GE'       : '>=';
        'NOTEQUAL' : '!=';
        'AND'      : '&&';
        'OR'       : '||';
        'INC'      : '++';
        'DEC'      : '--';
        'ADD'      : '+';
        'SUB      : '-';
        'MUL'      : '*';
        'DIV'      : '/';
        'BITAND'   : '&';
        'BITOR'    : '|';
        'CARET'    : '^';
        'MOD'      : '%';
        'ADD_ASSIGN'     : '+=';
        'SUB_ASSIGN'     : '-=';
        'MUL_ASSIGN'     : '*=';
        'DIV_ASSIGN'     : '/=';
        'AND_ASSIGN'     : '&=';
        'OR_ASSIGN'      : '|=';
        'XOR_ASSIGN'     : '^=';
        'MOD_ASSIGN'     : '%=';
        'LSHIFT_ASSIGN'  : '<<=';
        'RSHIFT_ASSIGN'  : '>>=';
        'URSHIFT_ASSIGN' : '>>>=';

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
    [sg.Text("Введите код на java:")],
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

window = sg.Window("java Syntax Highlighter", layout, finalize=True)

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
