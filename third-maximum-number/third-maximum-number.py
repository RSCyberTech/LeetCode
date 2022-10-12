class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        unique=[]
        for n in nums:
            if n not in unique:
                unique.append(n)
        try:
            return unique[-3]
        except:
            return unique[-1]