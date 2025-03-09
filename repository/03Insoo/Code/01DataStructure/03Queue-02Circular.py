class CircularQueue:
    def __init__(self, capacity):
        self.capacity=capacity
        self.array=[None] * self.capacity
        self.rear=0
        self.front=0
    
    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return self.front==(self.rear+1)%self.capacity
    
    def enqueue(self, value):
        if not self.isFull():
            self.rear=(self.rear+1)%self.capacity
            self.array[self.rear]=value
        else:
            print("Overflow")
    def dequeue(self):
        if not self.isEmpty():
            self.front=(self.front+1)%self.capacity
            return self.array[self.front]
        else:
            print("Underflow")
    def size(self):
        return (self.rear-self.front+self.capacity)%self.capacity
    def display(self):
        for i in range(self.front+1, self.front+1+self.size()):
            print(self.array[i%self.capacity]," ", end="")
        




q1= CircularQueue(10)
#
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.enqueue(60)
q1.enqueue(70)
q1.enqueue(80)
q1.enqueue(90)
q1.enqueue(100)
#
q1.enqueue(110)
#
q1.dequeue()
q1.dequeue()
q1.enqueue(110)
#
print(q1.size())
print(q1.isFull())



#
def josephus(n,k):
    q1=CircularQueue(n+1)
    for i in range(1, n+1):
        q1.enqueue(i)
    print(q1.display())
    print("\n")
    while q1.size()>1:
        for i in range(k-1):
            j=q1.dequeue()
            q1.enqueue(j)
        q1.dequeue()
        q1.display()
        print("\n")
        
    return q1.dequeue()
#
n= int(input("게임사람수입력: "))
k= int(input("제외될번호입력: "))
print("남은사람의번호는 ", josephus(n, k))
