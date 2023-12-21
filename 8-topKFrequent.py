# Given an integer array nums and an integer k, 
# return the k most frequent elements

from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        return [key for key, _ in count.most_common(k)]
    

mom = [1, 1, 2, 3, 4, 2]
sol = Solution()

print(sol.topKFrequent(mom, 2))