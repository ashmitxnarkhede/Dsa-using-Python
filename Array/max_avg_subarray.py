class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n=len(nums)
        window_sum=float(sum(nums[:k]))
        max_sum=window_sum

        for i in range(1,n-k+1):
            window_sum=window_sum-nums[i-1]+nums[i+k-1]

            if max_sum<window_sum:
                max_sum=window_sum
        print("max_avg:",max_sum/k)
        return max_sum/k
    

sol=Solution()
nums=[1,2,3,4,5,6]
size=3
sol.findMaxAverage(nums,size)