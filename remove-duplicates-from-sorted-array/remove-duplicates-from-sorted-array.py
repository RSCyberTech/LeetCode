class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) > 0:
            counter=len(nums)-1
            while counter >= 0:
                if nums[counter] in nums[:counter]:
                    del(nums[counter])
                counter-=1
            return len(nums)