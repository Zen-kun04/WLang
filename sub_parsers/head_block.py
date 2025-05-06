from sub_parsers.meta.author import AuthorParser
from sub_parsers.meta.description import DescriptionParser
from sub_parsers.meta.keywords import KeywordsParser
from sub_parsers.meta.language import LanguageParser
from sub_parsers.title import TitleParser
from utils.classes import Parser


class HeadBlockParser:
    def __init__(self, parser: Parser, source_file: str):
        self.source_file = source_file
        self.ast = []

        while parser.current_token(source_file) and parser.current_token(source_file).type != "RBRACE":
            if parser.current_token(source_file).type == "IDENTIFIER":
                identifier = parser.consume(source_file, "IDENTIFIER")
                assert identifier.value == "page"
                parser.consume(source_file, "DOT")
                if parser.current_token(source_file).value == "setTitle":
                    self.ast.append(TitleParser(parser, source_file).html())
                    continue
                if parser.current_token(source_file).value == "setLang":
                    LanguageParser(parser, source_file)
                    continue
                if parser.current_token(source_file).value == "setDescription":
                    self.ast.append(DescriptionParser(parser, source_file).html())
                    continue
                if parser.current_token(source_file).value == "setAuthor":
                    self.ast.append(AuthorParser(parser, source_file).html())
                    continue
                if parser.current_token(source_file).value == "setKeywords":
                    self.ast.append(KeywordsParser(parser, source_file).html())
                    continue
                    

            raise Exception(f"Unregistered token: '{parser.current_token(source_file).value}' of type {parser.current_token(source_file).type}") 
        parser.consume(source_file, "RBRACE")

    def html(self):
        return ''.join(self.ast)

    def __repr__(self):
        return f"<h{self.level}>{self.value.value}</h{self.level}>"