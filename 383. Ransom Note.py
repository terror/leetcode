class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a, b = collections.Counter(ransomNote), collections.Counter(magazine)
        for x in a.keys():
            if x not in b:
                return False
            if b[x] < a[x]:
                return False
        return True
