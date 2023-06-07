class Solution:
  def maximumDetonation(self, bombs: List[List[int]]) -> int:
    def overlaps(b1, b2):
      x1, y1, r1 = b1
      x2, y2, _ = b2
      distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
      return distance <= r1

    adj = defaultdict(set)

    for i in range(len(bombs)):
      for j in range(len(bombs)):
        if i != j and overlaps(bombs[i], bombs[j]):
          adj[i].add(j)

    def dfs(v, vis, count):
      vis[v] = True
      for u in adj[v]:
        if not vis[u]:
          return dfs(u, vis, count + 1)
      return count

    ans = 0

    for i in range(len(bombs)):
      ans = max(ans, dfs(i, defaultdict(bool), 1))

    return ans
