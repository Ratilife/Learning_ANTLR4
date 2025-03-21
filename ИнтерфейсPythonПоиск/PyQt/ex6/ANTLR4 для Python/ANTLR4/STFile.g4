grammar STFile;

BOM: '\uFEFF' -> skip;

// Корневая структура файла: всегда начинается с {1, ...}
fileStructure: LBRACE '1' ',' rootContent RBRACE;

// Содержимое корневой структуры: папка с количеством элементов
rootContent: LBRACE count=INT ',' folderContent RBRACE;

// Содержимое папки: заголовок папки и вложенные элементы
folderContent: folderHeader ',' nestedEntries;

// Вложенные элементы: папки или шаблоны
nestedEntries: entry (',' entry)*;

// Запись: папка или шаблон
entry:
    // Папка: {count, {"Название", 1, 0, "", ""}, вложенные_элементы}
    LBRACE count=INT ',' folderHeader ',' nestedEntries RBRACE
    |
    // Шаблон: {0, {"Название", 0, 0, "@ТекстДляАвтоЗаполнения", "текст шаблона"}}
    LBRACE '0' ',' templateHeader RBRACE
;

// Заголовок папки: {"Название", 1, 0, "", ""}
folderHeader:
    LBRACE
    name=STRING ',' 
    '1' ','  // Тип "Папка" (второй параметр = 1)
    '0' ','  // Константа (третий параметр = 0)
    empty1=STRING ','  // Пустая строка (четвёртый параметр)
    empty2=STRING      // Пустая строка (пятый параметр)
    RBRACE
;

// Заголовок шаблона: {"Название", 0, 0, "@ТекстДляАвтоЗаполнения", "текст шаблона"}
templateHeader:
    LBRACE
    name=STRING ',' 
    '0' ','  // Тип "Шаблон" (второй параметр = 0)
    flags=INT ','  // Флаги (третий параметр, может быть 0 или 1)
    param1=STRING ','  // Параметр 1 (четвёртый параметр)
    codeBlock=STRING   // Код шаблона (пятый параметр)
    RBRACE
;

// Лексемы
INT: [0-9]+;
STRING: '"' ( '""' | '\\' .  | ~["\\\r\n] )* '"'; // Разрешены экранированные кавычки и обратные слэши
LBRACE: '{';
RBRACE: '}';
WS: [ \t\r\n]+ -> skip;