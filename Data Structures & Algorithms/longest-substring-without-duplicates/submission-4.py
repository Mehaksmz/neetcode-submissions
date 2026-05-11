class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        string = ""
        dict = {}
        for i in range(len(s)):
            string = ""
            for j in range(i, len(s)):
                if s[j] not in string:
                    string += s[j]
                    dict[string] = len(string)
                else:
                    break
        return max(dict.values())