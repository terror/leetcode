class Solution:
  def numberOfLines(self, widths: List[int], S: str) -> List[int]:
    d, mx, abc = {}, 100, list('abcdefghijklmnopqrstuvwxyz')

    for i, v in enumerate(widths):
      d[abc[i]] = v

    x, currline, s = [], 0, 1

    for i in S:
      currline += d[i]
      if currline > mx:
        currline = d[i]
        s += 1
      x.append(currline)

    return [s, x[-1]]
