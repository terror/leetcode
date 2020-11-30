class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s = 0
        prev = []
        for i in range(len(ops)):
            if ops[i] == "C":
                val = prev[-1]
                s -= val
                prev.pop()
            elif ops[i] == "D":
                val = 2*prev[-1]
                s += val
                prev.append(val)
            elif ops[i] == "+":
                val = prev[-1]+prev[len(prev)-2]
                s += val
                prev.append(val)
            else:
                val = int(ops[i])
                s += val
                prev.append(val)
        return s
