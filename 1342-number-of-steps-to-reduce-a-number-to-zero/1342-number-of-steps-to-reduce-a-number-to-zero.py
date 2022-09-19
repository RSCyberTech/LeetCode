class Solution:
    def numberOfSteps(self, num: int) -> int:
        toReturn=0
        while num >0:
            if num%2!=0:
                num-=1
            else:
                num>>=1
            toReturn+=1
        return toReturn