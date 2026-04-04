"""Write Python code to:
1. Print the first and last number
2. Add the number 99 to the end
3. Change the number 3 to 300
4. Print the total count of items in the list"""
"""
#1. Print the first and last number
numbers = [1, 2, 3, 4, 5]
print("First Number & Last Number:", numbers[0], numbers[-1])
#2. Add the number 99 to the end
numbers.append(99)
print("After adding 99 to the end:", numbers)
#3. Change the number 3 to 300
i=numbers.index(3)
numbers[i] = 300
print("After changing 3 to 300:", numbers)
#4. Print the total count of items in the list
print("Total count of items in the list:", len(numbers))
"""

#Two Pointers Approach
#sorted array
#nums=[1,2,3,4,5,6]
#target=8
"""
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j] == target:
            print(nums[i], nums[j])
"""

#Optimizing for two pointer technique
"""
left=0
right=len(nums)-1

while left<right:
    sum=nums[left]+nums[right]
    if sum==target:
        print(nums[left], nums[right])
        left+=1
        right-=1
    elif sum<target:
        left+=1
    else:
        right-=1
        """
"""        
Use the Two Pointer technique to find ALL pairs 
that add up to 20.

Expected output:
Pair found: 2 + 18 = 20
Pair found: 6 + 14 = 20
Pair found: 10 + 10 = 20  ← wait, is this possible here? 🤔
"""
numbers = [2, 4, 6, 8, 10, 14, 18]
target=20

left=0
right=len(numbers)-1

while left<=right:
    curr_sum=numbers[left]+numbers[right]
    if curr_sum==target:
        print(f"Pair found: {numbers[left]} + {numbers[right]} = {target}")
        left+=1
        right-=1
    elif curr_sum<target:
        left+=1
    else:
        right-=1