class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        d = {}
        paragraph = re.sub("[^0-9a-zA-Z]+", ' ', paragraph).lower().split()
        for i in paragraph:
            i = i.lower()
            if i not in banned:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
        return max(d, key=d.get)
