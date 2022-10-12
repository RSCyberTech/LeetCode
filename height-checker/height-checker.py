class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h=heights[:]
        h.sort()
        counter=0
        for r in range(len(h)):
            if h[r] != heights[r]:
                counter+=1
        return counter
            