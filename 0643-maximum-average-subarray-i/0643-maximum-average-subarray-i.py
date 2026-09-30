class Solution(object):
    def findMaxAverage(self, nums, k):
        if k > len(nums) or k < 0:
            return -1
    
        window = sum(nums[ : k ])
        best = window
        for i in range(k , len(nums)):
            window = window + nums[i] - nums[i-k]
            best = max(window , best)
        return float(best)/k

        