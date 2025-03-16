grammar STFile;

// Пропуск BOM (Byte Order Mark)
BOM: '\uFEFF' -> skip;

// Корневая структура файла
fileStructure: LBRACE INT ',' entryStructure (',' entryStructure)* RBRACE (RBRACE | WS);

// Структура элемента (может быть вложенной)

//entryStructure: LBRACE INT ',' (folderEntry | templateEntry | entryStructure) (',' entryStructure)* RBRACE;
entryStructure: LBRACE INT ',' (folderEntry | templateEntry | nestedEntry) RBRACE;

// Вложенные структуры
nestedEntry: LBRACE INT ',' entryStructure* RBRACE;

// Структура папки
folderEntry: LBRACE STRING ',' '1' ',' '0' ',' STRING (',' STRING)? RBRACE;

// Структура шаблона
templateEntry: LBRACE STRING ',' '0' ',' '0' ',' STRING (',' STRING)? RBRACE;

// Лексемы
DIGIT: [0-9];
INT: DIGIT+;  // Правильно: теперь `INT` не конфликтует

LBRACE: '{';  // Открывающая фигурная скобка
RBRACE: '}';  // Закрывающая фигурная скобка

// Строка (поддерживает экранированные символы и юникод)
STRING: '"' ( '""' | '\\' . | ~["\\] )* '"';


SYMBOL: [()[\]|=<>*+-,;&.:/\\%!`?'@#]+;

//WORD: [\u0400-\u04FFa-zA-Z0-9_]+;

// Слова из всех языков мира + цифры
WORD: [\p{L}\p{N}_\u2013\u2014\u2026\u2022\u201C\u201D\u00AB\u00BB]+;

// Эмодзи
EMOJI: [\p{So}\p{Sk}]+;

// Математические символы
MATH_SYMBOL: [\p{Sm}]+;

// Пропускаем пробелы, табуляции и переводы строк
WS: [ \t\r\n\u00A0\u00AD\u000B\f\u2002\u2003\u2009\u202F]+ -> skip;
