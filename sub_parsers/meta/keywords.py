from utils.classes import Parser


class KeywordsParser:
    def __init__(self, parser: Parser, source_file: str):
        self.source_file = source_file
        self.method = parser.consume(source_file, "IDENTIFIER")
        assert self.method.value == "setKeywords"
        parser.consume(source_file, "LPAREN")
        self.keywords = []
        while parser.current_token(source_file) and parser.current_token(source_file).type != "RPAREN":
            self.keyword = parser.consume(source_file, "STRING")
            if parser.current_token(source_file).type != "RPAREN":
                parser.consume(source_file, "COMMA")
            if self.keyword not in self.keywords:
                self.keywords.append(self.keyword)

        parser.consume(source_file, "RPAREN")
        parser.consume(source_file, "SEMICOLON")
    
    def html(self):
        return f"<meta name=\"keywords\" content=\"{', '.join(keyword.value for keyword in self.keywords)}\">"
        
    def __repr__(self):
        return ""