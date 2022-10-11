class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        for r in range(len(arr)-1,-1,-1):
            if arr[r] == 0:
                arr.insert(r,0)
                del(arr[-1])            