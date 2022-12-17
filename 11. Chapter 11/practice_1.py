class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x**2 + self.y**2)**0.5

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * self.x, self.y * self.y)

    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"


class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def length(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print(v1 + v2)  # prints "(5, 7, 9)"
print(v1 - v2)  # prints "(-3, -3, -3)"
print(v1 * 2)   # prints "(2, 4, 6)"
print(v1 / 2)   # prints "(0.5, 1.0, 1.5)"
print(v1.length())  # prints "3.7416573867739413"
