import cmath

def quadratic_equation(a: float, b: float, c: float) -> tuple[float, float] | tuple[complex, complex]:
    EPSILON = 1e-10
    if a != 0:
        disc = b ** 2 - 4 * a * c
        first_root = (-b + cmath.sqrt(disc)) / (2 * a)
        second_root = (-b - cmath.sqrt(disc)) / (2 * a)
        if abs(first_root.imag) < EPSILON and abs(second_root.imag) < EPSILON:
            return first_root.real, second_root.real
        return first_root, second_root
    raise ValueError("argument a can't be a zero")
