class Animals:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "BARK!"


class Pets(Animals):
    def __init__(self, name):
        super().__init__(name)


class Dogs(Pets):
    def __init__(self, name):
        super().__init__(name)


bhura = Dogs(
    "BHURA"
)

print(bhura.bark())
