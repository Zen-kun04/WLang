from sub_parsers.comp import CompParser
from sub_parsers.footer import FooterParser
from sub_parsers.head import HeadParser
from sub_parsers.main import MainParser
from utils.classes import Parser
from utils.a import base
from os import makedirs


def parse(parser: Parser, source_file: str):
    head_ast = []
    body_ast = []
    footer_ast = []
    head = False
    main = False
    footer = False

    while parser.current_token(source_file):
        if parser.current_token(source_file).type == "N_FUNC":
            if parser.current_token(source_file).value == "head":
                if head:
                    raise Exception("Error: head function is already declared!")
                head = True
                head_ast.append(HeadParser(parser, source_file).html())
                continue

            if parser.current_token(source_file).value == "main":
                if main:
                    raise Exception("Error: main function is already declared!")
                main = True
                body_ast.append(MainParser(parser, source_file).html())
                continue
            
            if parser.current_token(source_file).value == "footer":
                if footer:
                    raise Exception("Error: footer function is already declared!")
                footer = True
                footer_ast.append(FooterParser(parser, source_file).html())
                continue
        if parser.current_token(source_file).type == "KEYWORD":
            if parser.current_token(source_file).value == "comp":
                parser.consume(source_file, "KEYWORD")
                component_name = parser.consume(source_file, "IDENTIFIER").value
                if component_name in parser.components:
                    raise Exception(f"Error: the component \"{component_name}\" already exists!")
                parser.components[component_name] = CompParser(parser, source_file).html()
                continue

        raise Exception(f"Unregistered token: '{parser.current_token(source_file).value}' of type {parser.current_token(source_file).type}") 
    
    makedirs("out\\" + source_file.split(parser.directory, 1)[1].rsplit('\\', 1) [0], exist_ok=True)
    with open("out\\" + source_file.split(parser.directory, 1)[1].rsplit('.', 1)[0] + ".html", 'w') as f:
        code = base.replace('[lang]', parser.language).replace("[head]", ''.join(head_ast)).replace("[body]", ''.join(body_ast)).replace("[footer]", f"""<footer>
{''.join(footer_ast)}
</footer>""" if footer_ast else "")
        f.write(f"{code}<!-- Made with <3 using WLang -->")