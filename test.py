from vectors import Vector2D
from linear_algebra.vector_space import VectorSpace
from matrix import Matrix

matrix = Matrix(
    [
        [2, 1, 5],
        [0, 1, 3],
        [0, 1, 2]
    ]
)

print(f"\n Исходный вид: \n{matrix}")

print(f"\n Треугольный вид: \n{matrix.triangularize()}")

print(f"\n Определитель: \n{matrix.determinant()}")

print(f"\n Ранг: \n{matrix.rank()}")

inverse = matrix.inverse()

print(f"\n Обратная матрица: \n{inverse}")

prov = matrix.multiply(inverse)

print(f"\n Умножение на исходную обратной: \n{prov}")

print(f"Собственные значения: {matrix.eigen_values()}")
