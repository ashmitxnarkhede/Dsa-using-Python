class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        if n == 0:
            return
            
        k = k % n 
        
        def reverse_sublist(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse_sublist(0, n - 1)
        reverse_sublist(0, k - 1)
        reverse_sublist(k, n - 1)