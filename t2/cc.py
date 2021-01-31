"""
v =       123;
f ( 123 ) -> { v = 213; return 132; }

"""
import sys
class Lexer:
    def __init__(self, text: str) -> list[str]:
        self.text = text
    def make_tokens(self):
        chars = {
            "(": "STPAR",
            ")": "ENDPAR",
            "{": "STFUN",
            "}": "ENDFUN",
            "=": "ASSIGN",
            "\n": "NEWLINE",
            ";": "SEPCOL",
            "+": "PLUS"
        }
        WORDS = {
            "return": "RETURN",
            "->": 'DO'
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
    def __init__(self, lexer: Lexer):
        self.lexer = lexer

