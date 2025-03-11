import networkx as nx
import matplotlib.pyplot as plt
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from ANTLR4.STFileLexer import STFileLexer
from ANTLR4.STFileParser import STFileParser
from antlr4.tree.Tree import TerminalNodeImpl, ParseTreeListener

# Разбор файла
input_stream = FileStream("МоиШаблоны.st", encoding="utf-8")
lexer = STFileLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = STFileParser(token_stream)
tree = parser.fileStructure()

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
