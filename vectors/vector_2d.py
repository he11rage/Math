import math

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def sub(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def scalar_multiplication(self, scalar: float) -> "Vector2D":
        return Vector2D(self.x * scalar, self.y * scalar)

    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self) -> "Vector2D":
        if self.x == 0 and self.y == 0:
            raise ValueError("zero vector can't be normalized")
        length = self.length()
        return Vector2D(self.x / length, self.y / length)

    def scalar_product(self, other: "Vector2D") -> float:
        return self.x * other.x + self.y * other.y

    def cos_angle(self, other: "Vector2D") -> float:
        product = self.scalar_product(other)
        cos_angle = product / (self.length() * other.length())
        if cos_angle > 1:
            return 1
        elif cos_angle < -1:
            return -1
        else:
            return cos_angle

    def angle(self, other: "Vector2D") -> float:
        return math.acos(self.cos_angle(other))

    def is_collinear(self, other: "Vector2D") -> bool:
        EPSILON = 1e-10
        if self.angle(other) == 0 or self.angle(other) - math.pi < EPSILON:
            return True
        else:
            return False

    def is_ortogonal(self, other: "Vector2D") -> bool:
        if self.scalar_product(other) == 0:
            return True
        else:
            return False

    def projection_length(self, other: "Vector2D") -> float:
        return self.length() * self.cos_angle(other)

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __eq__(self, other: "Vector2D") -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return self.add(other)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        return self.sub(other)

    def __mul__(self, scalar: float) -> "Vector2D":
        return self.scalar_multiplication(scalar)

    def __rmul__(self, scalar: float) -> "Vector2D":
        return self.__mul__(scalar)

    def __round__(self, ndigits=2):
        return Vector2D(round(self.x, ndigits), round(self.y, ndigits))
