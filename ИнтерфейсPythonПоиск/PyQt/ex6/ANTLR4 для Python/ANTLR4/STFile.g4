grammar STFile;

BOM: '\uFEFF' -> skip;
fileStructure: '{' INT ',' (entryStructure (',' entryStructure)*)? '}';
entryStructure: '{' INT ',' (folderEntry | templateEntry) (',' entryStructure)* '}';
folderEntry: '{' STRING ',' '1' ',' '0' ',' STRING ',' STRING '}';
templateEntry: '{' STRING ',' '0' ',' '0' ',' STRING ',' STRING '}';

INT: [0-9]+;
STRING: '"' ( '\\' [btnfr"\\] . | ~["\\\r\n] )* '"';  // Разрешены любые символы, включая кириллицу и []
WORD: [\u0400-\u04FFa-zA-Z0-9_]+;


SYMBOL: [()|=<>*+-[],;&.:/\\];

// Пропускаем пробелы, табуляции и переводы строк
WS: [ \t\r\n\u00A0\u00AD\v\f]+ -> skip;
