from antlr4 import *
from CSharNew.CSharpLexer import CSharpLexer
from CSharNew.CSharpParser  import CSharpParser 
from CSharNew.CSharpPreprocessorParser  import CSharpPreprocessorParser 
from CSharNew.CSharpPreprocessorLexer import CSharpPreprocessorLexer
from graphviz import Digraph

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

# Предварительная обработка
preprocessor_lexer = CSharpPreprocessorLexer(input_stream)
preprocessor_tokens = CommonTokenStream(preprocessor_lexer)
preprocessor_parser = CSharpPreprocessorParser(preprocessor_tokens)
preprocessed_tree = preprocessor_parser.compilation_unit()

# Создание нового потока токенов для основного парсера
input_stream.seek(0)  # Вернуться к началу файла для повторного чтения
lexer = CSharpLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = CSharpParser(token_stream)
tree = parser.compilation_unit()    # Получаем синтаксическое дерево

# Создание графа
graph = Digraph(format="png", graph_attr={"rankdir": "TB"})

# Обход дерева разбора
visit_tree(preprocessed_tree, graph)

# Сохранение дерева
output_path = graph.render("preprocessed_parse_tree")
print(f"Дерево сохранено как '{output_path}'")
