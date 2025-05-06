from sub_parsers.block import BlockParser
from utils.classes import Parser


class CompParser:
    def __init__(self, parser: Parser, source_file: str):
        self.source_file = source_file
        parser.consume(source_file, "LBRACE")
        self.code = BlockParser(parser, source_file).html()
        
    def html(self):
        return self.code

    def __repr__(self):
        return f"<h{self.level}>{self.value.value}</h{self.level}>"