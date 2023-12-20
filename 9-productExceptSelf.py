# given a list of nums, 
# return a list where each element is 
# all the OTHER elements multiplied together
# excluding the current one.

class Solution(object):
    def productExceptSelf(self, nums):
        # creates a list of all 1s
        l = len(nums)
        ret = [1]*l
        # gets the numbers to the left of each index, multiplied
        # so i=0 will be 1 and i=len will have all but len
        for i in range(l-1):
            ret[i+1] = ret[i]*nums[i]
        
        # initializes the opposite of the above
        # where we multiply all numbers to the right
        # we start it at the last number in nums
        right = nums[-1]
        # then, looping backwards through the array
        for i in range(l-2, -1, -1):
            # we multiply the previously calculated array
            # by the numbers to the right of it, stored in right
            # to get (numbers to left) * (numbers to right),
            # but not including the number we are on
            # which is the solution
            ret[i] *= right
            # (updates the right value)
            # the same way we update the values in ret
            # in the first loop
            right *= nums[i]
        return ret