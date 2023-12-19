# also the correct solution
class mySolution(object):
    def twoSum(self, nums, target):
        dict = {}
        # loops through the numbers with their corresponding indexs (so it doesnt use .index())
        for i, num in enumerate(nums):
            # sees if the number makes a pair
            complement = target - num
            if complement in dict:
                # if so return it
                return [dict[complement], i]
            # otherwise add the number to the numbers we've seen
            dict[num] = i