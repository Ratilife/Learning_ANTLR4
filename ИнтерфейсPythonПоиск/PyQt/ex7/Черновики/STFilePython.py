import networkx as nx
import matplotlib.pyplot as plt
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker, DiagnosticErrorListener
from ANTLR4.STFileLexer import STFileLexer
from ANTLR4.STFileParser import STFileParser
from antlr4.tree.Tree import TerminalNodeImpl, ParseTreeListener


from STFileCustomListener import STFileCustomListener

# Класс для обхода дерева и добавления узлов
class TreeGraphListener(ParseTreeListener):
    def __init__(self,graph, parser):
        self.node_id = 0
        self.edges = []
        self.G = graph  # Сохраняем граф в поле класса
        self.parser = parser  # Сохраняем parser
    
    def enterEveryRule(self, ctx):
        node_label = self.parser.ruleNames[ctx.getRuleIndex()]  # Используем self.parser
        self.G.add_node(self.node_id, label=node_label)  # Используем self.G вместо глобальной G
        if ctx.parentCtx:
            parent_id = ctx.parentCtx.node_id
            self.edges.append((parent_id, self.node_id))
        ctx.node_id = self.node_id
        self.node_id += 1

    def visitTerminal(self, node: TerminalNodeImpl):
        label = node.getText()
        # Заменяем спецсимволы на читаемые аналоги
        label = label.replace('\t', '\\t').replace('\r', '\\r').replace('\n', '\\n')
        self.G.add_node(self.node_id, label=label)
        self.G.add_edge(node.parentCtx.node_id, self.node_id)
        self.node_id += 1
        #self.G.add_node(self.node_id, label=node.getText())
        #self.G.add_edge(node.parentCtx.node_id, self.node_id)
        #self.node_id += 1

# Функция для обработки кодировки "utf-8 BOM"
def read_file_with_bom(file_path):
    with open(file_path, "rb") as file:
        raw_data = file.read()
        if raw_data.startswith(b"\xef\xbb\xbf"):  # Проверяем наличие BOM
            return raw_data.decode("utf-8-sig")  # Используем utf-8-sig для удаления BOM
        return raw_data.decode("utf-8")  # Иначе используем обычный utf-8


def check_braces_balance(file_content):
    stack = []
    for i, char in enumerate(file_content):
        if char == '{':
            stack.append(i)  # Сохраняем индекс открывающей скобки
        elif char == '}':
            if not stack:
                raise ValueError(f"Лишняя закрывающая скобка в позиции {i}")
            stack.pop()  # Удаляем последнюю открывающую скобку из стека

    if stack:
        raise ValueError(f"Не хватает {len(stack)} закрывающих скобок. Открывающие скобки в позициях: {stack}")
    else:
        print("Скобки сбалансированы.")


# Разбор файла с учетом кодировки "utf-8 BOM"
file_content = read_file_with_bom("Новый1.st")
# Проверка баланса скобок
try:
    check_braces_balance(file_content)
except ValueError as e:
    print(f"Ошибка в структуре файла: {e}")
    # Здесь можно добавить логику для исправления файла или завершения программы
else:
    input_stream = FileStream("Новый1.st", encoding="utf-8")
    lexer = STFileLexer(input_stream)

    token_stream = CommonTokenStream(lexer)
    parser = STFileParser(token_stream)
    parser.addErrorListener(DiagnosticErrorListener())  # Включаем диагностику
    tree = parser.fileStructure()  # Начинаем разбор с корневого правила

    # Проверка параметров шаблонов
    print("\nПроверка параметров шаблонов:")
    param_checker = STFileCustomListener()
    walker = ParseTreeWalker()
    walker.walk(param_checker, tree)
    print("Проверка завершена\n")


# Граф для визуализации
G = nx.DiGraph()  # Создаём граф ДО использования
walker = ParseTreeWalker()  
listener = TreeGraphListener(G, parser)     # Передаём и граф, и парсер в конструктор
walker.walk(listener, tree)
G.add_edges_from(listener.edges) # Добавляем рёбра
    
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
labels = nx.get_node_attributes(G, 'label')
nx.draw(G, pos, with_labels=True, labels=labels, node_size=3000, node_color="lightblue", font_size=10)
plt.show()

'''
# Проходим по дереву
walker = ParseTreeWalker()
listener = TreeGraphListener()
walker.walk(listener, tree)

# Добавляем связи
G.add_edges_from(listener.edges)

# Визуализация
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
labels = nx.get_node_attributes(G, 'label')
nx.draw(G, pos, with_labels=True, labels=labels, node_size=3000, node_color="lightblue", font_size=10)
plt.show()
'''