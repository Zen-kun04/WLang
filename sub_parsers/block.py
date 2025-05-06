from sub_parsers.heading import HeadingParser
from sub_parsers.paragraph import ParagraphParser
from sub_parsers.url import UrlParser
from utils.classes import Parser


class BlockParser:
    def __init__(self, parser: Parser, source_file: str):
        self.source_file = source_file
        self.ast = []
        heading1_registered = False
        past_heading = None
        
        while parser.current_token(source_file) and parser.current_token(source_file).type != "RBRACE":
            if parser.current_token(source_file).type == "N_FUNC":
                if parser.current_token(source_file).value in ("paragraph", "p"):
                    self.ast.append(ParagraphParser(parser, source_file).html())
                    continue

                if parser.current_token(source_file).value in ("heading1", "heading2", "heading3", "heading4", "heading5", "heading6", "h1", "h2", "h3", "h4", "h5", "h6"):
                    p = HeadingParser(parser, source_file)
                    if p.level == '1' and heading1_registered:
                        raise Exception(f"Error: heading1 (h1) is already registered in {source_file}. If you repeat it you will have a bad score!")
                    elif p.level == '1' and not heading1_registered:
                        heading1_registered = True
                    
                    if past_heading and past_heading not in (int(p.level), int(p.level) + 1, int(p.level) - 1):
                        raise Exception(f"Error: if you add multiple headings they have to be in order. Do not skip headings!")
                    else:
                        past_heading = int(p.level)
                    self.ast.append(p.html())
                    continue

                if parser.current_token(source_file).value == "url":
                    self.ast.append(UrlParser(parser, source_file).html())
                    continue

            if parser.current_token(source_file).type == "IDENTIFIER":
                    identifier = parser.consume(source_file, "IDENTIFIER").value
                    if identifier not in parser.components:
                        raise Exception(f"The component \"{identifier}\" does not exist!")
                    parser.consume(source_file, "SEMICOLON")
                    self.ast.append(parser.components[identifier])
                    continue

            raise Exception(f"Unregistered token: '{parser.current_token(source_file).value}' of type {parser.current_token(source_file).type}") 
        parser.consume(source_file, "RBRACE")

    def html(self):
        return ''.join(self.ast)

    def __repr__(self):
        return f"<h{self.level}>{self.value.value}</h{self.level}>"