class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter=len(nums)-2
        while counter >= 0:
            if nums[counter] == 0:
                nums.append(nums.pop(counter))
                counter-=1
            else:
                counter-=1