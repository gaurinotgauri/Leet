class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

#find shortest word
        min_len= float('inf')
        for s in strs:
            if len(s)<min_len: min_len = len(s)

# each till traverselength of shortest word
#if the letter at i is  not equal to letter aat i of 1st word ->return string till ith position

        i=0
        while i < min_len:
            for s in strs: #checks for the i'th letter of each word
                if s[i]!=strs[0][i]: 
                    return s[:i]
            i+=1

        return s[:i] # for edge cases which dont enter the if loop (strs= [""] or ["word"])