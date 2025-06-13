import math


class Matrix:

    def __init__(self, matrix: list[list[float]]):
        self.matrix = matrix

    def shape(self) -> tuple[float, float]:
        return (len(self.matrix), len(self.matrix[0]))
        
    def copy(self) -> "Matrix":
        size = self.shape()
        new_matrix = []
        for i in range(size[0]):
            row = []
            for j in range(size[1]):
                row.append(self.matrix[i][j])
            new_matrix.append(row)
                
        return Matrix(new_matrix)
    
    def __getitem__(self, index):
        return self.matrix[index]
    
    def __repr__(self): 
        rows = []
        for row in self.matrix:
            row_str = ", ".join(str(x) for x in row)
            rows.append(f"[{row_str}]")
        return f"Matrix([{', '.join(rows)}])"
    
    def add(self, other: "Matrix") -> "Matrix":
        size = self.shape()
        res = self.copy()
        for i in range(size[0]):
            for j in range(size[1]):
                res[i][j] = self[i][j] + other[i][j]
        return res
