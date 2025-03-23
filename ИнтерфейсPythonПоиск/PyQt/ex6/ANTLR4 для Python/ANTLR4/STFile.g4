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
    {self.isFolder($header)}?  // Проверка, что это папка
    |
    LBRACE '0' ',' header=headerContent RBRACE
    {self.isTemplate($header)}?  // Проверка, что это шаблон
;

// Заголовок папки или шаблона
headerContent:
    LBRACE
    name=STRING ',' 
    type=INT ','  // Тип (1 для папки, 0 для шаблона)
    flags=INT ','  // Флаги (0 или 1)
    param1=STRING ','  // Параметр 1
    param2=STRING      // Параметр 2
    RBRACE
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

    def isFolder(self, header):
        # Проверка, что тип папки равен 1, а константа равна 0
        return header.type.text == '1' and header.flags.text == '0'

    def isTemplate(self, header):
        # Проверка, что тип шаблона равен 0, а флаги равны 0 или 1
        return header.type.text == '0' and header.flags.text in {'0', '1'}
}