"""
Модуль для анализа и визуализации структуры ST-файлов с использованием ANTLR4 и NetworkX.

Основные функции:
- Разбор ST-файлов с поддержкой кодировки UTF-8 BOM.
- Проверка баланса скобок.
- Визуализация структуры файла в виде графа.
- Обработка и вывод синтаксических ошибок.

Классы:
- STFileInfoListener: Слушатель для обработки правил и ошибок парсера.
- TreeGraphListener: Слушатель для построения графа структуры файла.

Функции:
- read_file_with_bom: Чтение файла с учетом BOM.
- check_braces_balance: Проверка баланса скобок в файле.
- main: Основная функция для запуска анализа.

Пример использования:
    python STFilePython.py
"""
import networkx as nx
import matplotlib.pyplot as plt
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker, DiagnosticErrorListener
from ANTLR4.STFileLexer import STFileLexer
from ANTLR4.STFileParser import STFileParser
from antlr4.tree.Tree import TerminalNodeImpl, ParseTreeListener
from STFileCustomListener import STFileCustomListener

class STFileInfoListener(STFileCustomListener):
    """
    Слушатель для обработки правил парсера и сбора ошибок.

    Атрибуты:
        indent (int): Текущий уровень отступа для вывода.
        current_rule (str): Текущее обрабатываемое правило.
        error_messages (list): Список сообщений об ошибках.

    Методы:
        enterEveryRule: Обработка входа в правило.
        exitEveryRule: Обработка выхода из правила.
        syntaxError: Обработка синтаксических ошибок.
        get_errors: Возвращает список ошибок.
    """
    def __init__(self):
        super().__init__()
        self.indent = 0
        self.current_rule = None
        self.error_messages = []
    
    def get_indent(self):
        """Возвращает строку с отступом."""
        return "  " * self.indent
    
    def enterEveryRule(self, ctx):
        """
        Обработка входа в правило.
        
        Args:
            ctx: Контекст правила.
        """
        rule_name = STFileParser.ruleNames[ctx.getRuleIndex()]
        self.current_rule = rule_name
        text = ctx.getText().replace("\n", "\\n").replace("\r", "\\r")
        if len(text) > 50:
            text = text[:47] + "..."
        print(f"{self.get_indent()}{text} - правило: {rule_name}")
        self.indent += 1
        super().enterEveryRule(ctx)
    
    def exitEveryRule(self, ctx):
        """
        Обработка выхода из правила.
        
        Args:
            ctx: Контекст правила.
        """
        self.indent -= 1
        self.current_rule = None
        super().exitEveryRule(ctx)
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Обработка синтаксической ошибки.
        
        Args:
            recognizer: Распознаватель ANTLR.
            offendingSymbol: Ошибочный символ.
            line: Номер строки.
            column: Номер столбца.
            msg: Сообщение об ошибке.
            e: Исключение.
        """
        error_msg = f"Line {line}:{column} - правило: {self.current_rule or 'unknown'} - ошибка: {msg}"
        self.error_messages.append(error_msg)
        print(error_msg)
        
        # Получаем текст из исходного файла
        try:
            with open("Новый2.st", "r", encoding="utf-8") as f:
                lines = f.readlines()
                if line > 0 and line <= len(lines):
                    error_line = lines[line-1].rstrip()
                    print(error_line)
                    print(" " * (column) + "^")
        except Exception as e:
            print(f"Не удалось прочитать файл для отображения ошибки: {str(e)}")
    
    def get_errors(self):
        """Возвращает список ошибок."""
        return self.error_messages

class TreeGraphListener(ParseTreeListener):
    def __init__(self, graph, parser):
        self.G = graph
        self.parser = parser
        self.node_stack = []  # Стек для отслеживания родительских узлов
    
    def enterEveryRule(self, ctx):
        rule_name = STFileParser.ruleNames[ctx.getRuleIndex()]
        node_id = f"rule_{id(ctx)}"
        self.G.add_node(node_id, label=rule_name, type='rule')
        
        if self.node_stack:
            self.G.add_edge(self.node_stack[-1], node_id)
        
        self.node_stack.append(node_id)
    
    def visitTerminal(self, node):
        text = node.getText()
        if len(text) > 20:
            text = text[:17] + "..."
        node_id = f"term_{id(node)}"
        self.G.add_node(node_id, label=text, type='terminal')
        
        if self.node_stack:
            self.G.add_edge(self.node_stack[-1], node_id)
    
    def exitEveryRule(self, ctx):
        if self.node_stack:
            self.node_stack.pop()

class PrettyTreeListener(ParseTreeListener):
    def __init__(self):
        self.tree = []
        self.current_level = 0
        self.connectors = []
    
    def enterEveryRule(self, ctx):
        rule_name = STFileParser.ruleNames[ctx.getRuleIndex()]
        connector = '├── ' if self.current_level > 0 else ''
        indent = ''.join(self.connectors[:self.current_level])
        self.tree.append(f"{indent}{connector}{rule_name}")
        self.connectors.append('│   ' if self.current_level > 0 else '    ')
        self.current_level += 1
    
    def visitTerminal(self, node):
        text = node.getText().replace('\n', '\\n').replace('\r', '\\r')
        if len(text) > 50:
            text = text[:20] + "[...]" + text[-20:]
        connector = '├── ' if self.current_level > 0 else ''
        indent = ''.join(self.connectors[:self.current_level])
        self.tree.append(f"{indent}{connector}{text}")
    
    def exitEveryRule(self, ctx):
        self.current_level -= 1
        if self.connectors:
            self.connectors.pop()
    
    def get_pretty_tree(self):
        header = "="*50 + "\nСтруктура файла:\n" + "="*50
        return header + "\n" + "\n".join(self.tree) + "\n" + "="*50
    
    def save_to_file(self, filename="structure.txt"):
        """Сохраняет структуру дерева в файл в исходном формате"""
        with open(filename, "w", encoding="utf-8") as f:
            for line in self.tree:
                if line.startswith("fileStructure"):
                    continue
                f.write(f"{line}\n")

    def save_to_file1(self, filename="structure.txt"):
        """Сохраняет структуру дерева в файл в заданном формате"""
        with open(filename, "w", encoding="utf-8") as f:
            for line in self.tree:
                # Убираем лишние пробелы в начале строки
                cleaned_line = line.lstrip()
                # Заменяем правило "fileStructure" на пустую строку
                if cleaned_line.startswith("fileStructure"):
                    continue
                # Заменяем отступы для правил на 4 пробела
                if any(rule in cleaned_line for rule in STFileParser.ruleNames):
                    indent = "    " * (line.count('│   ') + line.count('    '))
                    f.write(f"{indent}{cleaned_line}\n")
                else:
                    # Для терминалов добавляем дополнительный отступ
                    indent = "    " * (line.count('│   ') + line.count('    ') + 1)
                    f.write(f"{indent}{cleaned_line}\n")
        
def read_file_with_bom(file_path):
    """
    Чтение файла с учетом BOM (Byte Order Mark).
    
    Args:
        file_path (str): Путь к файлу.
    
    Returns:
        str: Содержимое файла в кодировке UTF-8.
    """
    with open(file_path, "rb") as file:
        raw_data = file.read()
        if raw_data.startswith(b"\xef\xbb\xbf"):
            return raw_data.decode("utf-8-sig")
        return raw_data.decode("utf-8")

def check_braces_balance(file_content):
    """
    Проверка баланса скобок в содержимом файла.
    
    Args:
        file_content (str): Содержимое файла.
    
    Raises:
        ValueError: Если обнаружены несбалансированные скобки.
    """
    stack = []
    lines = file_content.split('\n')  # Разбиваем содержимое на строки
    
    for line_num, line in enumerate(lines, start=1):
        for char_pos, char in enumerate(line):
            if char == '{':
                # Сохраняем номер строки и позицию в строке
                stack.append((line_num, char_pos + 1))  # +1 для удобства (позиция начинается с 1)
            elif char == '}':
                if not stack:
                    raise ValueError(f"Лишняя закрывающая скобка в строке {line_num}, позиция {char_pos + 1}")
                stack.pop()

    if stack:
        error_lines = []
        for line_num, char_pos in stack:
            # Получаем текст строки с ошибкой
            error_line = lines[line_num - 1]
            # Формируем сообщение с указанием строки, позиции и самой строки
            error_msg = (f"Не хватает закрывающей скобки для открывающей в строке {line_num}, позиция {char_pos}:\n"
                         f"{error_line}\n"
                         f"{' ' * (char_pos - 1)}^")
            error_lines.append(error_msg)
        
        raise ValueError(f"Не хватает {len(stack)} закрывающих скобок:\n\n" + "\n\n".join(error_lines))
    else:
        print("Скобки сбалансированы.")

def save_tokens_to_file(tokens, lexer, filename="tokens_output.txt"):
    """
    Сохраняет список токенов в файл в удобочитаемом формате.
    
    Args:
        tokens: Список токенов из CommonTokenStream
        lexer: Экземпляр лексера
        filename: Имя файла для сохранения (по умолчанию "tokens_output.txt")
    """
    with open(filename, "w", encoding="utf-8") as tokens_file:
        # Заголовок
        tokens_file.write("="*50 + "\nСПИСОК ТОКЕНОВ\n" + "="*50 + "\n")
        tokens_file.write("{:<5} {:<5} {:<20} {}\n".format("Line", "Pos", "Type", "Value"))
        tokens_file.write("-"*50 + "\n")
        
        # Записываем каждый токен
        for token in tokens:
            tokens_file.write("{:<5} {:<5} {:<20} '{}'\n".format(
                token.line, 
                token.column, 
                lexer.ruleNames[token.type - 1], 
                token.text.replace("\n", "\\n").replace("\r", "\\r")
            ))
        
        tokens_file.write("="*50 + "\n")
        tokens_file.write(f"Всего токенов: {len(tokens)}\n")
'''
def visualize_hierarchy( parser, tree):
    """
    Визуализирует структуру файла в виде иерархического дерева.
    
    Args:
        parser: Экземпляр парсера STFileParser.
        tree: Дерево разбора, полученное от парсера.
    """
    import numpy as np
    import networkx as nx
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(14, 10))

    # Создаем граф
    G = nx.DiGraph()
    graph_listener = TreeGraphListener(G, parser)
    walker = ParseTreeWalker()
    walker.walk(graph_listener, tree)

    # Определяем уровни иерархии
    levels = {}
    for node in G.nodes():
        if 'rule_' in node:
            level = len(list(nx.ancestors(G, node)))
            levels[node] = level

    # Создаем позиции для узлов
    pos = {}
    y_offset = 0
    max_level = max(levels.values()) if levels else 0

    for level in range(max_level + 1):
        nodes_at_level = [n for n in levels if levels[n] == level]
        x_positions = np.linspace(0, 10, len(nodes_at_level)+2)[1:-1]
        
        for i, node in enumerate(nodes_at_level):
            pos[node] = (x_positions[i], max_level - level)
        
        # Добавляем терминальные узлы
        for node in G.nodes():
            if node.startswith('term_'):
                predecessors = list(G.predecessors(node))
                if predecessors and predecessors[0] in pos:
                    parent_pos = pos[predecessors[0]]
                    term_count = len([n for n in G.nodes() 
                                    if n.startswith('term_') and 
                                    predecessors[0] in list(G.predecessors(n))])
                    term_idx = [n for n in G.nodes() 
                               if n.startswith('term_') and 
                               predecessors[0] in list(G.predecessors(n))].index(node)
                    
                    pos[node] = (parent_pos[0] - 0.5 + (term_idx+1)/(term_count+1), 
                                max_level - level - 0.3)

    # Рисуем граф
    node_colors = []
    node_sizes = []
    labels = {}

    for node in G.nodes():
        label = G.nodes[node].get('label', '')
        if len(label) > 15:
            label = label[:12] + "..."
        labels[node] = label
        
        if node.startswith('rule_'):
            node_colors.append('#a6cee3')  # Голубой для правил
            node_sizes.append(2000)
        else:
            node_colors.append('#b2df8a')  # Зеленый для терминалов
            node_sizes.append(1500)

    nx.draw(G, pos, 
           node_color=node_colors,
           node_size=node_sizes,
           labels=labels,
           font_size=8,
           font_weight='bold',
           with_labels=True,
           edge_color='gray',
           width=0.5,
           arrows=False)  # Убираем стрелки

    # Добавляем горизонтальные линии для уровней
    for level in range(max_level + 1):
        nodes_at_level = [n for n in levels if levels[n] == level]
        if nodes_at_level:
            x_positions = [pos[n][0] for n in nodes_at_level]
            plt.hlines(max_level - level, 
                      min(x_positions)-0.5, 
                      max(x_positions)+0.5, 
                      colors='gray', 
                      linestyles='dashed', 
                      alpha=0.3)

    plt.title("Иерархическая структура ST-файла", fontsize=12)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
'''
def visualize_hierarchy(parser, tree):
    """
    Визуализирует структуру файла в виде иерархического дерева.
    
    Args:
        parser: Экземпляр парсера STFileParser.
        tree: Дерево разбора, полученное от парсера.
    """
    import numpy as np
    
    # Создаем фигуру с большими размерами и DPI
    plt.figure(figsize=(16, 12), dpi=100)
    
    # Создаем граф
    G = nx.DiGraph()
    graph_listener = TreeGraphListener(G, parser)
    walker = ParseTreeWalker()
    walker.walk(graph_listener, tree)

    # Определяем уровни иерархии
    levels = {}
    for node in G.nodes():
        if 'rule_' in node:
            level = len(list(nx.ancestors(G, node)))
            levels[node] = level

    # Создаем позиции для узлов
    pos = {}
    max_level = max(levels.values()) if levels else 0
    vertical_spacing = 1.2  # Увеличим вертикальные расстояния

    for level in range(max_level + 1):
        nodes_at_level = [n for n in levels if levels[n] == level]
        x_positions = np.linspace(0, 12, len(nodes_at_level)+2)[1:-1]
        
        for i, node in enumerate(nodes_at_level):
            pos[node] = (x_positions[i], (max_level - level) * vertical_spacing)
        
        # Добавляем терминальные узлы
        for node in G.nodes():
            if node.startswith('term_'):
                predecessors = list(G.predecessors(node))
                if predecessors and predecessors[0] in pos:
                    parent_pos = pos[predecessors[0]]
                    term_count = len([n for n in G.nodes() 
                                    if n.startswith('term_') and 
                                    predecessors[0] in list(G.predecessors(n))])
                    term_idx = [n for n in G.nodes() 
                               if n.startswith('term_') and 
                               predecessors[0] in list(G.predecessors(n))].index(node)
                    
                    pos[node] = (parent_pos[0] - 0.5 + (term_idx+1)/(term_count+1), 
                                (max_level - level) * vertical_spacing - 0.4)

    # Рисуем граф
    node_colors = []
    node_sizes = []
    labels = {}

    for node in G.nodes():
        label = G.nodes[node].get('label', '')
        # Удаляем табуляции и другие спецсимволы из меток
        label = label.replace('\t', ' ').replace('\n', '\\n').replace('\r', '\\r')
        if len(label) > 15:
            label = label[:12] + "..."
        labels[node] = label
        
        if node.startswith('rule_'):
            node_colors.append('#a6cee3')  # Голубой для правил
            node_sizes.append(2000)
        else:
            node_colors.append('#b2df8a')  # Зеленый для терминалов
            node_sizes.append(1500)

    nx.draw(G, pos, 
           node_color=node_colors,
           node_size=node_sizes,
           labels=labels,
           font_size=8,
           font_weight='bold',
           with_labels=True,
           edge_color='gray',
           width=0.5,
           arrows=False)

    # Добавляем горизонтальные линии для уровней
    for level in range(max_level + 1):
        nodes_at_level = [n for n in levels if levels[n] == level]
        if nodes_at_level:
            x_positions = [pos[n][0] for n in nodes_at_level]
            plt.hlines((max_level - level) * vertical_spacing, 
                      min(x_positions)-0.5, 
                      max(x_positions)+0.5, 
                      colors='gray', 
                      linestyles='dashed', 
                      alpha=0.3)

    plt.title("Иерархическая структура ST-файла", fontsize=12)
    plt.axis('off')
    
    # Вместо tight_layout используем adjust
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    
    plt.show()
    
def main():
    """
    Основная функция для запуска анализа ST-файла.
    """
    # Разбор файла с учетом кодировки "utf-8 BOM"
    file_content = read_file_with_bom("МоиШаблоны.st")
    
    # Проверка баланса скобок
    try:
        #check_braces_balance(file_content)
        print('проверка баланса скоб отключена')
    except ValueError as e:
        print(f"Ошибка в структуре файла: {e}")
        return

    input_stream = FileStream("МоиШаблоны.st", encoding="utf-8")
    lexer = STFileLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    '''
    эту реализацию визуализации отладки перенес отдельно в метод save_tokens_to_file()
    # Вывод всех токенов для отладки
    token_stream.fill()
    for token in token_stream.tokens:
        print(f"{token.line}:{token.column} {lexer.ruleNames[token.type - 1]} = '{token.text}'")
    parser = STFileParser(token_stream)
    '''
    # Вывод всех токенов для отладки
    # Заполняем поток токенов
    token_stream.fill()
    
    # Сохраняем токены в файл
    save_tokens_to_file(token_stream.tokens, lexer)
    print("Токены сохранены в файл tokens_output.txt")
    parser = STFileParser(token_stream)
    # Удаляем стандартный обработчик ошибок и добавляем наш
    parser.removeErrorListeners()
    info_listener = STFileInfoListener()
    parser.addErrorListener(info_listener)
    
    # Парсим файл
    try:
        tree = parser.fileStructure()
        
        
        # Проверка параметров шаблонов
        print("\nПроверка параметров шаблонов:")
        walker = ParseTreeWalker()
        walker.walk(info_listener, tree)
        print("Проверка завершена\n")
        
        # Вывод структуры в виде дерева
        #print("\nСтруктура файла:")
        pretty_listener = PrettyTreeListener()
        walker.walk(pretty_listener, tree)
        print(pretty_listener.get_pretty_tree())

        # Сохраняем структуру в файл
        pretty_listener.save_to_file("structure.txt")
        print("\nСтруктура сохранена в файл structure.txt")

        # Визуализация иерархии
        #visualize_hierarchy(parser, tree)

        # Выводим ошибки, если они есть
        errors = info_listener.get_errors()
        if errors:
            print("\nНайдены ошибки:")
            for error in errors:
                print(error)
        else:
            print("\nФайл успешно разобран без ошибок")
        
       

    except Exception as e:
        print(f"Ошибка при разборе: {str(e)}")

if __name__ == "__main__":
    main()