# Given an integer array nums and an integer k, 
# return the k most frequent elements

from collections import Counter

class mySolution(object):
    def topKFrequent(self, nums, k):
        # uses Counter to get a frequency dist
        count = Counter(nums)
        # loops through and returns the k most common
        return [key for key, _ in count.most_common(k)]
    
class Solution(object):
    def topKFrequent(self, nums, k):
        hs = {}
        frq = {}
        
        for i in xrange(0, len(nums)):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1

        for z,v in hs.iteritems():
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)
        
        arr = []
        
        for x in xrange(len(nums), 0, -1):
            if x in frq:
                
                for i in frq[x]:
                    arr.append(i)

        return [arr[x] for x in xrange(0, k)]