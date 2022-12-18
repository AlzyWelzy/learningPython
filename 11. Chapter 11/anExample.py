class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'MyClass({self.value})'


obj = MyClass(123)
print(obj)  # prints "MyClass(123)"
