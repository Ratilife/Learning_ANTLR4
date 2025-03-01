from antlr4 import *
from CSharNew.CSharpLexer import CSharpLexer
from CSharNew.CSharpParser  import CSharpParser 
from CSharNew.CSharpPreprocessorParser  import CSharpPreprocessorParser 

preprocessor_input = FileStream("C#Example.cs", encoding="utf-8")
preprocessor_lexer = CSharpPreprocessorLexer(preprocessor_input)
preprocessor_tokens = CommonTokenStream(preprocessor_lexer)
preprocessor_parser = CSharpPreprocessorParser(preprocessor_tokens)
preprocessed_tree = preprocessor_parser.compilation_unit()
# ... дальше работа с preprocessed_tree (возможно, трансформация в другой поток токенов)

