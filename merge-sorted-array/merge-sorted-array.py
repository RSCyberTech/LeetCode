class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        newArray=[]
        for number in range(n+m-1,-1,-1):
            if m>0 and n>0:
                if nums1[m-1] > nums2[n-1]:
                    nums1[number]=nums1[m-1]
                    m-=1
                else:
                    nums1[number]=nums2.pop(n-1)
                    n-=1
            elif m>0:
                pass
            else:
                nums1[number]=nums2.pop(n-1)
                n-=1