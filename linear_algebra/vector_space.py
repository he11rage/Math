from vectors import Vector2D, Vector3D

class VectorSpace:
    
    def __init__(self, basis_vectors):
        self.basis = basis_vectors
        
    def linear_combination(self, coef) -> "Vector":
        result = self.basis[0] * 0
        pairs = zip(self.basis, coef)
        for v, c in pairs:
            result += v * c
        return result