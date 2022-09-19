class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        toReturn=[]
        add=0
        for n in nums:
            add+=n
            toReturn.append(add)
        return toReturn