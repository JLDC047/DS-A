class Stack():
    def __init__(self, capicity):
        self.capicity = capicity
        self.stack = []

    def push(self, item):
        if len(self.stack) < self.capicity:
            self.stack.append(item)
        else:
            print("Stack overflow")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop(-1)
        else:
            print("Stack empty")

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack empty")

    def is_empty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True

    def show_stack(self):
        print(self.stack)

openings = ["[","(","{","<"]
closings = ["]",")","}",">"]

def is_balanced(expression):
    bracket_stack = Stack(26)
    for character in expression:
        if character in openings:
            bracket_stack.push(character)
        elif character in closings:
            index = closings.index(character)  
            if not bracket_stack.is_empty() and openings[index] == bracket_stack.top():
                bracket_stack.pop()
            else:
                return False
    if bracket_stack.is_empty():
        return True
    else:
        return False                    
             
print(is_balanced("print(look at this[234])"))
print(is_balanced("print look at this[234])"))
print(is_balanced("print(look at this[234)"))

