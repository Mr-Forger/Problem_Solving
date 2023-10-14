class Queue:
    def __init__(self):
        self.item = []

    def enqueue(self, item):
        self.item.append(item)

    def dequeue(self):
        dequeue_object = None
        if self.isEmpty():
            print("queue is empty")
        else:
            dequeue_object = self.item[0]
            self.item = self.item[1:]

        return dequeue_object

    def peek(self):
        peek_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            peek_object = self.item[0]

        return peek_object

    def isEmpty(self):
        is_empty = False
        if len(self.item) == 0:
            is_empty = True
        return is_empty


queue = Queue()

print(queue)
print(queue.enqueue(7))
print(queue.enqueue(8))
print(queue.enqueue(9))
print(queue.dequeue())