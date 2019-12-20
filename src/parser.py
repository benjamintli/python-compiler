from rply import ParserGenerator
from .ast import Number, Sum, Sub, Print, Mul, Div, Mod, Or, And, Xor, Comparison


class Parser():
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'MUL', 'DIV', 'MOD', 'AND', 'OR', 'XOR', "<", ">", "<=", ">=", "==", "!="],
            precedence=[("left", ["MOD", "DIV", "MUL", "SUM", "SUB", "AND", "OR", "XOR", "<", ">", "<=", ">=", "==", "!="])]
        )
        self.module = module
        self.builder = builder
        self.printf = printf
        self.comparison_list = ["<", ">", "<=", ">=", "==", "!="]

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(self.builder, self.module, self.printf, p[2])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression MOD expression')
        @self.pg.production('expression : expression OR expression')
        @self.pg.production('expression : expression AND expression')
        @self.pg.production('expression : expression XOR expression')
        @self.pg.production('expression : expression > expression')
        @self.pg.production('expression : expression < expression')
        @self.pg.production('expression : expression >= expression')
        @self.pg.production('expression : expression <= expression')
        @self.pg.production('expression : expression == expression')
        @self.pg.production('expression : expression != expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'MOD':
                return Mod(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'OR':
                return Or(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'AND':
                return And(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'XOR':
                return Xor(self.builder, self.module, left, right)
            elif operator.gettokentype() in self.comparison_list:
                return Comparison(self.builder, self.module, left, right, operator.gettokentype())

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(self.builder, self.module, p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()