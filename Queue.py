
class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, item): 
        if len(self.queue) < self.size:
            self.queue.append(item)
        else:
            print("Queue overflow")

    def dequeue(self):
        if len(self.queue) > 0:
            self.queue.pop(0) 
        else:
            print("Queue underflow")

    def front(self):
        return self.queue[0]

    def back(self):
        return self.queue[-1]

    def display(self):
        print(self.queue)

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


