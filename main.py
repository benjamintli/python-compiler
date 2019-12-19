from src.lexer import Lexer
from src.parser import Parser
from src.codegen import CodeGen
import sys


if __name__ == "__main__":
    input_code_path = sys.argv[1]
    output_file_path = sys.argv[2]
    with open(input_code_path) as f:
        text_input = f.readlines()


    lexer = Lexer().get_lexer()
    tokens_1 = lexer.lex(text_input[0])

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