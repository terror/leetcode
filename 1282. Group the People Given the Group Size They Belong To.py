class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = collections.defaultdict(list)
        for i, v in enumerate(groupSizes):
            d[v].append(i)
        ans = []
        for k, v in d.items():
            for i in range(0, len(v), k):
                ans.append(v[i:i+k])
        return ans
