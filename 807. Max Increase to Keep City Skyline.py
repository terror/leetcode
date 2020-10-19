class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """
        get all max top/bot
        get all max left/right

        increase everything maximally that isn't
        a max

        """
        n, m = len(grid), len(grid[0])

        # top/bot
        mx_tb = []
        for i in range(n):
            mx = 0
            for j in range(m):
                mx = max(mx, grid[j][i])
            mx_tb.append(mx)

        # left/right
        mx_lr = []
        for i in range(n):
            mx = 0
            for j in range(m):
                mx = max(mx, grid[i][j])
            mx_lr.append(mx)

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != mx_tb[j] and grid[i][j] != mx_lr[i]:
                    ans += abs(grid[i][j]-min(mx_tb[j], mx_lr[i]))
        return ans
