class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        unique=[]
        for n in nums:
            if n not in unique:
                unique.append(n)
                if len(unique) > 2:
                    return unique[-1]
        return unique[0]