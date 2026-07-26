class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        
        hashmaps = {}
        hashmapt = {}

        for i in range (len(s)):

            if s[i] in hashmaps:
                hashmaps[s[i]]+= 1
            else:
                hashmaps[s[i]]=1

            if t[i] in hashmapt:
                hashmapt[t[i]]+= 1
            else:
                hashmapt[t[i]]=1 
        
        return hashmaps == hashmapt