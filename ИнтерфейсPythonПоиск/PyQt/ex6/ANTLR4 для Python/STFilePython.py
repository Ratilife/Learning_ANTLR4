import networkx as nx
import matplotlib.pyplot as plt
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker, DiagnosticErrorListener
from ANTLR4.STFileLexer import STFileLexer
from ANTLR4.STFileParser import STFileParser
from antlr4.tree.Tree import TerminalNodeImpl, ParseTreeListener

# Функция для обработки кодировки "utf-8 BOM"
def read_file_with_bom(file_path):
    with open(file_path, "rb") as file:
        raw_data = file.read()
        if raw_data.startswith(b"\xef\xbb\xbf"):  # Проверяем наличие BOM
            return raw_data.decode("utf-8-sig")  # Используем utf-8-sig для удаления BOM
        return raw_data.decode("utf-8")  # Иначе используем обычный utf-8

# Разбор файла с учетом кодировки "utf-8 BOM"
file_content = read_file_with_bom("МоиШаблоны.st")
input_stream = FileStream("МоиШаблоны.st", encoding="utf-8")
lexer = STFileLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = STFileParser(token_stream)
parser.addErrorListener(DiagnosticErrorListener())  # Включаем диагностику
tree = parser.fileStructure()  # Начинаем разбор с корневого правила

# Граф для визуализации
G = nx.DiGraph()

# Класс для обхода дерева и добавления узлов
class TreeGraphListener(ParseTreeListener):
    def __init__(self):
        self.node_id = 0
        self.edges = []
    
    def enterEveryRule(self, ctx):
        node_label = parser.ruleNames[ctx.getRuleIndex()]
        G.add_node(self.node_id, label=node_label)
        if ctx.parentCtx:
            parent_id = ctx.parentCtx.node_id
            self.edges.append((parent_id, self.node_id))
        ctx.node_id = self.node_id
        self.node_id += 1

    def visitTerminal(self, node: TerminalNodeImpl):
        G.add_node(self.node_id, label=node.getText())
        G.add_edge(node.parentCtx.node_id, self.node_id)
        self.node_id += 1

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
