class Solution:
  def validTree(self, n: int, edges: List[List[int]]) -> bool:
    if len(edges) != n - 1: return False

    adj = defaultdict(set)

    for u, v in edges:
      adj[u].add(v)
      adj[v].add(u)

    cc, vis = 0, defaultdict(bool)

    def dfs(v):
      vis[v] = True
      for u in adj[v]:
        if not vis[u]: dfs(u)

    for i in range(n):
      if not vis[i]:
        dfs(i); cc += 1

    return cc == 1
