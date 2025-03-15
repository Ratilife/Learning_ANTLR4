grammar STFile;

BOM: '\uFEFF' -> skip;
fileStructure: LBRACE INT ',' (entryStructure (',' entryStructure)*)? RBRACE;
entryStructure: LBRACE INT ',' (folderEntry | templateEntry) (',' entryStructure)* RBRACE;
folderEntry: LBRACE STRING ',' '1' ',' '0' ',' STRING (',' STRING)? RBRACE;
templateEntry: LBRACE STRING ',' '0' ',' '0' ',' STRING (',' STRING)? RBRACE;

DIGIT: [0-9];
INT: DIGIT+;  // Правильно: теперь `INT` не конфликтует

STRING: '"' ( '\\' [btnfr"\\] | '\\' . | ~["\\] )* '"';

LBRACE: '{';  // Открывающая фигурная скобка
RBRACE: '}';  // Закрывающая фигурная скобка

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
