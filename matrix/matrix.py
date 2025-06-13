import math


class Matrix:

    def __init__(self, matrix: list[list[float]]):
        self.matrix = matrix
        self._size = (len(self.matrix), len(self.matrix[0]))

    @property
    def size(self) -> tuple[float, float]:
        return self._size

    def copy(self) -> "Matrix":
        new_matrix = []
        for i in range(self._size[0]):
            row = []
            for j in range(self._size[1]):
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
        return f"{'\n'.join(rows)}"

    def add(self, other: "Matrix") -> "Matrix":
        res = self.copy()
        for i in range(self._size[0]):
            for j in range(self._size[1]):
                res[i][j] = self[i][j] + other[i][j]
        return res

    def sub(self, other: "Matrix") -> "Matrix":
        res = self.copy()
        for i in range(self._size[0]):
            for j in range(self._size[1]):
                res[i][j] = self[i][j] - other[i][j]
        return res

    def multiply(self, other: "Matrix") -> "Matrix":
        if self._size[1] != other._size[0]:
            raise ValueError("Incompatible matrix dimensions")

        res = [[0 for _ in range(other._size[1])] for _ in range(self._size[0])]

        for i in range(self._size[0]):
            for j in range(other._size[1]):
                for k in range(self._size[1]):
                    res[i][j] += self[i][k] * other[k][j]

        return Matrix(res)

    def transpose(self) -> "Matrix":
        res = self.copy()
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                res[i][j] = self[j][i]
        return res

    def determinant(self) -> float:
        if self.size[0] != self.size[1]:
            raise ValueError("Matrix should be quadratic!")

        triangularized_matrix, perm_count = self.triangularize(return_perm_count=True)
        det = 1
        for i in range(self.size[0]):
            det *= triangularized_matrix[i][i]

        return round(det * (-1)**perm_count)

    def triangularize(self, return_perm_count=False):
        res = self.copy()
        perm_count = 0

        for i in range(self.size[0]):
            num_row, max_el = 0, 0

            for j in range(i, self.size[0]):
                if abs(res[j][i]) > abs(max_el):
                    max_el = res[j][i]
                    num_row = j

            if max_el == 0:
                return 0

            if num_row != i:
                for j in range(self.size[1]):
                    res[i][j], res[num_row][j] = res[num_row][j], res[i][j]
                    perm_count += 1

            for j in range(i + 1, self.size[0]):
                coef = res[j][i] / res[i][i]
                for k in range(self.size[1]):
                    res[j][k] -= res[i][k] * coef

        if return_perm_count:
            return (res, perm_count)
        else:
            return res

    def rank(self) -> float:
        res = self.copy()
        res_triang = res.triangularize()
        rank = 0
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if res_triang[i][j] != 0:
                    rank += 1
                    break
        return rank
