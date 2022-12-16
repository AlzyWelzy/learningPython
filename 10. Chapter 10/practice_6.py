class CSStudents:
    stream = "cse"

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


alzy = CSStudents("alzy", 11)
print(f"alzy.stream: {alzy.stream}")

alzy.stream = "CSE"
print(f"alzy.stream: {alzy.stream}")
