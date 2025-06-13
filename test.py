from vectors import Vector2D
from linear_algebra.vector_space import VectorSpace
from matrix import Matrix

matrix = Matrix([[0, 2, 3], 
                 [0, 2, 3], 
                 [0, 2, 3]])

#print(matrix.determinant())
print(matrix.triangularize())
print(matrix.rank())
#print(matrix.transpose())