import sys

class Solution:
  def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    q, dis, vis = [(0, 0, 1)], sys.maxsize, defaultdict(bool)

    di = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    def in_bounds(p):
      x, y = p
      return x >= 0 and x < len(grid) and y >= 0 and y < len(grid)

    found = False

    while q:
      x, y, dissy = q.pop(0)

      if grid[x][y] == 1: continue

      if x == len(grid) - 1 == y:
        found = True
        dis = min(dis, dissy)
        continue

      for u, v in di:
        p = (x + u, y + v, dissy + 1)
        if not in_bounds((p[0], p[1])) or not grid[p[0]][p[1]] == 0: continue
        if not vis[(p[0], p[1])]:
          q.append(p)
          vis[(p[0], p[1])] = True

    return dis if found else -1
