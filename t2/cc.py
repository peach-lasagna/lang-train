"""
v =       123;

"""
def error(msg: str):
    print(msg)
    sys.exit(1)

import sys
class Lexer:
    def __init__(self, text: str):
        self.text = text
    def make_tokens(self) -> list[str]:
        chars = {
            "(": "LP",
            ")": "RP",
            "=": "ASSIGN",
            ";": "SEPCOL",
            "+": "PLUS",
            "*": "MUL",
            "-": "MINUS",
            "/": "DIV"
        }
        WORDS = {
            "return": "RETURN",
            "var": "VAR"
        }
        DIGITS = "1234567809"
        aplpha = "qwertyuioplkjhgfdsazxcvbnm"
        ap_dig = DIGITS+ aplpha
        tokens = []
        stack = ''
        for c in self.text:
            ind = self.text.index(c)
            if c in chars.keys():
                if stack != '':
                    tokens.append(WORDS.get(stack, stack))
                    stack = ''
                tokens.append(chars[c])
            elif c in ap_dig:
                stack += c
            elif stack != '':
                tokens.append(WORDS.get(stack, stack))
                stack = ''
        return tokens

class Parser:
    def __init__(self, tokens: list[str]):
        self.tokens = tokens
        self.tok_ind = 0
        self.vars = {}

    def parse(self):
        res = self.expr()
        if self.tok_ind != len(self.tokens):
            error(f"ParseError in exp {self.tokens[self.tok_ind]}")
        return res

    def expr(self):
        first = self.term()
        while self.tok_ind < len(self.tokens):
            operator = self.tokens[self.tok_ind]
            if not operator == "PLUS" and not operator == "MINUS":
                break
            else:
                self.tok_ind += 1
            # находим второе слагаемое (вычитаемое)
            second = self.term()
            if operator == "PLUS":
                first += second
            else:
                first -= second
        return first

    def term(self):
        first = self.factor()
        while self.tok_ind < len(self.tokens):
            operator = self.tokens[self.tok_ind]
            if not operator == "MUL" and not operator == "DIV":
                break
            else:
                self.tok_ind += 1

            # находим второе слагаемое (вычитаемое)
            second = self.factor()
            if operator == "MUL":
                first *= second
            else:
                first /= second
        return first

    def factor(self):
        next = self.tokens[self.tok_ind]
        result = 0
        if next == "LP":
            self.tok_ind += 1
            result = self.expr()
            closingBracket = ''
            if self.tok_ind < len(self.tokens):
                closingBracket = self.tokens[self.tok_ind]
            else:
                error("Unexpected end of expression")
            if self.tok_ind < len(self.tokens) and closingBracket == 'RP':
                self.tok_ind += 1
                return result
            error("')' expected but " + closingBracket)
        self.tok_ind += 1
        try:
            return float(self.vars.get(next, next))
        except ValueError:
            error(f"var {next} is not definded")

