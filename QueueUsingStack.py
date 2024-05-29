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


class Queue():
    def __init__(self, size):
        self.queue = Stack(size)
        self.tempQueue = Stack(size)

    def enqueue(self, item):
        self.queue.push(item)
        if self.queue.stackOverflow:
            print("Queue overflow") 

    def dequeue(self):
        if not self.queue.is_empty():    
            while not self.queue.is_empty():
                value = self.queue.pop() 
                self.tempQueue.push(value) 
            firstItem = self.tempQueue.pop() 
            while not self.tempQueue.is_empty():
                value = self.tempQueue.pop() 
                self.queue.push(value) 
            return firstItem
        else:
            print("Queue empty")               

    def front(self):
        return self.queue.stack[0]

    def back(self):
        return self.queue.top()

    def display(self):
        print(self.queue.stack)

queue = Queue(4)
queue.dequeue()

queue.enqueue("SKINNY")
queue.display()

queue.enqueue("LUNCH")
queue.display()

queue.enqueue("CHIHIRO")
queue.display()

queue.enqueue("BIRDS OF A FEATHER")
queue.display()

queue.enqueue("wILDFLOWER")
queue.display()

print(queue.front())
print(queue.back())

queue.dequeue()
queue.display()

print(queue.front())
print(queue.back())




