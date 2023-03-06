class Solution:
    def reverseWords(self, s: str) -> str:
        result = str()
        startIndex = 0
        for lastIndex in range(len(s)):
            if s[lastIndex] == " ":
                # print(lastIndex, startIndex)
                for i in range(lastIndex - 1, startIndex - 1, -1):
                    result += s[i]
                result += " "
                startIndex = lastIndex + 1
        lastIndex = len(s) - 1
        while(lastIndex >= startIndex):
            result += s[lastIndex]
            lastIndex -= 1
        return(result)

''' Надо переделать всего 20%'''