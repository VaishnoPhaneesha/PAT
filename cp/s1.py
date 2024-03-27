def


def push(self,data):
    new_node=Node(data)
    if self.top=new_node
        self.top=new_node
        self.minEle=data
    else:
        if data<self.minEle:
            new_node.data=2*data-self.minEle

def pop(self):
    if self.top is None:
        raise IndexError("pop from any empty stack")
    temp=self.top.data
    self.top=self.top.next
    if temp<self.minEle:
        min_removed=self.minEle:
            self.minEle=2*self.minEle-temp
            print(f"Popped:{temp},Peek:{self.top.data if self.top else None},Min:{self.min})
            return min_removed
    else:
        print(f"Popped:{temp},Peek:{self.top.data if self.top else None},Min:{self.min})



def getMin(self):
    if self.top is None:
        raise IndexError("getMin from an empty stack")
    
                         
