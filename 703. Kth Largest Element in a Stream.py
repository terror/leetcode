from heapq import heapify, heappush, heappop, heappushpop


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapify(nums)
        # we are left with k max elements
        for _ in range(len(nums)-k):
            heappop(self.nums)

    def add(self, val: int) -> int:
        """
        Naive sort solution

        self.nums.append(val)
        self.nums = sorted(self.nums, reverse=True)
        return self.nums[self.k-1]
        """

        """
        Idea: maintain heap of k largest elements at all times
        
        - Kth largest will be the min element at all times
        
        Example 1 & 2:
        
        k = 3
        nums = [4, 5, 8, 2]
        Heap: [4, 5, 8]
        
        kthLargest.add(3);   // return 4
        kthLargest.add(5);   // return 5
        
        --- 1 ---
        Heap: [4, 5, 8]
        Add 3 and pop the min 
        Heap: [4,5,8]
        Kth largest: 4
        
        --- 2 ---
        Heap: [4, 5, 8]
        Add 5 and pop the min
        Heap: [5, 5, 8]
        Kth largest: 5
        
        etc...
        
        """

        # if we don't already have k max elements in heap
        if len(self.nums) < self.k:
            heappush(self.nums, val)
            return min(self.nums)

        heappushpop(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
