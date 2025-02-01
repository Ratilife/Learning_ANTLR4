from graphviz import Digraph
from antlr4 import *
from CShar.CSharpLexer import CSharpLexer
from CShar.CSharpParser import CSharpParser

# Функция для безопасного создания имени узла
def sanitize_text(text):
    """Заменяет недопустимые символы в тексте узла."""
    if not text.strip():
        text = "EMPTY"  # Для узлов с пустым текстом
    return text.replace('"', "'").replace("{", "").replace("}", "").replace(" ", "_")

# Рекурсивное создание дерева
def visit_tree(node, graph, parent_name=None):
    if node is None:
        return

    # Уникальное имя узла
    node_text = sanitize_text(node.getText())
    node_name = f"node_{id(node)}"
    graph.node(node_name, label=node_text)

    # Связь с родителем
    if parent_name:
        graph.edge(parent_name, node_name)

    # Рекурсивный обход дочерних узлов
    for i in range(node.getChildCount()):
        visit_tree(node.getChild(i), graph, node_name)

# Чтение C#-кода
input_stream = FileStream("C#Example.cs", encoding="utf-8")
lexer = CSharpLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = CSharpParser(token_stream)
tree = parser.compilation_unit()
'''
try:
    with open("C#Example.cs", "r", encoding="utf-8") as file:
        code = file.read()
except UnicodeDecodeError:
    print("Ошибка: Не удалось декодировать файл. Проверьте кодировку файла.")
    exit(1)

# Создание потока ввода для ANTLR
input_stream = InputStream(code)
lexer = CSharpLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = CSharpParser(token_stream)
tree = parser.compilation_unit()
'''
# Создание графа
graph = Digraph(format="png", graph_attr={"rankdir": "TB"})
visit_tree(tree, graph)

# Сохранение дерева
output_path = graph.render("parse_tree")
print(f"Дерево сохранено как '{output_path}'")
