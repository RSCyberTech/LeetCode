class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        if 1 <= len(nums) and len(nums) <= 1000:
            ans=[]
            for i in nums:
                if 0 <= nums[i] < len(nums):
                    ans.append(nums[i])
            return ans
        