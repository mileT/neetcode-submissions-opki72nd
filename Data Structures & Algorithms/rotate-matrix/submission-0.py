class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        start, end = 0, n - 1
        
        while start < end:
            for i in range(end - start):
                top, bottom = start, end
                left, right = start, end

                temp = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = temp
            end -= 1
            start += 1    
        