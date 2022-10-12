class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        upPointer=0
        lowPointer=0
        max1=0
        
        
        while upPointer <= len(nums):
            toCheck=nums[lowPointer:upPointer]
            
            if toCheck.count(0) > 1:
                lowPointer+=1
            else:
                upPointer+=1
                if len(toCheck) > max1:
                    max1=len(toCheck)
        return max1