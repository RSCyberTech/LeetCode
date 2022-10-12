class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing=[]
        for n in range(len(nums)):
            toCheck=abs(nums[n])-1
            nums[toCheck]=-(abs(nums[toCheck]))
        for n in range(len(nums)):
            if nums[n] > 0:
                missing.append(n+1)
        return missing