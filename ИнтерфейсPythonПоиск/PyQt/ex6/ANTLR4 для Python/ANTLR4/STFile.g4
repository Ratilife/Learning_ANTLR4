grammar STFile;

fileStructure: '{' INT ',' (entryStructure (',' entryStructure)*)? '}';
entryStructure: '{' INT ',' (folderEntry | templateEntry) (',' entryStructure)* '}';
folderEntry: '{' STRING ',' '1' ',' '0' ',' STRING ',' STRING '}';
templateEntry: '{' STRING ',' '0' ',' '0' ',' STRING ',' STRING '}';

INT: [0-9]+;
STRING: '"' ( '\\' . | ~["\\\r\n\u0400-\u04FF] )* '"';
WORD: [\u0400-\u04FFa-zA-Z0-9_]+;

// Определяем отдельные токены для символов
LBRACK: '[';
RBRACK: ']';
SYMBOL: [()|=<>*+-,;&.:/\\];

WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip;