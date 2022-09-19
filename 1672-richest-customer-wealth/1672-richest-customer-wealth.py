class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=0
        for a in accounts:
            s=sum(a)
            wealth= s if s > wealth else wealth
        return wealth
            