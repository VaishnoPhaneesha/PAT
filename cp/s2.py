#implementing 2 stacks in an array
class twoStacks:
    def __init__(self,n):
        self.size=n
        self.arr=[None]*n
        self.top1=-1
        self.top2=self.size
    def push1(self,x):
        if self.top1>self.top2-1:
            self.top1+=1
            self.arr[self.top1]=x
            print("Pushed:",x)
        else:
            print("Stack1 Overflow")
    def push2(self,x):
        if self.top2>self.top2-1:
            self.top2+=1
            self.arr[self.top2]=x
            print("Pushed:",x)
        else:
            print("Stack2 Overflow")
    def pop1(self):
        if self.top1>=0:
            x=self.arr[self.top1]
            self.top1-=1
            return x
        else:
            print("Stack1 Undeflow")
    def pop2(self):
        if self.top2>=0:
            x=self.arr[self.top2]
            self.top2-=1
            return x
        else:
            print("Stack2 Undeflow")
stacks=twoStacks(5)
stacks.push1(1)
stacks.push1(2)
stacks.push2(11)
stacks.push2(12)
stacks.push1(4)
stacks.push2(8)
stacks.push1(6)


print("Popped from stack1:",stacks.pop1())
print("Popped from stack1:",stacks.pop1())
print("Popped from stack1:",stacks.pop1())
print("Popped from stack1:",stacks.pop1())
print("Popped from stack1:",stacks.pop1())
print("Popped from stack1:",stacks.pop1())
print("Popped from stack1:",stacks.pop1())

    
