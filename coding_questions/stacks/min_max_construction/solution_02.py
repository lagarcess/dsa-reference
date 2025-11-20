class MinMaxStack:
    def __init__(self):
        # The stack will store tuples: (value, min_so_far, max_so_far)
        self.stack = []

    def peek(self):
        if not self.stack:
            return None
        # Return just the value (index 0)
        return self.stack[-1][0]

    def pop(self):
        if not self.stack:
            return None
        # Pop the tuple, but only return the value
        value, _, _ = self.stack.pop()
        return value

    def push(self, number):
        new_min = number
        new_max = number

        # If the stack isn't empty, grab the current min/max to compare
        if self.stack:
            last_min = self.stack[-1][1]
            last_max = self.stack[-1][2]
            new_min = min(number, last_min)
            new_max = max(number, last_max)

        # Push the tuple containing the value and the snapshots of min/max
        self.stack.append((number, new_min, new_max))

    def getMin(self):
        if not self.stack:
            return None
        # Return the min_so_far (index 1)
        return self.stack[-1][1]

    def getMax(self):
        if not self.stack:
            return None
        # Return the max_so_far (index 2)
        return self.stack[-1][2]
