from vectors import Vector2D
from linear_algebra.vector_space import VectorSpace
from matrix import Matrix

matrix = Matrix([[1, 2, 3], [1, 3, 2], [3, 2, 1]])
second_matrix = Matrix([[1, 2, 3], [1, 3, 2], [3, 2, 1]])

print(matrix.shape())
print(matrix.add(second_matrix))

x = Vector2D(0, 0)
y = Vector2D(0, 1)    
space2d = VectorSpace([x, y])

z = space2d.linear_combination([3, 4])

print(z)