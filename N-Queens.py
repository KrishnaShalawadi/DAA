class Solution:
    def solveNQueens (self, n):
        def dfs(queens, xy_diff, xy_sum):
            p = len (queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    dfs(queens+[q], xy_diff+[p-q], xy_sum+[p+q])
        result = []
        dfs([], [], [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in result]
        
n = 4
solution = Solution()
solutions = solution.solveNQueens (n)
for solution in solutions:
    for row in solution:
        print(row)
    print()
