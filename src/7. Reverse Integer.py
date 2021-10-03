class Solution:
  def reverse(self, x: int) -> int:
    p = 0
    if x < 0:
      p = 1
    x = abs(x)
    ans = list(str(x)[::-1])

    idx = 0
    for i in range(len(ans)):
      if ans[i] != "0":
        idx = i
        break

    if int("".join(ans[idx:len(ans)])) > (2**31) - 1:
      return 0

    if p:
      return "-{}".format("".join(ans[idx:len(ans)]))
    return "".join(ans[idx:len(ans)])
