class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. remove non-alphanumeric characters
        # 2. lower the string
        # 3. two pointer, where if i and j meets we return true else false
        newString = re.sub(r'[^a-zA-z0-9]', '', s)
        lowerStr = newString.lower()
        print(lowerStr)
        i = 0 
        j = len(lowerStr) - 1
        while i < j:
            if lowerStr[i] != lowerStr[j]:
                return False
            i += 1
            j -= 1
        return True
