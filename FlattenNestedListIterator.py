# Time Complexity : O(n), where n is the total number of integers
# Space Complexity : O(n)

from collections import deque

class NestedIterator:
    def __init__(self, nestedList):
        self.stack = deque(nestedList[::-1])

    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self.stack.extend(deque(top.getList()[::-1]))
        return False


class NestedInteger:
    def __init__(self, value):
        self.value = value

    def isInteger(self):
        return isinstance(self.value, int)

    def getInteger(self):
        return self.value if self.isInteger() else None

    def getList(self):
        return self.value if not self.isInteger() else None

nestedList = [NestedInteger([NestedInteger(1), NestedInteger(1)]), NestedInteger(2), NestedInteger([NestedInteger(1), NestedInteger(1)])]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
print(v)  # Expected output: [1, 1, 2, 1, 1]

nestedList = [NestedInteger(1), NestedInteger([NestedInteger(4), NestedInteger([NestedInteger(6)])])]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
print(v)  # Expected output: [1, 4, 6]

nestedList = [NestedInteger([NestedInteger([]), NestedInteger([])])]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
print(v)  # Expected output: []