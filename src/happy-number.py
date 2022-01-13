class Solution:
  def isHappy(self, n: int) -> bool:
    seen = set()
    while n != 1:
      curr = n
      temp = 0
      while curr:
        temp += (curr % 10)**2
        curr //= 10
      if temp in seen:
        return False
      seen.add(temp)
      n = temp
    return True
