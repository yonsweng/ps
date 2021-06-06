class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if self.isEqual(mat, target):
            return True

        for _ in range(3):
            mat = self.rotate(mat)
            if self.isEqual(mat, target):
                return True

        return False

    def rotate(self, mat):
        n = len(mat)
        new_mat = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                new_i = j
                new_j = n - i - 1

                new_mat[new_i][new_j] = mat[i][j]

        return new_mat

    def isEqual(self, mat, target):
        n = len(mat)

        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    return False

        return True
