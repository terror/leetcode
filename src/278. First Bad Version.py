# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
  def firstBadVersion(self, n):
    """
        :type n: int
        :rtype: int
        """
    lo, hi = 0, n - 1
    while (lo <= hi):
      mid = (lo + hi) // 2
      if isBadVersion(mid):
        hi = mid - 1
      else:
        lo = mid + 1
    return hi + 1
