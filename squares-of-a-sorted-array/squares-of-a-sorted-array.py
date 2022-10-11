class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        toReturn=[]
        for n in nums:
            toReturn.append(n**2)
        toReturn.sort()
        return toReturn