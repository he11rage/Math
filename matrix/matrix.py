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

    def __setitem__(self, index, value):
        self.matrix[index] = value

    def __repr__(self):
        def format_elem(x):
            if isinstance(x, float):
                x = 0.0 if abs(x) < 1e-10 else round(x, 6)
            return str(int(x)) if x == int(x) else str(x)

        rows = []
        for row in self.matrix:
            row_str = ", ".join(format_elem(x) for x in row)
            rows.append(f"[{row_str}]")
        return "\n".join(rows)

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
        transposed = [
            [self.matrix[j][i] for j in range(self.size[0])]
            for i in range(self.size[1])
        ]

        return Matrix(transposed)

    def determinant(self) -> float:
        if self.size[0] != self.size[1]:
            raise ValueError("Matrix should be quadratic!")

        triangularized_matrix, perm_count, is_singular = self.triangularize(
            return_info=True
        )
        if is_singular:
            return 0
        det = 1
        for i in range(self.size[0]):
            det *= triangularized_matrix[i][i]

        return round(det * (-1) ** perm_count)

    def triangularize(self, return_info=False):
        EPSILON = 1e-10
        res = self.copy()
        perm_count = 0
        is_singular = False

        for i in range(self.size[0]):
            num_row, max_el = i, abs(res[i][i])

            for j in range(i, self.size[0]):
                if abs(res[j][i]) > max_el:
                    max_el = abs(res[j][i])
                    num_row = j

            if max_el == 0:
                is_singular = True
                continue

            if num_row != i:
                res[i], res[num_row] = res[num_row], res[i]
                perm_count += 1

            for j in range(i + 1, self.size[0]):
                coef = res[j][i] / res[i][i]
                for k in range(i, self.size[1]):
                    res[j][k] -= coef * res[i][k]

            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    if abs(res[i][j]) < EPSILON:
                        res[i][j] = 0

        if return_info:
            return (res, perm_count, is_singular)
        else:
            return res

    def gauss_jordan(self):
        EPSILON = 1e-10
        res = self.copy()

        for i in range(self.size[0]):
            num_row, max_el = i, abs(res[i][i])

            for j in range(i, self.size[0]):
                if abs(res[j][i]) > max_el:
                    max_el = abs(res[j][i])
                    num_row = j

            if num_row != i:
                res[i], res[num_row] = res[num_row], res[i]

            lead = res[i][i]
            if lead != 0:
                for j in range(self.size[1]):
                    res[i][j] /= lead

            for j in range(self.size[0]):
                if j != i:
                    coef = res[j][i]
                    for k in range(self.size[1]):
                        res[j][k] -= res[i][k] * coef

            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    if abs(res[i][j]) < EPSILON:
                        res[i][j] = 0

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

    def inverse(self) -> "Matrix":
        det = self.determinant()
        if det == 0:
            raise ValueError("Determinant can't be a zero!")

        singular_matrix = self.copy()
        extended_matrix = []

        for row in range(singular_matrix.size[0]):
            for column in range(singular_matrix.size[1]):
                if row == column:
                    singular_matrix[row][column] = 1
                else:
                    singular_matrix[row][column] = 0

        for row_self, row_other in zip(self.matrix, singular_matrix.matrix):
            extended_matrix.append(row_self + row_other)

        inverse_matrix = Matrix(extended_matrix).gauss_jordan()

        res_matrix = []

        for row in range(inverse_matrix.size[0]):
            res_row = []
            for column in range(inverse_matrix.size[1]):
                if column >= inverse_matrix.size[1] // 2:
                    res_row.append(inverse_matrix[row][column])
            res_matrix.append(res_row)

        return Matrix(res_matrix)

    def solve(self) -> list[float]:

        return

    def eigen(self) -> list[float]:

        return
