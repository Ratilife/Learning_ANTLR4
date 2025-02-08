from graphviz import Digraph
from antlr4 import *
from Python3.PythonLexer import PythonLexer
from CShar.CSharpLexer import CSharpLexer



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
                'SINGLE_LINE_DOC_COMMENT'     : '///' InputCharacter*   -> channel(COMMENTS_CHANNEL);
                'EMPTY_DELIMITED_DOC_COMMENT' : '/***/'                 -> channel(COMMENTS_CHANNEL);
                'DELIMITED_DOC_COMMENT'       : '/**' ~'/' .*? '*/'     -> channel(COMMENTS_CHANNEL);
                'SINGLE_LINE_COMMENT'         : '//' InputCharacter*    -> channel(COMMENTS_CHANNEL);
                'DELIMITED_COMMENT'           : '/*' .*? '*/'           -> channel(COMMENTS_CHANNEL);
                'WHITESPACES'                 : (Whitespace | NewLine)+ -> channel(HIDDEN);
                'SHARP'                       : 'orange'                    

                'ABSTRACT'   : 'abstract';
                'ADD'        : 'add';
                'ALIAS'      : 'alias';
                'ARGLIST'    : '__arglist';
                'AS'         : 'as';
                'ASCENDING'  : 'ascending';
                'ASYNC'      : 'async';
                'AWAIT'      : 'await';
                'BASE'       : 'base';
                'BOOL'       : 'bool';
                'BREAK'      : 'break';
                'BY'         : 'by';
                'BYTE'       : 'byte';
                'CASE'       : 'case';
                'CATCH'      : 'catch';
                'CHAR'       : 'char';
                'CHECKED'    : 'checked';
                'CLASS'      : 'class';
                'CONST'      : 'const';
                'CONTINUE'   : 'continue';
                'DECIMAL'    : 'decimal';
                'DEFAULT'    : 'default';
                'DELEGATE'   : 'delegate';
                'DESCENDING' : 'descending';
                'DO'         : 'do';
                'DOUBLE'     : 'double';
                'DYNAMIC'    : 'dynamic';
                'ELSE'       : 'else';
                'ENUM'       : 'enum';
                'EQUALS'     : 'equals';
                'EVENT'      : 'event';
                'EXPLICIT'   : 'explicit';
                'EXTERN'     : 'extern';
                'FALSE'      : 'false';
                'FINALLY'    : 'finally';
                'FIXED'      : 'fixed';
                'FLOAT'      : 'float';
                'FOR'        : 'for';
                'FOREACH'    : 'foreach';
                'FROM'       : 'from';
                'GET'        : 'get';
                'GOTO'       : 'goto';
                'GROUP'      : 'group';
                'IF'         : 'if';
                'IMPLICIT'   : 'implicit';
                'IN'         : 'in';
                'INT'        : 'int';
                'INTERFACE'  : 'interface';
                'INTERNAL'   : 'internal';
                'INTO'       : 'into';
                'IS'         : 'is';
                'JOIN'       : 'join';
                'LET'        : 'let';
                'LOCK'       : 'lock';
                'LONG'       : 'long';
                'NAMEOF'     : 'nameof';
                'NAMESPACE'  : 'namespace';
                'NEW'        : 'new';
                'NULL_'      : 'null';
                'OBJECT'     : 'object';
                'ON'         : 'on';
                'OPERATOR'   : 'operator';
                'ORDERBY'    : 'orderby';
                'OUT'        : 'out';
                'OVERRIDE'   : 'override';
                'PARAMS'     : 'params';
                'PARTIAL'    : 'partial';
                'PRIVATE'    : 'private';
                'PROTECTED'  : 'protected';
                'PUBLIC'     : 'public';
                'READONLY'   : 'readonly';
                'REF'        : 'ref';
                'REMOVE'     : 'remove';
                'RETURN'     : 'return';
                'SBYTE'      : 'sbyte';
                'SEALED'     : 'sealed';
                'SELECT'     : 'select';
                'SET'        : 'set';
                'SHORT'      : 'short';
                'SIZEOF'     : 'sizeof';
                'STACKALLOC' : 'stackalloc';
                'STATIC'     : 'static';
                'STRING'     : 'string';
                'STRUCT'     : 'struct';
                'SWITCH'     : 'switch';
                'THIS'       : 'this';
                'THROW'      : 'throw';
                'TRUE'       : 'true';
                'TRY'        : 'try';
                'TYPEOF'     : 'typeof';
                'UINT'       : 'uint';
                'ULONG'      : 'ulong';
                'UNCHECKED'  : 'unchecked';
                'UNMANAGED'  : 'unmanaged';
                'UNSAFE'     : 'unsafe';
                'USHORT'     : 'ushort';
                'USING'      : 'using';
                'VAR'        : 'var';
                'VIRTUAL'    : 'virtual';
                'VOID'       : 'void';
                'VOLATILE'   : 'volatile';
                'WHEN'       : 'when';
                'WHERE'      : 'where';
                'WHILE'      : 'while';
                'YIELD'      : 'yield';
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