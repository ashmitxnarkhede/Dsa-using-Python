class Solution():
    def max_sum_subarray(self,nums,k):
        n=len(nums)
        if n<k:
            print("List is smaller than window")
            return None
    
        window_sum=sum(nums[:k])
        max_sum=window_sum
        
        for i in range(1,n-k+1):
            winodow_sum=window_sum-nums[i-1]+nums[i+k-1]
            
            max_sum=max(max_sum,window_sum)
        print("Max Sum:",max_sum)
        return max_sum
    
sol=Solution()
nums=[1,2,3,4,5,6,7]
window_size=3
    
sol.max_sum_subarray(nums,window_size)
    
#when asked the indices of best sum
#instead of max_sum=max(max_sum,window_sum) do,
"""
        if window_sum>max_sum:
            max_sum=window_sum
            best_sum_index=i
        best_sum=nums([best_sum_index:best_sum_index+k])
"""