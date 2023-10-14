class Stack:
    def __init__(self):
        self.item = []      #요소들을 집어넣는 리스트 생성

    def push(self, item):       #스택에 값을 집어넣는 메소드
        self.item.append(item)

    def pop(self):      #스택의 맨 마지막의 인덱스를 삭제하는 메소드
        return self.item.pop()

    def peek(self):     #스택의 맨 마지막의 인덱스를 삭제하지 않고 리턴하는 메소드
        return self.item[-1]

    def is_empty(self):     #스택이 비어있는지 확인하는 메소드
        if len(self.item) == 0:
            return True
        return False


stack = Stack()
print(stack)

print(stack.is_empty())
stack.push(7)
stack.push(8)
stack.push(9)
print(stack.item)

print(stack.pop())
print(stack.item)

print(stack.peek())
print(stack.item)

print(stack.pop())
print(stack.item)

