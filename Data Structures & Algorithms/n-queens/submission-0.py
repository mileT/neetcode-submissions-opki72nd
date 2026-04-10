class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        grid = [['.' for _ in range(n)] for _ in range(n)]
        self.dfs(result, grid, 0)
        return result

    def dfs(self, lists: List[List[str]], grid: List[List[str]], row: int) -> None:
        if row == len(grid):
            lists.append(self.write_grid(grid))
            return
        for col in range(len(grid[0])):
            if self.valid_position(grid, row, col):
                grid[row][col] = 'Q'
                self.dfs(lists, grid, row + 1)
                grid[row][col] = '.'

    def valid_position(self, grid, r, c) -> bool:
        for i in range(r):
            if grid[i][c] == 'Q':
                return False
        for i, j in zip(range(r - 1, -1, -1), range(c - 1, -1, -1)):
            if grid[i][j] == 'Q':
                return False
        for i, j in zip(range(r - 1, -1, -1), range(c + 1, len(grid))):
            if grid[i][j] == 'Q':
                return False
        return True

    def write_grid(self, grid: List[List[str]]) -> List[str]:
        return [''.join(row) for row in grid]

            
        