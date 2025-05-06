from utils.classes import Token, Parser


reserved = {
    "const": "KEYWORD",
    "paragraph": "N_FUNC",
    "p": "N_FUNC",
    "heading1": "N_FUNC",
    "h1": "N_FUNC",
    "heading2": "N_FUNC",
    "h2": "N_FUNC",
    "heading3": "N_FUNC",
    "h3": "N_FUNC",
    "heading4": "N_FUNC",
    "h4": "N_FUNC",
    "heading5": "N_FUNC",
    "h5": "N_FUNC",
    "heading6": "N_FUNC",
    "h6": "N_FUNC",
    "head": "N_FUNC",
    "main": "N_FUNC",
    "footer": "N_FUNC",
    "url": "N_FUNC",
    "true": "BOOLEAN",
    "false": "BOOLEAN",
    "if": "KEYWORD",
    "comp": "KEYWORD",
    "null": "KEYWORD",
    '"': "DOUBLE_QUOTE",
    "'": "SINGLE_QUOTE",
    ".": "DOT",
    ",": "COMMA",
    ";": "SEMICOLON",
    "(": "LPAREN",
    ")": "RPAREN",
    "{": "LBRACE",
    "}": "RBRACE",
    "[": "LBRACK",
    "]": "RBRACK",
    "+": "PLUS",
    "-": "MINUS",
    "*": "STAR",
    "/": "SLASH",
    "<": "LOWER",
    ">": "HIGHER",
    "=": "ASSIGN",
    "!": "NOT",
    "<=": "LEQ",
    ">=": "HEQ",
    "==": "EQ",
    "!=": "NEQ",
}

def peek(pos: int, code: str):
    if pos + 1 < len(code):
        return code[pos + 1]
    return None

def tokenize(code: str, source_file: str, parser: Parser):
    pos = 0
    tokens = []
    quoted = None
    word = ""
    while pos < len(code):
        char = str(code[pos])
        if char in ('"', "'"):
            if char == quoted:
                quoted = False
                tokens.append(Token("STRING", word))
                word = ""
            elif not quoted:
                quoted = char
            else:
                word += char
            pos += 1
            continue

        if char.isalpha() and not quoted:
            word = ""
            while pos < len(code) and code[pos].isalnum():
                word += code[pos]
                pos += 1
            if word in reserved:
                tokens.append(Token(reserved[word], word))
            else:
                tokens.append(Token("IDENTIFIER", word))
            word = ""
            continue

        if quoted and char == '\n':
            raise Exception(f"Error: String not closed")
        
        if not quoted and char in ('\n', ' '):
            pos += 1
            continue
        
        if char == '/' and peek(pos, code) == '/' and not quoted:
            while pos < len(code) and code[pos] != '\n':
                pos += 1
            continue
            

        if quoted and char != quoted:
            word += char
            pos += 1
            continue

        if char.isdigit():
            digits = ""
            while pos < len(code) and code[pos].isdigit():
                digits += code[pos]
                pos += 1
            tokens.append(Token("DIGIT", int(digits)))
            continue
        
        if char in reserved:
            p = peek(pos, code)
            if p and char+p in reserved:
                tokens.append(Token(reserved[char+p], char+p))
                pos += 2
            else:
                tokens.append(Token(reserved[char], char))
                pos += 1
            word = ""
            continue
        raise Exception(f"Error: Unknown token: '{char}'")
    parser.source_tokens[source_file] = tokens