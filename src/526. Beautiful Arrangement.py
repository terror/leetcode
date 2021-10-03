class Solution:
  def countArrangement(self, n: int) -> int:
    """
        TLE

        from itertools import permutations
        arr = [i for i in range(1, n+1)]
        ret = 0
        for i in permutations(arr):
            ok = 1
            for j in range(len(i)):
                if i[j] % (j+1) != 0 and (j+1) % i[j] != 0:
                    ok = 0
                    break
            ret += ok
        return ret
        """
