class MyStack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def display(self):
        for item in self._data:
            print(item, end=", ")

    def pop(self):
        try:
            return self._data.pop()
        except IndexError:
            print("List is empty")


test = MyStack()
test.push(23)
test.push(63)
test.push(83)
test.push(893)

print("Popped value is", test.pop())
print("Popped value is", test.pop())
print("Popped value is", test.pop())
print("Popped value is", test.pop())
print("Popped value is", test.pop())
print("Popped value is", test.pop())
