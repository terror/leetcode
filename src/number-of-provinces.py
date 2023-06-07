class Solution:
  def findCircleNum(self, c: List[List[int]]) -> int:
    n = len(c); adj = defaultdict(set)

    for i in range(n):
      for j in range(n):
        if c[i][j]:
          adj[i].add(j); adj[j].add(i)

    ans, vis = 0, defaultdict(bool)

    def dfs(v):
      vis[v] = True
      for u in adj[v]:
        if not vis[u]: dfs(u)

    for i in range(n):
      if not vis[i]:
        dfs(i)
        ans += 1

    return ans
