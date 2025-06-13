from vectors import Vector2D
from linear_algebra.vector_space import VectorSpace
from matrix import Matrix

matrix = Matrix([[5, 2, 3], 
                 [2, 2, 8], 
                 [3, 123, -2]])

print(matrix.determinant())
print(matrix.triangularize())
print(matrix.rank())
print(matrix.transpose())