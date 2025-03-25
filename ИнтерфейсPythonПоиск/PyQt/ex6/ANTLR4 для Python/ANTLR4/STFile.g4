grammar STFile;

BOM: '\uFEFF' -> skip;

// Корневая структура файла: всегда начинается с {1, ...}
fileStructure: LBRACE '1' ',' rootContent RBRACE;

// Содержимое корневой структуры: папка с количеством элементов
rootContent: LBRACE count=forceInt ',' folderContent RBRACE;  // Используем forceInt вместо INT

// Содержимое папки: заголовок папки и вложенные элементы
folderContent: folderHeader ',' nestedEntries;

// Вложенные элементы: папки или шаблоны
nestedEntries: entry (',' entry)*;

// Запись: папка или шаблон
entry:
    LBRACE count=forceInt ',' header=headerContent ',' nestedEntries RBRACE
    {STFileParserExtensions.isFolder($header.type, $header.flags)}?  // Проверка, что это папка
    |
    LBRACE '0' ',' header=headerContent RBRACE
    {STFileParserExtensions.isTemplate($header.type, $header.flags)}?  // Проверка, что это шаблон
;

// Заголовок папки или шаблона
headerContent returns [String type, String flags]:
    LBRACE
    name=STRING ',' 
    t_type=INT ','      // Тип (1 для папки, 0 для шаблона)
    f_flags=INT ','     // Флаги (0 или 1)
    param1=STRING ','   // Параметр 1
    param2=STRING       // Параметр 2
    RBRACE
    {
        // Присваиваем возвращаемые значения
        $type = $t_type.text;
        $flags = $f_flags.text;
    }
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

// Лексемы
INT: [0-9]+;
// Слова из всех языков мира + цифры
WORD: [\p{L}\p{N}_\u2013\u2014\u2026\u2022\u201C\u201D\u00AB\u00BB]+;

STRING: '"' ( '""' | '\\' .  | ~["\\\r\n] )* '"'; // Разрешены экранированные кавычки и обратные слэши
SYMBOL: [()[\]|=<>*+-,;&.:/\\%!`?'@#]+;   // распозноваие символов
LBRACE: '{';
RBRACE: '}';
// Пропускаем пробелы, табуляции и переводы строк
WS: [ \t\r\n\u00A0\u00AD\u000B\f\u2002\u2003\u2009\u202F]+ -> skip;

// Семантический предикат для принудительного распознавания INT
forceInt: INT {STFileParserExtensions.isInteger($INT.text)}?;

