lexer grammar CSharpPreprocessorLexer;

// Определение токенов
WS      : [ \t\r\n]+ -> skip; // Пропускаем пробелы
NEWLINE : [\r\n]+;

// Директивы препроцессора -  ОБЪЕДИНЕНЫ В ОДНО РЕГУЛЯРНОЕ ВЫРАЖЕНИЕ
PREPROCESSOR_DIRECTIVE
    : '#' ('define' | 'undef' | 'if' | 'else' | 'elif' | 'endif' )
      [ \t\r\n]* //позволяет пропускать пробелы после директив
    ;


// Определите другие токены по мере необходимости
ID      : [a-zA-Z_][a-zA-Z0-9_]*; // Идентификаторы
STRING  : '"' ( ~["\\] | '\\' . )* '"'; // Строки
