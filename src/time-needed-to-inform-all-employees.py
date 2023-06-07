class Solution:
  def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    adj = defaultdict(set)

    for i in range(n):
      if manager[i] != -1:
        adj[manager[i]].add(i)

    q, ans = [(headID, 0)], 0

    while q:
      v, t = q.pop(0)
      ans = max(ans, t)
      for u in adj[v]:
        q.append((u, t + informTime[v]))

    return ans
