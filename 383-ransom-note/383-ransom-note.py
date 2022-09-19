class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars={}
        for m in magazine:
            if m not in chars.keys():
                chars[m]=0
            chars[m]+=1
        
        print(chars)
        
        for r in ransomNote:
            try:
                chars[r]-=1
            except:
                return False
            if chars[r]< 0:
                return False
        
        return True