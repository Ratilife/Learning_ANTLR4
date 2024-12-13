from antlr4 import Parser

class CSharpPreprocessorParserBase(Parser):
    def __init__(self, input, output=None, errorOutput=None):
        super().__init__(input, output, errorOutput)
        self.conditions = [True]
        self.conditional_symbols = {"DEBUG"}

    def all_conditions(self):
        return all(self.conditions)

    def on_preprocessor_directive_define(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_declaration', None)
        if d:
            self.conditional_symbols.add(d.CONDITIONAL_SYMBOL().getText())
            d.value = self.all_conditions()

    def on_preprocessor_directive_undef(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_declaration', None)
        if d:
            self.conditional_symbols.discard(d.CONDITIONAL_SYMBOL().getText())
            d.value = self.all_conditions()

    def on_preprocessor_directive_if(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_conditional', None)
        if d:
            d.value = d.expr.value == "true" and self.all_conditions()
            self.conditions.append(d.expr.value == "true")

    def on_preprocessor_directive_elif(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_conditional', None)
        if d:
            if not self.conditions[-1]:
                self.conditions.pop()
                d.value = d.expr.value == "true" and self.all_conditions()
                self.conditions.append(d.expr.value == "true")
            else:
                d.value = False

    def on_preprocessor_directive_else(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_conditional', None)
        if d:
            if not self.conditions[-1]:
                self.conditions.pop()
                d.value = True and self.all_conditions()
                self.conditions.append(True)
            else:
                d.value = False

    def on_preprocessor_directive_endif(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_conditional', None)
        if d:
            self.conditions.pop()
            d.value = self.conditions[-1]

    def on_preprocessor_directive_line(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_line', None)
        if d:
            d.value = self.all_conditions()

    def on_preprocessor_directive_error(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_diagnostic', None)
        if d:
            d.value = self.all_conditions()

    def on_preprocessor_directive_warning(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_diagnostic', None)
        if d:
            d.value = self.all_conditions()

    def on_preprocessor_directive_region(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_region', None)
        if d:
            d.value = self.all_conditions()

    def on_preprocessor_directive_endregion(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_region', None)
        if d:
            d.value = self.all_conditions()

    def on_preprocessor_directive_pragma(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_pragma', None)
        if d:
            d.value = self.all_conditions()

    def on_preprocessor_directive_nullable(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_nullable', None)
        if d:
            d.value = self.all_conditions()

    def on_preprocessor_expression_true(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_expression', None)
        if d:
            d.value = "true"

    def on_preprocessor_expression_false(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_expression', None)
        if d:
            d.value = "false"

    def on_preprocessor_expression_conditional_symbol(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_expression', None)
        if d:
            d.value = "true" if d.CONDITIONAL_SYMBOL().getText() in self.conditional_symbols else "false"

    def on_preprocessor_expression_conditional_open_parens(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_expression', None)
        if d:
            d.value = d.expr.value

    def on_preprocessor_expression_conditional_bang(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_expression', None)
        if d:
            d.value = "false" if d.expr.value == "true" else "true"

    def on_preprocessor_expression_conditional_eq(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_expression', None)
        if d:
            d.value = "true" if d.expr1.value == d.expr2.value else "false"

    def on_preprocessor_expression_conditional_ne(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_expression', None)
        if d:
            d.value = "true" if d.expr1.value != d.expr2.value else "false"

    def on_preprocessor_expression_conditional_and(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_expression', None)
        if d:
            d.value = "true" if d.expr1.value == "true" and d.expr2.value == "true" else "false"

    def on_preprocessor_expression_conditional_or(self):
        ctx = self._ctx
        d = getattr(ctx, 'preprocessor_expression', None)
        if d:
            d.value = "true" if d.expr1.value == "true" or d.expr2.value == "true" else "false"
