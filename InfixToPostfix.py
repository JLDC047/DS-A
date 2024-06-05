class Stack():
    def __init__(self, capacity):
        self.capicity = capacity
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
        
    def length(self):
        return len(self.stack)

    def show_stack(self):
        print(self.stack)

precendence = {"+":1, "-":1, "*":2, "/":2, "^":3, "(":0, ")":0}

def infixToPostfix(expression):
    operators = Stack(15)
    postfixString = ""
    for character in expression:
        if character not in precendence:
            postfixString += character 
        else:
            if character == "(":
                operators.push(character)
            elif character == ")":
                lastOperator = operators.pop()
                #print(lastOperator) 
                while not operators.is_empty() and lastOperator != "(":
                        postfixString += lastOperator
                        lastOperator = operators.pop()
                        #print(lastOperator)
            else:
                while not operators.is_empty() and precendence[character] <= precendence[operators.top()] and operators.top() != "(":
                    print(precendence[character])
                    print(precendence[operators.top()])
                    postfixString += operators.pop()                  
                operators.push(character)    
        #print(postfixString)            
        #print(operators.stack)    
    while not operators.is_empty():
        postfixString += operators.pop()              
    return postfixString                 
    

print(infixToPostfix("c+d/f-(a+b-d)+e"))

