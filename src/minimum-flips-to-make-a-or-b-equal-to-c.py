class Solution:
  def minFlips(self, a: int, b: int, c: int) -> int:
    a, b, c = bin(a)[2:], bin(b)[2:], bin(c)[2:]

    L = max(len(a), len(b), len(c))

    while len(a) < L:
      a = '0' + a
    while len(b) < L:
      b = '0' + b
    while len(c) < L:
      c = '0' + c

    ans = 0

    for x, y, z in zip(a, b, c):
      if z == '1':
        ans += x == '0' and y == '0'
      else:
        ans += ((x == '1' and y == '1') *
                2) or (x == '1' and y == '0') or (x == '0' and y == '1')

    return ans
