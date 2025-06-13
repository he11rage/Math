from vectors import Vector2D
from linear_algebra.vector_space import VectorSpace
from matrix import Matrix

matrix = Matrix([[1, 2, 3], [1, 3, 2], [3, 2, 1]])
second_matrix = Matrix([[1, 2, 3], [1, 3, 2], [3, 2, 1]])


add_matrix = matrix.add(second_matrix)

copy_matrix = matrix.copy()


print(matrix)
print(add_matrix)
print(copy_matrix)