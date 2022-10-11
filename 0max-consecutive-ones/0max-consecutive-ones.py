class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum=0
        current=0
        for n in nums:
            if n != 1:
                current=0
            else:
                current+=1
                if current > maximum:
                    maximum=current
        return maximum