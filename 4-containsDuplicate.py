# return if the array contains duplicates

class mySolution(object):
    def containsDuplicate(self, nums):
        # just removes the duplicates and checks if its the same
        return len(set(nums)) != len(nums)
    

# answer
class Solution(object):
    def containsDuplicate(self, nums):
        # does basically the same thing but saves some time but cutting the program if it finds a duplicate
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)