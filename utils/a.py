from os import listdir
from os.path import isdir, join

from utils.classes import Lexer

def scan(lexer: Lexer, path: str = '.'):
    for file in listdir(path):
        if not isdir(join(path, file)) and file.endswith('.wl'):
            with open(join(path, file)) as f:
                content = f.read()
                if not content:
                    continue
                lexer.source_code[join(path, file)] = content
        elif isdir(join(path, file)):
            scan(lexer, path=join(path, file))


base = """<!DOCTYPE html><html lang="[lang]"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">[head]</head><body><main>[body]</main></body>[footer]</html>"""