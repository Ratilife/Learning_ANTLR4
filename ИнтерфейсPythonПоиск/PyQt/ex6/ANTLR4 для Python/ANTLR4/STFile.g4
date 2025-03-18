grammar STFile;

BOM: '\uFEFF' -> skip;

fileStructure: LBRACE '1' ',' entries RBRACE;

entries: entry (',' entry)*;

entry:
    // Папка: {кол-во_вложений, {"Название", 1, ...}, вложенные_элементы}
    LBRACE count=INT ',' folderHeader ',' nested_entries RBRACE
    |
    // Шаблон: {0, {"Название", 0, ...}}
    LBRACE '0' ',' templateHeader RBRACE
;

nested_entries: entry (',' entry)*;

folderHeader:
    LBRACE
    name=STRING ',' 
    '1' ','  // Тип "Папка" (второй параметр = 1)
    flags=INT ',' 
    param1=STRING ',' 
    param2=STRING
    RBRACE
;

templateHeader:
    LBRACE
    name=STRING ',' 
    '0' ','  // Тип "Шаблон" (второй параметр = 0)
    flags=INT ',' 
    param1=STRING ',' 
    codeBlock=STRING
    RBRACE
;

// Лексемы
INT: [0-9]+;
STRING: '"' ( '\\' . | ~["\\] )* '"';
LBRACE: '{';
RBRACE: '}';
WS: [ \t\r\n]+ -> skip;