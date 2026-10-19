class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=len(needle)
        m=len(haystack)
        count=0
        j=0

        while j<=(m-l):
            for i in range(l):
                if needle[i]==haystack[j+i]: 
                    count+=1
                elif needle[i]!=haystack[j+i]:
                    count=0
                    break 
            if count==l: return j
            count=0
            j+=1
        return -1
        