class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1
        while i < n:
            curr = numbers[i] + numbers[j]

            if curr == target:
                return [i+1, j+1]

            if curr > target:
                j -= 1
            else:
                i += 1
