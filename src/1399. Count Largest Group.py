class Solution:
  def countLargestGroup(self, n: int) -> int:
    ans, d = 0, collections.defaultdict(list)

    for i in range(1, n + 1):
      # get sum of digs
      s = sum([int(n) for n in str(i)])
      d[s].append(i)

    # get max group
    mx = max([len(v) for k, v in d.items()])

    return sum([1 for k, v in d.items() if len(v) == mx])
