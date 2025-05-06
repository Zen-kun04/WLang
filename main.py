from utils.a import scan
from utils.classes import Lexer, Parser
from lexer import tokenize
from parser import parse
from sys import argv
from os.path import isdir

if __name__ == "__main__":
    args = argv[1:]
    if not args:
        print("WLang version 0.0.3")
        print("GitHub: https://github.com/Zen-kun04/WLang")
    elif len(args) >= 1 and args[0] == "compile":
        lexer = Lexer()
        parser = Parser()
        if len(args) >= 2 and isdir(args[1]):
            parser.directory = args[1]
        
        print("Compiling sources...")
        scan(lexer, parser.directory)

        for source_file in lexer.source_code:
            tokenize(lexer.source_code[source_file], source_file, parser)
            parse(parser, source_file)
        print("Check the folder: out/")
    else:
        print("Unknown command:", args[0])