from cc import Lexer, Parser

# with open('./test.txt') as f:
#     # print(repr(f.read()))
#     print(Lexer(f.read()).make_tokens())
# print("====================")
print(Parser(["v", "ASSIGN", "5","SEMCOL", "L", "ASSIGN", "LP", '2', "PLUS", "v", "RP", "MUL", "5", "SEMCOL"]).parse())

