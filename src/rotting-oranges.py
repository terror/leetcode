class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    q = [[]]

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == 2: q[0].append((i, j))

    vis = defaultdict(bool)

    for x in q[0]:
      vis[x] = True

    ans = 0
    di = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def in_bounds(x, y):
      return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

    while q:
      t = q.pop(0)
      next_batch = []

      for u, v in t:
        for xo, yo in di:
          p = (u + xo, v + yo)
          if vis[p]: continue
          if in_bounds(p[0], p[1]) and grid[p[0]][p[1]] == 1:
            grid[p[0]][p[1]] = 2
            next_batch.append(p)
            vis[p] = True

      if next_batch:
        q.append(next_batch)
        ans += 1

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == 1: return -1

    return ans
