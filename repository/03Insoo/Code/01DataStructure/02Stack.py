class Stack:
    def __init__(self, capacity):
        self.capacity=capacity
        self.array=[None] * self.capacity
        self.top=-1

    def isEmpty(self):
        return self.top==-1
    def isFull(self):
        return self.top==self.capacity -1
    def push(self, value):
        if not self.isFull():
            self.top+=1
            self.array[self.top]=value
        else:
            print("StackOverflow")
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.array[self.top+1]
        else:
            print("StackUnderflow")
    def size(self):
        return self.top+1
    def display(self):
        for i in range(self.top+1):
            print(self.array[i], " ", end="")


#
s1=Stack(10)
s2=Stack(100)
#
s1.push(10)
s1.push(20)
s1.push(30)
#
# s1.pop()
# s1.pop()
# s1.pop()
# s1.pop()
#
s1.size()
s1.display()





# 괄호짝맞추기
def check_brackets(str, length):
    s1= Stack(length)
    for ch in str:
        if ch== '(':
            s1.push(ch)
        elif ch==')':
            if s1.isEmpty():
                return False
            else:
                s1.pop()
        else:
            pass
    return s1.isEmpty()

str=input("수식입력:")
print("괄호짝맞추기결과: ", check_brackets(str, len(str)))