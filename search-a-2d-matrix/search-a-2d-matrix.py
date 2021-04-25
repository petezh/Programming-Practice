class Solution:
    def searchMatrix(self, matrix, target):
        # null case
        if not matrix or target is None:
            return False
        # count rows/cols
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        # bin search
        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False