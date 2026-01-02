"""You are given an integer array nums with the following properties:

    --nums.length == 2 * n.
    --nums contains n + 1 unique elements.
    --Exactly one element of nums is repeated n times.
    --Return the element that is repeated n times."""

# class Solution:
#     def repeatedNTimes(self, nums) -> int:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return num
#             seen.add(num)



class Solution:
    def repeatedNTimes(self, nums) -> int:
        n=len(nums)/2
        return int((sum(nums)-sum(set(nums)))/(n-1))
    
sol=Solution()
result = sol.repeatedNTimes([5,1,5,2,5,3,5,4])
print(result)