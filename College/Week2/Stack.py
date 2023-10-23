#리스트를 활용한 스택
#스택은 LIFO 방식이다.

stack = []

def push(item):
    stack.append(item)

def pop(item):
    if len(stack) != 0:
        item = stack.pop(-1) # or len(stack -1)도 가능
        return item
