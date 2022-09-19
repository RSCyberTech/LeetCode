class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        toReturn=[]
        for r in range(1,n+1):
            if r%3==0 and r%5==0:
                toReturn.append("FizzBuzz")
            elif r%3==0:
                toReturn.append("Fizz")
            elif r%5==0:
                toReturn.append("Buzz")
            else:
                toReturn.append(str(r))
        return toReturn