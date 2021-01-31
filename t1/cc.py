class Interpreter:
    def __init__(self, text):
        self.text = text
        self.sym = 0
    def run(self):
        for char in self.text:
            if char == "+":
                self.sym +=1
            elif char == "-":
                print(self.sym)
                self.sym = 0
            else:
                ind = self.text.index(char)
                print(" "*(ind+2)+ "^")
                print(f"SyntaxError in position {ind}")
                return

if __name__ == "__main__":
    while True:
        Interpreter(input("|>")).run()
