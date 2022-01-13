class Solution:
  def maxSatisfied(
    self, customers: List[int], grumpy: List[int], minutes: int
  ) -> int:
    N = len(customers)

    satisfied = sum([customers[i] for i in range(N) if not grumpy[i]])

    i = j = acc = mx = 0
    while j < N:
      acc += customers[j] * grumpy[j]
      if j + 1 >= minutes:
        mx = max(mx, acc)
        acc -= customers[i] * grumpy[i]
        i += 1
      j += 1

    return satisfied + mx
