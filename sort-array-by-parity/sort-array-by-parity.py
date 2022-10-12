class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        toPop=True
        while toPop:
            try:
                num=nums.pop(0)
            except:
                toPop=False
            else:
                if num%2==0:
                    even.append(num)
                else:
                    odd.append(num)
        return even+odd
                