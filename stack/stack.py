"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""


class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
        # self.storage = ?

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.stack.append(value)

    def pop(self):
        self.size -= 1
        # if not IndexError:
        return self.stack.pop()
        # else:
        #     return None


if __name__ == '__main__':
    a = Stack()
    a.push(1)
    a.push(1)
    a.pop()
    print(a.stack)
    print(a.__len__())
