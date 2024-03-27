class MinnStack:
    def__init__(self):
        self.stack=[]
        self.minStack=[]
    def push9self,val:int -> None:
        self,stack.append(val)
        val=val if not slef.minStack or min(self.minStack) > val else self.minStack[-1]
        self.minStack.append(val)
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.(pop)
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
    def getMin(self) -> int:
        return self.minStack[-1] if self.stack else None
#driver code
commands=["MinStack","push","push","push","getMin","pop","top","getMin"]
inputs=[[],[-2],[0],[-3],[],[],[],[],]
minStack=None
output=[]
for cmd,vals in zip(commands,inputs):
    if cmd=="MinStack":
        minStack=MinStack()
        output.append(None)
    elif cmd=="push":
        minStack.push(*vals)
        output.append(None)
    elif cmd=="pop":
        minStack.pop(
        output.append(None)-
        
        
    
