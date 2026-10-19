class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        end_index = len(s)-1
        while end_index>=0 and s[end_index]==" ":
            end_index-=1

        while s[end_index]!=" " and end_index>=0:
            count+=1
            end_index-=1
        return count