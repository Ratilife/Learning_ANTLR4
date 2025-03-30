grammar STFile;

BOM: '\uFEFF' -> skip;

fileStructure: LBRACE INT ',' rootContent RBRACE;

rootContent: LBRACE INT ',' folderContent RBRACE;


//folderContent: 
//    folderHeader ',' entriesBlock 
//    | folderHeader (',' entry)* 
//;

//entriesBlock: LBRACE (entry (',' entry)*)? RBRACE;
folderContent: folderHeader (',' entry)*;

entry:
// Папка: {count, header, вложенные_элементы}
    //LBRACE INT ',' folderHeader ','(entriesBlock |entry (','  entry)*) RBRACE
    LBRACE INT ',' folderHeader ',' entryList RBRACE
    |
// Шаблон: {0, header}
    LBRACE '0' ',' templateHeader RBRACE
;

entryList: entry (',' entry)*;

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

INT: [0-9\uFF10-\uFF19]+;   // Обычные и Unicode-цифры
STRING: '"' ('""' | ~["])* '"';
LBRACE: '{';
RBRACE: '}';
WS: [ \t\r\n]+ -> skip;