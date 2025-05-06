class Token:
    def __init__(self, type_: str, value: str):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token(type={self.type}, value={self.value})"

class Lexer:
    def __init__(self):
        self.source_code = {}

class Parser:
    def __init__(self):
        self.positions = {}
        self.source_tokens = {}
        self.language = "en"
        self.directory = "."
        self.components = {}

    def peek(self, file: str):
        if self.positions.get(file, 0) + 1 < len(self.source_tokens[file]):
            return self.source_tokens[file][self.positions.get(file, 0) + 1]
        return None
    
    def current_token(self, file: str):
        if self.positions.get(file, 0) < len(self.source_tokens[file]):
            return self.source_tokens[file][self.positions.get(file, 0)]
        return None

    def consume(self, file: str, *types):
        token = self.current_token(file)
        if not token:
            raise Exception(f"Error: Unexpected error of input. Expected {','.join(types)}")
        if token.type not in types:
            raise Exception(f"Error: Token {token.value} is of type {token.type} but {','.join(types)} is required")
        self.positions[file] = self.positions.get(file, 0) + 1
        return token