import math


class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def sub(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def scalar_multiplication(self, scalar: float) -> "Vector3D":
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self) -> "Vector3D":
        if self.x == 0 and self.y == 0 and self.z == 0:
            raise ValueError("zero vector can't be normalized")
        length = self.length()
        return Vector3D(self.x / length, self.y / length, self.z / length)

    def scalar_product(self, other: "Vector3D") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def vector_product(self, other: "Vector3D") -> "Vector3D":
        i = self.y * other.z - self.z * other.y
        j = self.z * other.x - self.x * other.z
        k = self.x * other.y - self.y * other.x
        return Vector3D(i, j, k)

    def cos_angle(self, other: "Vector3D") -> float:
        product = self.scalar_product(other)
        cos_angle = product / (self.length() * other.length())
        if cos_angle > 1:
            return 1
        elif cos_angle < -1:
            return -1
        else:
            return cos_angle

    def angle(self, other: "Vector3D") -> float:
        return math.acos(self.cos_angle(other))

    def is_collinear(self, other: "Vector3D") -> bool:
        EPSILON = 1e-10
        if self.angle(other) == 0 or self.angle(other) - math.pi < EPSILON:
            return True
        else:
            return False

    def is_ortogonal(self, other: "Vector3D") -> bool:
        if self.scalar_product(other) == 0:
            return True
        else:
            return False

    def projection_length(self, other: "Vector3D") -> float:
        return self.length() * self.cos_angle(other)

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def __eq__(self, other: "Vector3D") -> bool:
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False

    def __add__(self, other: "Vector3D") -> "Vector3D":
        return self.add(other)

    def __sub__(self, other: "Vector3D") -> "Vector3D":
        return self.sub(other)

    def __mul__(self, scalar: float) -> "Vector3D":
        return self.scalar_multiplication(scalar)

    def __rmul__(self, scalar: float) -> "Vector3D":
        return self.__mul__(scalar)

    def __round__(self, ndigits=2):
        return Vector3D(
            round(self.x, ndigits), round(self.y, ndigits), round(self.z, ndigits)
        )
