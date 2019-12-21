from .parser import Parser
from .lexer import Lexer
from .codegen import CodeGen
import os

def compile(input_code, output_file_path, file=True):
    if file:
        # input code is a file,
        with open(input_code) as f:
           text_input = f.read()
    else:
        # input code is a string
        text_input = input_code

    lexer = Lexer().get_lexer()
    tokens_1 = lexer.lex(text_input)

    codegen = CodeGen()

    module = codegen.module
    builder = codegen.builder
    printf = codegen.printf

    pg = Parser(module, builder, printf)
    pg.parse()
    parser = pg.get_parser()
    parser.parse(tokens_1).eval()

    codegen.create_ir()
    codegen.save_ir(output_file_path)