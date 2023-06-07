class Solution:
  def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
    indeg, ans = Counter(), 0

    adj = defaultdict(set)

    for i in range(n):
      indeg[i] += 0

    for u, v in relations:
      adj[u - 1].add(v - 1)
      indeg[v - 1] += 1

    q = [[k for k in indeg if not indeg[k]]]

    studied = 0

    while q:
      t = q.pop(0); next = set()

      studied += len(t)

      ans += 1

      for u in t:
        for v in adj[u]:
          indeg[v] -= 1
          if not indeg[v]: next.add(v)

      if next: q.append(list(next))

    return ans if studied == n else -1
