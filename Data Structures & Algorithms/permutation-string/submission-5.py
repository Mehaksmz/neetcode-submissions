class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1) 
        s1Hash = {}
        s2Hash = {}

        for q in range(0, k):
            s1Hash[s1[q]] = 1 + s1Hash.get(s1[q], 0)
        
        if len(s2) >= k:
            for i in range(0, k):
                s2Hash[s2[i]] = 1 + s2Hash.get(s2[i], 0)
        else:
            return False
          
        if s1Hash == s2Hash:
            return True
        
        for j in range(k, len(s2)):
            sChar = s2[j - k]

            s2Hash[sChar] -= 1

            if s2Hash[sChar] == 0:
                del s2Hash[sChar]

            s2Hash[s2[j]] = 1 + s2Hash.get(s2[j], 0)

            if s1Hash == s2Hash:
                return True

        return False
       

