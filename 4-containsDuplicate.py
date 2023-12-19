class mySolution(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)
    

# answer
class Solution(object):
    def containsDuplicate(self, nums):
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)