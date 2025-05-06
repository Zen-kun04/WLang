from utils.classes import Parser


class AuthorParser:
    def __init__(self, parser: Parser, source_file: str):
        self.source_file = source_file
        self.method = parser.consume(source_file, "IDENTIFIER")
        assert self.method.value == "setAuthor"
        parser.consume(source_file, "LPAREN")
        self.value = parser.consume(source_file, "STRING")
        parser.consume(source_file, "RPAREN")
        parser.consume(source_file, "SEMICOLON")
    
    def html(self):
        return f"<meta name=\"author\" content=\"{self.value.value}\">"
        
    def __repr__(self):
        return ""