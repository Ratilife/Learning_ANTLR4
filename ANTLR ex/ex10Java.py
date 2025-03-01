import PySimpleGUI as sg
from antlr4 import *
from Java.Java20Lexer import Java20Lexer

def apply_syntax_highlighting(text_widget, text):
    # Очистка форматирования
    text_widget.Widget.delete("1.0", sg.tk.END)
    text_widget.Widget.insert(sg.tk.END, text)

    # Создаем лексер ANTLR
    lexer = Java20Lexer(InputStream(text))
    token = lexer.nextToken()

     # Цвета для подсветки
    colors = {
    # Модификаторы и ключевые слова управления пакетами/модулями
    'EXPORTS'     : '#8B4513',  # Brown (кирпичный, указывает на "открытость")
    'MODULE'      : '#8B4513',
    'OACA'        : '#2F4F4F',  # DarkSlateGray (для угловых скобок, как обрамление)
    'OPEN'        : '#8B4513',
    'OPENS'       : '#8B4513',
    'PERMITS'     : '#8B4513',
    'PROVIDES'    : '#8B4513',
    'REQUIRES'    : '#8B4513',
    'SEALED'      : '#8B4513',
    'TO'          : '#8B4513',
    'TRANSITIVE'  : '#8B4513',
    'USES'        : '#8B4513',
    'WITH'        : '#8B4513',
    'YIELD'       : '#8B4513',
    'PACKAGE'     : '#8B4513',

    # Ключевые слова управления потоком выполнения
    'ASSERT'      : '#005580',  # MediumBlue (для утверждений)
    'BREAK'       : '#005580',
    'CASE'        : '#005580',
    'CATCH'       : '#005580',
    'CONTINUE'    : '#005580',
    'DEFAULT'     : '#005580',
    'DO'          : '#005580',
    'ELSE'        : '#005580',
    'FOR'         : '#005580',
    'IF'          : '#005580',
    'GOTO'        : '#005580',
    'INSTANCEOF'  : '#005580',
    'RETURN'      : '#005580',
    'SWITCH'      : '#005580',
    'THROW'       : '#005580',
    'THROWS'      : '#005580',
    'TRY'         : '#005580',
    'WHILE'       : '#005580',

    # Типы данных
    'BOOLEAN'     : '#008000',  # Green (для логических типов)
    'BYTE'        : '#008000',
    'CHAR'        : '#008000',
    'DOUBLE'      : '#008000',
    'FLOAT'       : '#008000',
    'INT'         : '#008000',
    'LONG'        : '#008000',
    'SHORT'       : '#008000',
    'VOID'        : '#008000',

    # Объявление классов, интерфейсов, перечислений
    'CLASS'       : '#B8860B',  # DarkGoldenRod (для классов и интерфейсов)
    'ENUM'        : '#B8860B',
    'INTERFACE'   : '#B8860B',
    'RECORD'      : '#B8860B',  # Считаем Record похожим на класс

    # Модификаторы доступа и другие ключевые слова
    'ABSTRACT'    : '#A0522D',  # Sienna (для абстрактных элементов)
    'FINAL'       : '#A0522D',
    'NATIVE'      : '#A0522D',
    'PRIVATE'     : '#A0522D',
    'PROTECTED'   : '#A0522D',
    'PUBLIC'      : '#A0522D',
    'STATIC'      : '#A0522D',
    'STRICTFP'    : '#A0522D',
    'SYNCHRONIZED': '#A0522D',
    'TRANSIENT'   : '#A0522D',
    'VOLATILE'    : '#A0522D',
    'CONST'       : '#A0522D',
    'EXTENDS'     : '#A0522D',
    'IMPLEMENTS'  : '#A0522D',

    # Работа с памятью и объектами
    'NEW'         : '#800080',  # Purple (для создания объектов)
    'THIS'        : '#800080',
    'SUPER'       : '#800080',

    # Литералы
    'NullLiteral'    : '#4682B4',  # SteelBlue (для null)
    'BooleanLiteral' : '#4682B4',  # SteelBlue (для true/false)
    'IntegerLiteral' : '#4682B4', # IntegerLiteral
    'FloatingPointLiteral' : '#4682B4', # FloatingPointLiteral
    'CharacterLiteral' : '#4682B4', # CharacterLiteral
    'StringLiteral': '#4682B4', # StringLiteral
    'TextBlock': '#4682B4', #TextBlock

    # Разделители
    'LPAREN'     : '#2F4F4F', # DarkSlateGray (скобки и знаки препинания)
    'RPAREN'     : '#2F4F4F',
    'LBRACE'     : '#2F4F4F',
    'RBRACE'     : '#2F4F4F',
    'LBRACK'     : '#2F4F4F',
    'RBRACK'     : '#2F4F4F',
    'SEMI'       : '#2F4F4F',
    'COMMA'      : '#2F4F4F',
    'DOT'        : '#2F4F4F',
    'ELLIPSIS'   : '#2F4F4F',
    'AT'         : '#2F4F4F',
    'COLONCOLON' : '#2F4F4F',

    # Операторы
    'ASSIGN'     : '#000000',  # Black (для операторов)
    'GT'         : '#000000',
    'LT'         : '#000000',
    'BANG'       : '#000000',
    'TILDE'      : '#000000',
    'QUESTION'   : '#000000',
    'COLON'      : '#000000',
    'ARROW'      : '#000000',
    'EQUAL'      : '#000000',
    'LE'         : '#000000',
    'GE'         : '#000000',
    'NOTEQUAL'   : '#000000',
    'AND'        : '#000000',
    'OR'         : '#000000',
    'INC'        : '#000000',
    'DEC'        : '#000000',
    'ADD'        : '#000000',
    'SUB'        : '#000000',
    'MUL'        : '#000000',
    'DIV'        : '#000000',
    'BITAND'     : '#000000',
    'BITOR'      : '#000000',
    'CARET'      : '#000000',
    'MOD'        : '#000000',
    'ADD_ASSIGN' : '#000000',
    'SUB_ASSIGN' : '#000000',
    'MUL_ASSIGN' : '#000000',
    'DIV_ASSIGN' : '#000000',
    'AND_ASSIGN' : '#000000',
    'OR_ASSIGN'  : '#000000',
    'XOR_ASSIGN' : '#000000',
    'MOD_ASSIGN' : '#000000',
    'LSHIFT_ASSIGN'  : '#000000',
    'RSHIFT_ASSIGN'  : '#000000',
    'URSHIFT_ASSIGN' : '#000000',

    # Прочее
    'UNDER_SCORE' : '#2F4F4F',
    'COMMENT'     : '#006400'  #  темно-зеленый (для комментариев)
    }
    '''     
    colors = {
        'EXPORTS'     :  'purple',  #Экспортирует пакет с модулем
        'MODULE'      :  'purple',
        'OACA'        :  '#1A1100',  #'<>'
        'OPEN'        :  '#004080',
        'OPENS'       :  '#004080',
        'PERMITS'     :  'purple',   #запечатанный класс
        'PROVIDES'    :  '#004080',
        'RECORD'      :  '#004080',
        'REQUIRES'    :  '#004080',  #requires 
        'SEALED'      :  '#004080',
        'TO'          :  '#004080',
        'TRANSITIVE'  :  '#004080',
        'USES'        :  'purple',   #указания зависимости модуля от сервиса.
        'VAR'         :  '#004466',  #переменные
        'WITH'        :  '#004080',
        'YIELD'       :  '#004080',

        'ASSERT'      :  '#004080',
        'BOOLEAN'     :  '#003399',  #тип данных
        'BREAK'       :  '#004080',
        'BYTE'        :  '#003399',  #тип данных
        'CASE'        :  '#004080',
        'CATCH'       :  '#004080',
        'CHAR'        :  '#003399',  #тип данных
        'CLASS'       :  '#0D4D00',
        'CONST'       :  '#004080',  #определяет класс
        'CONTINUE'    :  '#004080',
        'DEFAULT'     :  '#004080',
        'DO'          :  '#004080',
        'DOUBLE'      :  '#003399',  #тип данных
        'ELSE'        :  '#004080',
        'ENUM'        :  '#4B0082',  #объявляет перечисляемый (неизменяемый) тип
        'EXTENDS'     :  'purple',   #расширяет класс (указывает, что класс унаследован от другого класса)
        'FINAL'       :  '#008080',  #модификатор
        'FINALLY'     :  '#008080',  #Модификатор 
        'FLOAT'       :  '#003399',  #тип данных
        'FOR'         :  '#004080',
        'IF'          :  '#004080',
        'GOTO'        :  '#004080',
        'IMPLEMENTS'  :  'purple',  #Реализует интерфейс
        'IMPORT'      :  'purple',  #Используется для импорта пакета, класса или интерфейса
        'INSTANCEOF'  :  '#004080', #Проверяет, является ли объект экземпляром определенного класса или интерфейса
        'INT'         :  '#003399', #тип данных
        'INTERFACE'   :  '#0D4D00', #Используется для объявления особого типа класса, который содержит только абстрактные методы
        'LONG'        :  '#003399', #тип данных
        'NATIVE'      :  '#4B0082', #указывает, что метод не реализован в том же исходном файле Java (но на другом языке)
        'NEW'         :  '#662200', #создаёт новые объекты
        'PACKAGE'     :  'purple',  #Объявляет пакет
        'PRIVATE'     :  '#008080', #модификатор
        'PROTECTED'   :  '#008080', #модификатор 
        'PUBLIC'      :  '#008080', #модификатор 
        'RETURN'      :  '#008080', #модификатор 
        'SHORT'       :  '#003399', #тип данных
        'STATIC'      :  '#008080', #модификатор 
        'STRICTFP'    :  '#004080', #ограничивает точность и округление вычислений с плавающей запятой
        'SUPER'       :  '#004080', #относится к объектам суперкласса (родительского)
        'SWITCH'      :  '#004080',    
        'SYNCHRONIZED':  '#008080', #модификатор 
        'THIS'        :  '#994D00', # ссылается на текущий объект в методе или конструкторе
        'THROW'       :  '#004080',
        'THROWS'      :  '#004080',
        'TRANSIENT'   :  '#008080', #модификатор
        'TRY'         :  '#004080',
        'VOID'        :  '#4B0082', #указывает, что метод не должен иметь возвращаемого значения           
        'VOLATILE'    :  '#004080', #указывает, что атрибут не кэшируется локально в потоке и всегда читается из «основной памяти». 
        'WHILE'       :  '#004080',
        'UNDER_SCORE' :  '#004080',
        'COMMENT'     :  '#003311',

        'NullLiteral'    : '#99001A',
        'BooleanLiteral' : '#99001A',

        'LPAREN'     : '#1A1100',
        'RPAREN'     : '#1A1100',
        'LBRACE'     : '#1A1100',
        'RBRACE'     : '#1A1100',
        'LBRACK'     : '#1A1100',
        'RBRACK'     : '#1A1100',
        'SEMI'       : '#1A1100',
        'COMMA'      : '#1A1100',
        'DOT'        : '#1A1100',
        'ELLIPSIS'   : '#1A1100',
        'AT'         : '#1A1100',
        'COLONCOLON' : '#1A1100',
        'ASSIGN'     : '#1A1100',
        'GT'         : '#1A1100',
        'LT'         : '#1A1100',
        'BANG'       : '#1A1100',
        'TILDE'      : '#1A1100',
        'QUESTION'   : '#1A1100',
        'COLON'      : '#1A1100',
        'ARROW'      : '#1A1100',
        'EQUAL'      : '#1A1100',
        'LE'         : '#1A1100',
        'GE'         : '#1A1100',
        'NOTEQUAL'   : '#1A1100',
        'AND'        : '#1A1100',
        'OR'         : '#1A1100',
        'INC'        : '#1A1100',
        'DEC'        : '#1A1100',
        'ADD'        : '#1A1100',
        'SUB'        : '#1A1100',
        'MUL'        : '#1A1100',
        'DIV'        : '#1A1100',
        'BITAND'     : '#1A1100',
        'BITOR'      : '#1A1100',
        'CARET'      : '#1A1100',
        'MOD'        : '#1A1100',
        'ADD_ASSIGN' : '#1A1100',
        'SUB_ASSIGN' : '#1A1100',
        'MUL_ASSIGN' : '#1A1100',
        'DIV_ASSIGN' : '#1A1100',
        'AND_ASSIGN' : '#1A1100',
        'OR_ASSIGN'  : '#1A1100',
        'XOR_ASSIGN' : '#1A1100',
        'MOD_ASSIGN' : '#1A1100',
        'LSHIFT_ASSIGN'  : '#991900',
        'RSHIFT_ASSIGN'  : '#991900',
        'URSHIFT_ASSIGN' : '#991900',

    }'''    
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
