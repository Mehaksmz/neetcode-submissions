class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            wordLength = len(s)
            sperator = f"{wordLength}?"
            word = sperator + s
            encoded_string += word
        return encoded_string
     


    def decode(self, s: str) -> List[str]:
        num = 0
        i = 0
        res = []
        print(len(s))
        while i < len(s):
            twoNum = ""
            while i < len(s) and s[i] != "?":
                if s[i].isdigit():
                    twoNum += s[i]
                    num = int(twoNum)
                i += 1
            i += 1

            count = 0
            word = ""
            while i < len(s) and count < num:
                word += s[i]
                i += 1
                count += 1
            res.append(word)
        return res

                
