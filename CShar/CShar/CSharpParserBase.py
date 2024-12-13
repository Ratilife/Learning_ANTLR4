from antlr4 import Parser

class CSharpParserBase(Parser):
    def __init__(self, input, output=None, errorOutput=None):
        super().__init__(input, output, errorOutput)

    def is_local_variable_declaration(self):
        """
        Проверяет, является ли текущий контекст локальным объявлением переменной.
        """
        local_var_decl = getattr(self._ctx, 'local_variable_declaration', None)
        if local_var_decl is None:
            return True

        local_variable_type = local_var_decl.local_variable_type()
        if local_variable_type is None:
            return True

        if local_variable_type.getText() == "var":
            return False

        return True
