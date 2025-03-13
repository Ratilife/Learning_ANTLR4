grammar STFile;

BOM: '\uFEFF' -> skip;
fileStructure: '{' INT ',' (entryStructure (',' entryStructure)*)? '}';
entryStructure: '{' INT ',' (folderEntry | templateEntry) (',' entryStructure)* '}';
folderEntry: '{' STRING ',' '1' ',' '0' ',' STRING ',' STRING '}';
templateEntry: '{' STRING ',' '0' ',' '0' ',' STRING ',' STRING '}';

DIGIT: [0-9];
INT: DIGIT+;  // Правильно: теперь `INT` не конфликтует

STRING: '"' ( '\\' [btnfr"\\] | ~["\\]  )* '"';
SYMBOL: [\[\]()|=<>*+-,;&.:/\\%!`?'@#]+;  

WORD: [\u0400-\u04FFa-zA-Z0-9_]+;

// Пропускаем пробелы, табуляции и переводы строк
WS: [ \t\r\n\u00A0\u00AD\u000B\f\u2002\u2003\u2009\u202F]+ -> skip;
