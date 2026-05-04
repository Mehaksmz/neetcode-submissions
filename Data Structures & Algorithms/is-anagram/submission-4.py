class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        array=[]
        for i in s:
            array.append(i)
            
        for j in t:
            if j in array:
                array.remove(j)
            else:
                return False
        return True