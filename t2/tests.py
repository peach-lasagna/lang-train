from cc import Lexer

with open('./test.txt') as f:
    # print(repr(f.read()))
    print(Lexer(f.read()).make_tokens())
