# 1423. Maximum Points You Can Obtain from Cards
#
# Solution: Sliding window shenanigans
#
# Start the window from 0 -> n - k
# Accumulate a running min window
# Subtract this min window from the total to get the answer
#
# TC: O(n) time, O(1) space

class Solution:
  def maxScore(self, cardPoints: List[int], k: int) -> int:
    cards, n = cardPoints, len(cardPoints)

    if k == n:
      return sum(cards)

    curr_window = sum(cards[:n - k])
    curr_min = curr_window

    for i in range(n - k, n):
      curr_window += cards[i] - cards[i - (n - k)]
      curr_min = min(curr_min, curr_window)

    return sum(cards) - curr_min
