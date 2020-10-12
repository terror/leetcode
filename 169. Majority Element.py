class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for key, val in d.items():
            if val > len(nums)/2:
                return key
