class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) > 0:
            counter=0
            toChange=True
            while toChange==True:
                if nums[counter] == val:
                    del(nums[counter])
                else:
                    counter+=1
                if counter >= len(nums):
                    toChange=False