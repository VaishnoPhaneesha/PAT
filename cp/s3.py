#implementing stack using two queues
from queue import Queue
class StackUsingQueues:
    def __init__(self):
        self.queue1=Queue()
        self.queue2=Queue()
    def push(self,x):
        self.queue2.put(x):
        while not self.queue1.empty():
            self.queue2.put(self.queue1.get())
        self.queue1,self.queue2=self.queue2,self.queue1
    def pop(self):
        if self.queue1.empty():
            raise IndexError("pop from an empty stack")
        return self.queue1.get()
    def top(self):
        if self.queue1.empty():
            raise IndexError("top on an empty stack")
        return self.queue1.
        
