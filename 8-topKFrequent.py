# Given an integer array nums and an integer k, 
# return the k most frequent elements

class Solution(object):
    def topKFrequent(self, nums, k):
        a = map(nums.count, nums)
        return a[:k]
    

mom = [1, 1, 2, 3, 4, 2]
sol = Solution()

print(sol.topKFrequent(mom, 1))