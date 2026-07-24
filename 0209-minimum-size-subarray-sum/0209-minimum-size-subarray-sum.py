class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        min_len= float ("inf")
        curr_sum=0
        n=len(nums)

        for r in range (n):
            curr_sum+=nums[r]

            while curr_sum>=target:
                min_len=min(min_len,r-l+1)
                curr_sum -= nums[l]
                l+=1
        return min_len if min_len !=float("inf") else 0
