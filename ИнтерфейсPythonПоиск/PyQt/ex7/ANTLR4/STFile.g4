grammar STFile;

BOM: '\uFEFF' -> skip;

fileStructure: LBRACE '1' ',' rootContent RBRACE;

rootContent: LBRACE INT ',' folderContent RBRACE;

folderContent: folderHeader ',' entriesBlock;

entriesBlock: LBRACE (entry (',' entry)*)? RBRACE;

entry:
    // Папка: {count, header, вложенные_элементы}
    LBRACE INT ',' folderHeader ',' entriesBlock RBRACE
    |
    // Шаблон: {0, header}
    LBRACE '0' ',' templateHeader RBRACE
;

folderHeader:
    LBRACE
    STRING ',' 
    INT ','    // type (любое число)
    INT ','    // flags (любое число)
    STRING ',' 
    STRING
    RBRACE
;

templateHeader:
    LBRACE
    STRING ',' 
    '0' ','     // type (строго 0)
    ('0' | '1') ',' // flags (0 или 1)
    STRING ',' 
    STRING
    RBRACE
;

INT: [0-9]+;
STRING: '"' ('""' | ~["])* '"';
LBRACE: '{';
RBRACE: '}';
WS: [ \t\r\n]+ -> skip;