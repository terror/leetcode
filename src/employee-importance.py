# 690. Employee Importance
#
# Solution: DFS + accumulate answer
#
# Create the adj list id -> (importance, subordinates)
# DFS on this adj list while accumulating the answer
# Return the answer

from collections import namedtuple

class Solution:
  def __init__(self):
    self.adj = {}
    self.ans = 0
    self.vis = [0] * int(2e5)

  def getImportance(self, employees: List['Employee'], id: int) -> int:
    I = namedtuple('I', 'v s')

    for employee in employees:
      self.adj[employee.id] = I(
        employee.importance,
        employee.subordinates
      )

    self.dfs(id)

    return self.ans

  def dfs(self, v):
    self.vis[v] = 1
    self.ans += self.adj[v].v
    for u in self.adj[v].s:
      if not self.vis[u]:
        self.dfs(u)
