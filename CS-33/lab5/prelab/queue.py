class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def push(self, v):
        return Stack(Node(v, self.head))

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.head.value, Stack(self.head.next)

    def reverse(self):
        cur = self.head
        res = Stack()
        while cur:
            res = res.push(cur.value)
            cur = cur.next
        return res


class Queue:
    def __init__(self, front=None, rear=None):
        self.front = front if front else Stack()
        self.rear = rear if rear else Stack()

    def is_empty(self):
        return self.front.is_empty() and self.rear.is_empty()

    def enqueue(self, v):
        # just push to rear
        return Queue(self.front, self.rear.push(v))

    def _normalize(self):
        if self.front.is_empty():
            return Queue(self.rear.reverse(), Stack())
        return self

    def dequeue(self):
        q = self._normalize()
        if q.front.is_empty():
            raise IndexError("dequeue from empty queue")
        val, new_front = q.front.pop()
        return val, Queue(new_front, q.rear)
