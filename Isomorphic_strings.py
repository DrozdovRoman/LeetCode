class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sArr = [-1 for i in range(128)]
        tArr = [-1 for i in range(128)]
        for i in range(len(s)):
            sAscii = ord(s[i])
            tAscii = ord(t[i])
            assert(0 <= sAscii and sAscii <= 127)
            assert(0 <= tAscii and tAscii <= 127)
            if sArr[sAscii] == tAscii and tArr[tAscii] == sAscii:
                continue
            elif sArr[sAscii] == -1 and tArr[tAscii] == -1:
                sArr[sAscii] = tAscii
                tArr[tAscii] = sAscii
            else:
                return False
        return True