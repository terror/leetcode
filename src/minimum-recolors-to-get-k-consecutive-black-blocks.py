class Solution:
  def minimumRecolors(self, blocks: str, k: int) -> int:
    cnt = i = 0; j = k - 1

    for oo in range(j + 1): cnt += blocks[oo] == 'B'

    ans = k - cnt

    while j < len(blocks):
      cnt -= blocks[i] == 'B'
      i += 1; j += 1
      if j < len(blocks):  cnt += blocks[j] == 'B'
      ans = min(ans, k - cnt)

    return ans
