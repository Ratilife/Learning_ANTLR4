grammar STFile;

BOM: '\uFEFF' -> skip;

// Корневая структура файла: всегда начинается с {1, ...}
fileStructure: LBRACE '1' ',' rootContent RBRACE;

// Содержимое корневой структуры: папка с количеством элементов
rootContent: LBRACE count=forceInt ',' folderContent RBRACE;        // Используем forceInt вместо INT

// Содержимое папки: заголовок папки и вложенные элементы
folderContent: folderHeader ',' nestedEntries;

// Вложенные элементы: папки или шаблоны
nestedEntries: entry (',' entry)*;

// Запись: папка или шаблон
entry:
    // Папка: {count, {"Название", 1, 0, "", ""}, вложенные_элементы}
    LBRACE count=forceInt ',' folderHeader ',' nestedEntries RBRACE    //Используем forceInt вместо INT
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

// Слова из всех языков мира + цифры
WORD: [\p{L}\p{N}_\u2013\u2014\u2026\u2022\u201C\u201D\u00AB\u00BB]+;
INT: [0-9]+;
STRING: '"' ( '""' | '\\' .  | ~["\\\r\n] )* '"'; // Разрешены экранированные кавычки и обратные слэши
SYMBOL: [()[\]|=<>*+-,;&.:/\\%!`?'@#]+;   // распозноваие символов
LBRACE: '{';
RBRACE: '}';
// Пропускаем пробелы, табуляции и переводы строк
WS: [ \t\r\n\u00A0\u00AD\u000B\f\u2002\u2003\u2009\u202F]+ -> skip;

// Семантический предикат для принудительного распознавания INT
forceInt: {self.isInteger(_input.LT(1).text)}? INT;

@parser::members {
    def isInteger(self, text):
        try:
            int(text)
            return True
        except ValueError:
            return False
}