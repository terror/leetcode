class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        s = sum([customers[i] for i in range(len(customers)) if not grumpy[i]])

        a = b = c = d = 0
        while a < len(customers):
            if grumpy[a]:
                c += customers[a]
            if a+1 >= X:
                d = max(d, c)
                if grumpy[b]:
                    c -= customers[b]
                b += 1
            a += 1

        return s+d
