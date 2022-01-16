class Solution:
  def isUgly(self, n: int) -> bool:
    if n <= 0:
      return False
    i, f = 2, []
    while i**2 <= n:
      if n % i:
        i += 1
      else:
        n //= i
        f.append(i)
    if n > 1:
      f.append(n)
    return all(el in [2, 3, 5] for el in f) or not f
