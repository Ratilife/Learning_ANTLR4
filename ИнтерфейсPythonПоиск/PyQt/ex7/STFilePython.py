import networkx as nx
import matplotlib.pyplot as plt
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker, DiagnosticErrorListener
from ANTLR4.STFileLexer import STFileLexer
from ANTLR4.STFileParser import STFileParser
from antlr4.tree.Tree import TerminalNodeImpl, ParseTreeListener
from STFileCustomListener import STFileCustomListener

class STFileInfoListener(STFileCustomListener):
    def __init__(self):
        super().__init__()
        self.indent = 0
        self.current_rule = None
        self.error_messages = []
    
    def get_indent(self):
        return "  " * self.indent
    
    def enterEveryRule(self, ctx):
        rule_name = STFileParser.ruleNames[ctx.getRuleIndex()]
        self.current_rule = rule_name
        text = ctx.getText().replace("\n", "\\n").replace("\r", "\\r")
        if len(text) > 50:
            text = text[:47] + "..."
        print(f"{self.get_indent()}{text} - правило: {rule_name}")
        self.indent += 1
        super().enterEveryRule(ctx)
    
    def exitEveryRule(self, ctx):
        self.indent -= 1
        self.current_rule = None
        super().exitEveryRule(ctx)
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
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
        return self.error_messages

class TreeGraphListener(ParseTreeListener):
    def __init__(self, graph, parser):
        self.node_id = 0
        self.edges = []
        self.G = graph
        self.parser = parser
    
    def enterEveryRule(self, ctx):
        node_label = self.parser.ruleNames[ctx.getRuleIndex()]
        self.G.add_node(self.node_id, label=node_label)
        if hasattr(ctx, 'parentCtx') and ctx.parentCtx:
            parent_id = ctx.parentCtx.node_id
            self.edges.append((parent_id, self.node_id))
        ctx.node_id = self.node_id
        self.node_id += 1

    def visitTerminal(self, node: TerminalNodeImpl):
        label = node.getText().replace('\t', '\\t').replace('\r', '\\r').replace('\n', '\\n')
        self.G.add_node(self.node_id, label=label)
        if hasattr(node, 'parentCtx') and node.parentCtx:
            self.G.add_edge(node.parentCtx.node_id, self.node_id)
        self.node_id += 1

def read_file_with_bom(file_path):
    with open(file_path, "rb") as file:
        raw_data = file.read()
        if raw_data.startswith(b"\xef\xbb\xbf"):
            return raw_data.decode("utf-8-sig")
        return raw_data.decode("utf-8")

def check_braces_balance(file_content):
    stack = []
    for i, char in enumerate(file_content):
        if char == '{':
            stack.append(i)
        elif char == '}':
            if not stack:
                raise ValueError(f"Лишняя закрывающая скобка в позиции {i}")
            stack.pop()

    if stack:
        raise ValueError(f"Не хватает {len(stack)} закрывающих скобок. Открывающие скобки в позициях: {stack}")
    else:
        print("Скобки сбалансированы.")

def main():
    # Разбор файла с учетом кодировки "utf-8 BOM"
    file_content = read_file_with_bom("Новый2.st")
    
    # Проверка баланса скобок
    try:
        check_braces_balance(file_content)
    except ValueError as e:
        print(f"Ошибка в структуре файла: {e}")
        return

    input_stream = FileStream("Новый2.st", encoding="utf-8")
    lexer = STFileLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Вывод всех токенов для отладки
    token_stream.fill()
    for token in token_stream.tokens:
        print(f"{token.line}:{token.column} {lexer.ruleNames[token.type - 1]} = '{token.text}'")
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
        
        # Выводим ошибки, если они есть
        errors = info_listener.get_errors()
        if errors:
            print("\nНайдены ошибки:")
            for error in errors:
                print(error)
        else:
            print("\nФайл успешно разобран без ошибок")
            
        # Визуализация графа
        G = nx.DiGraph()
        graph_listener = TreeGraphListener(G, parser)
        walker.walk(graph_listener, tree)
        G.add_edges_from(graph_listener.edges)
        
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G)
        labels = nx.get_node_attributes(G, 'label')
        nx.draw(G, pos, with_labels=True, labels=labels, 
               node_size=3000, node_color="lightblue", font_size=10)
        plt.show()
        
    except Exception as e:
        print(f"Ошибка при разборе: {str(e)}")

if __name__ == "__main__":
    main()