class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.max_stack = []

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def pop(self):
        if not self.stack:
            return None

        value = self.stack.pop()

        # Only pop from the min/max stacks if the value matches the current min/max
        if value == self.min_stack[-1]:
            self.min_stack.pop()

        if value == self.max_stack[-1]:
            self.max_stack.pop()

        return value

    def push(self, number):
        self.stack.append(number)

        # Push to min_stack ONLY if it's a new minimum (or equal to current min)
        if not self.min_stack or number <= self.min_stack[-1]:
            self.min_stack.append(number)

        # Push to max_stack ONLY if it's a new maximum (or equal to current max)
        if not self.max_stack or number >= self.max_stack[-1]:
            self.max_stack.append(number)

    def getMin(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

    def getMax(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]
