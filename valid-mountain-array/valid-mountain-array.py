class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) > 2:
            midpointFound=False
            if arr[0]>=arr[1] or arr[-1]>=arr[-2]:
                return False
            for r in range(1,len(arr)-1):
                if arr[r] == arr[r-1] or arr[r]==arr[r+1]:
                    return False
                if arr[r-1]<arr[r]>arr[r+1]:
                    if midpointFound==False:
                        midpointFound=True
                    else:
                        return False
            return True
        else:
            return False