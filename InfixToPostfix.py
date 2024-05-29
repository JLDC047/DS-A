class Stack():
    def __init__(self, capicity):
        self.capicity = capicity
        self.stack = []
        self.stackOverflow = False
  
    def push(self, item):
        if len(self.stack) < self.capicity:
            self.stack.append(item)
        else:
            self.stackOverflow = True

    def pop(self):
        if not self.is_empty():
            self.stackOverflow = False
            return self.stack.pop(-1)

    def top(self):
        if not self.is_empty():
            return self.stack[-1]  

    def is_empty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True

    def show_stack(self):
        print(self.stack)

precendence = {"+":1, "-":1, "*":2, "/":2, "^":3}

def infixToPostfix(expression):
    stack = Stack(15)
    postfixString = ""
