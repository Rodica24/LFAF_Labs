import re

TOKEN = [
    (r"\s+", None),
    (r"\d+\.\d+|\d+", "Digit"),
    (r"[a-zA-Z]\w*", "Identifier"),
    (r"\+", "Addition"),
    (r"-", "Subtraction"),
    (r"\*", "Multiply"),
    (r"/", "Divide"),
    (r"=", "Equal"),
    (r"\(", "LeftP"),
    (r"\)", "RightP"),
]

class Lexer:
    def __init__(self, text):
        self.tokens = []
        self.text = text
        self.pos = 0

    def lexer(self):
        while self.pos < len(self.text):
            match = None
            for pattern, token_type in TOKEN:
                regex = re.compile(pattern)
                match = regex.match(self.text, self.pos)
                if match:
                    if token_type:
                        token = (match.group(), token_type)
                        self.tokens.append(token)
                    break
            if not match:
                raise Exception(f"Invalid token: {self.text[self.pos]}")
            else:
                self.pos = match.end()

        return self.tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        result = self.parse_expression()
        if self.pos != len(self.tokens):
            raise ValueError(f"Invalid syntax near token: {self.tokens[self.pos][0]}")
        return result

    def parse_expression(self):
        result = self.parse_term()
        while self.pos < len(self.tokens):
            if self.tokens[self.pos][1] == "Addition":
                self.pos += 1
                right = self.parse_term()
                result = ('OPERATOR', '+', result, right)
            elif self.tokens[self.pos][1] == "Subtraction":
                self.pos += 1
                right = self.parse_term()
                result = ('OPERATOR', '-', result, right)
            else:
                break
        return result

    def parse_term(self):
        result = self.parse_factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos][1] in ("Multiply", "Divide"):
            if self.tokens[self.pos][1] == "Multiply":
                self.pos += 1
                right = self.parse_factor()
                result = ('OPERATOR', '*', result, right)
            else:
                self.pos += 1
                right = self.parse_factor()
                result = ('OPERATOR', '/', result, right)
        return result

    def parse_factor(self):
        current_token = self.tokens[self.pos]
        token_type = current_token[1]

        if token_type == "Digit":
            result = ('DIGIT', current_token[0])
            self.pos += 1
            return result
        elif token_type == "Identifier":
            result = ('IDENTIFIER', current_token[0])
            self.pos += 1
            return result
        elif token_type == "Operator" and current_token[0] == "=":
            result = ('OPERATOR', '=', current_token[0])
            self.pos += 1
            return result
        elif token_type == "LeftP":
            self.pos += 1
            result = self.parse_expression()
            if self.tokens[self.pos][1] != "RightP":
                raise Exception(f"Missing closing parenthesis")
            self.pos += 1
            return result
        else:
            raise Exception(f"Invalid syntax: {current_token[0]}")


def print_ast(ast, indent=""):
    node_type, *node_values = ast
    print(f"{indent}{node_type} ({node_values[0]})")
    for node in node_values[1:]:
        if isinstance(node, tuple):
            print_ast(node, indent + "  ")
        else:
            print(f"{indent}  {node_type} ({node})")



lexer = Lexer("( 3 + x ) -  a / b  * 2")
tokens = lexer.lexer()
parser = Parser(tokens)
ast = parser.parse()
print_ast(ast)

