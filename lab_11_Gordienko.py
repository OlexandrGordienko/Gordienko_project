# Приклад №1 ################################################################################
print('Приклад №1:\n')

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count = 0


    def get_counter(self):
        return self.__count


    def pop(self):
        val = Stack.pop(self)
        self.__count += 1
        return val



stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())

# Приклад №2 ################################################################################
print('\nПриклад №2:\n')

class QueueError(Exception):   # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self.list_queue = []

    def put(self, elem):
        self.list_queue.insert(0, elem)


    def get(self):
        if not len(self.list_queue):
            raise QueueError
        else:
            elem = self.list_queue.pop()
        return elem

    
#     Альтернативний варіант
    # def get(self):
    #     if len(self.queue) > 0:
    #         elem = self.queue[-1]
    #         del self.queue[-1]
    #         return elem
    #     else:
    #         raise QueueError

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
# print(que.get())
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")

# Завдання №1 ###############################################################################
print('\nЗавдання №1:\n')

class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []

    def put(self, item):
        self.items.append(item)

    def get(self):
        if not self.isempty():
            return self.items.pop(0)
        else:
            raise QueueError("Queue is empty")

    def isempty(self):
        return len(self.items) == 0

class SuperQueue(Queue):
    pass

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")