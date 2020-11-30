class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = collections.Counter(nums)
        a = sorted(a, key=a.get, reverse=True)
        ans = []
        for i in range(k):
            ans.append(a[i])
        return ans
