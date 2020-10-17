class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        p = s = 1
        while p:
            ok, j = 1, s
            for i in nums:
                j += i
                if j < 1:
                    s, ok = s+1, 0
                    break
            if ok:
                break
        return s
