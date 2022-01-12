class Solution:
  def reverse(self, x: int) -> int:
    LIMIT = 2**31 - 1

    if len(str(x)) == 1:
      return x

    if abs(x) > LIMIT:
      return 0

    flip = x < 0
    x = abs(x)

    ans = ''
    while x:
      ans += str(x % 10)
      x //= 10

    if int(ans) > LIMIT:
      return 0

    return ((1, -1)[flip]) * int(ans)
