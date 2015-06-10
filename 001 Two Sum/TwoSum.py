class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dict = {}
        # dict: key is the actual num, value is a list of index
        for i in xrange(len(nums)):
            if nums[i] in dict:
                dict[nums[i]].append(i + 1)
            else:
                dict[nums[i]] = [i + 1]

        for num in nums:
            if target - num in dict:
                # for instance, target is 6, one num is 3
                if target - num == num:
                    if len(dict[num]) > 1:
                        return (dict[num][0], dict[num][1])
                else:
                    return (dict[num][0], dict[target - num][0])
        return None
