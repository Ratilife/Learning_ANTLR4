from antlr4 import *
from ANTLR4.STFileListener import STFileListener
from ANTLR4.STFileParser import STFileParser

class STFileInfoListener(STFileListener):
    def __init__(self):
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
    
    def exitEveryRule(self, ctx):
        self.indent -= 1
        self.current_rule = None
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Line {line}:{column} - правило: {self.current_rule or 'unknown'} - ошибка: {msg}"
        self.error_messages.append(error_msg)
        print(error_msg)
        
        # Получаем текст строки с ошибкой
        input_stream = recognizer.getInputStream()
        if input_stream:
            lines = input_stream.strdata.split('\n')
            if line > 0 and line <= len(lines):
                error_line = lines[line-1]
                print(error_line)
                print(" " * (column) + "^")
    
    def get_errors(self):
        return self.error_messages