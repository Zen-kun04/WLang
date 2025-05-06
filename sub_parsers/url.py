from utils.classes import Parser

targets = {
    "new_page": "_blank",
    "current_page": "_self",
}

relations = [
    "alternate",
    "author",
    "bookmark",
    "external",
    "help",
    "license",
    "next",
    "nofollow",
    "noreferrer",
    "noopener",
    "prev",
    "search",
    "tag"
]

class UrlParser:
    def __init__(self, parser: Parser, source_file: str):
        self.source_file = source_file
        self.method = parser.consume(source_file, "N_FUNC")
        assert self.method.value == "url"
        parser.consume(source_file, "LPAREN")
        self.url = parser.consume(source_file, "STRING")
        parser.consume(source_file, "COMMA")
        self.text = parser.consume(source_file, "STRING")
        self.target = None
        self.relation = None
        self.ping = []
        self.destinationLanguage = None
        self.download = False
        if parser.current_token(source_file).type == "COMMA":
            parser.consume(source_file, "COMMA")
            parser.consume(source_file, "LBRACK")
            while parser.current_token(source_file) and parser.current_token(source_file).type != "RBRACK":
                self.method2 = parser.consume(source_file, "IDENTIFIER")
                assert self.method2.value in ("Target", "Relation", "Ping", "DestinationLang", "Download")
                parser.consume(source_file, "LPAREN")
                if self.method2.value == "Target":
                    self.target = parser.consume(source_file, "STRING")
                    assert self.target.value in targets
                elif self.method2.value == "Relation":
                    self.relation = parser.consume(source_file, "STRING")
                    assert self.relation.value in relations
                elif self.method2.value == "Ping":
                    while parser.current_token(source_file) and parser.current_token(source_file).type != "RPAREN":
                        self.ping.append(parser.consume(source_file, "STRING"))
                        if parser.current_token(source_file).type != "RPAREN":
                            parser.consume(source_file, "COMMA")
                elif self.method2.value == "DestinationLang":
                    self.destinationLanguage = parser.consume(source_file, "STRING")
                elif self.method2.value == "Download":
                    boolean = parser.consume(source_file, "BOOLEAN").value
                    self.download = boolean == "true"
                
                parser.consume(source_file, "RPAREN")
                if parser.current_token(source_file).type != "RBRACK":
                    parser.consume(source_file, "COMMA")
                
        if parser.current_token(source_file).type == "RBRACK":    
            parser.consume(source_file, "RBRACK")
        parser.consume(source_file, "RPAREN")
        parser.consume(source_file, "SEMICOLON")

    def html(self):
        return f"<a href=\"{self.url.value}\"{f' target=\"{targets[self.target.value]}\"' if self.target else ''}{f' rel=\"{self.relation.value}\"' if self.relation else ''}{f' ping=\"{' '.join(ping.value for ping in self.ping)}\"' if self.ping else ''}{f' hreflang=\"{self.destinationLanguage.value}\"' if self.destinationLanguage else ''}{f' download' if self.download else ''}>{self.text.value}</a>"

    def __repr__(self):
        return f"<a href=\"{self.url.value}\">{self.text.value}</a>"
