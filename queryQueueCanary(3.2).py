class Query:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class Queue:
    def __init__(self, length):
        self.length = length
        self.head = self.tail = None
        self.__size = 0

    def push(self, value):
        q = Query(value)

        if self.__size < self.length:
            if self.__size == 0:
                self.head = self.tail = q
            elif self.__size > 0:
                self.tail.next = q
                self.tail = q
        else:
            q.next = self.head
            self.head = q

        self.__size += 1

    def pop(self):
        value = self.head

        if self.__size == 1:
            self.head = self.tail = None
        elif self.__size > 1:
            self.head = value.next
            value.next = None

        if value is not None:
            self.__size -= 1

        return value

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        try:
            value = self.current
            self.current = value.next
            return value
        except AttributeError:
            raise StopIteration

    def __str__(self):
        res = ''

        for i in self:
            res += str(i) + ' '

        return res.strip()


if __name__ == '__main__':
    length = int(input())
    n = int(input())
    actions = [input() for i in range(n)]

    q = Queue(length)

    for action in actions:
        action = action.split()

        q.push(float(action[1])) if len(action) == 2 else q.pop()

    print(q)
