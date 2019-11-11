class Queue:
    def __init__(self):
        self.memory = []

    push = lambda self, val: self.memory.append(val)
    pop = lambda self: self.memory.pop(0) if len(self.memory) > 0 else None
    reverse = lambda self: self.memory.reverse()
    print = lambda self: print(' '.join([str(i) for i in self.memory]).strip())


if __name__ == '__main__':
    n = int(input())
    actions = [input() for i in range(n)]

    q = Queue()

    for action in actions:
        action = action.split()

        if action[0] == 'push':
            q.push(float(action[1]))
        else:
            getattr(q, action[0])()

    q.print()

