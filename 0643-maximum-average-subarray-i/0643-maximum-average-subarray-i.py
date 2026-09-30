class Solution(object):
    def findMaxAverage(self, nums, k):
        if k > len(nums) or k < 0:
            return -1
    
        window = float(sum(nums[ : k ]))
        best = window
        for i in range(k , len(nums)):
            window += nums[i]
            window -= nums[i-k]
            best = max(window , best)
        MaxAverage = best/k
        return MaxAverage

        