from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
    
    def _add_tokens(self):
        self.lexer.add('PRINT', r'print')
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        self.lexer.add('SEMI_COLON', r'\;')
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')
        self.lexer.add('MOD', r'\%')
        self.lexer.add('OR', r'\|')
        self.lexer.add('AND', r'\&')
        self.lexer.add('XOR', r'\^')
        self.lexer.add('<=', r'\<=')
        self.lexer.add('>=', r'\>=')
        self.lexer.add('==', r'\==')
        self.lexer.add('!=', r'\!=')
        self.lexer.add('SHL', r'\<<')
        self.lexer.add('LSHR', r'\>>')
        self.lexer.add('<', r'\<')
        self.lexer.add('>', r'\>')
        self.lexer.ignore('\s+')


        