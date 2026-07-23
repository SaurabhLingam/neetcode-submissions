class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for row in matrix:
            if row[n - 1] >= target:
                left = 0
                right = n - 1
                while left <= right:
                    mid = int((left + right)/2)
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        right = mid - 1
                    elif row[mid] < target:
                        left = mid + 1
            else:
                continue
        return False 