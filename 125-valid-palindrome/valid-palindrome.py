class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==1: return True
        a=[]
        
        for i in s:
            if i.isalnum()==True:
                a.append(i)
            else:continue
        
        j=len(a)-1
        for i in range(len(a)):
            if a[i].lower()==a[j].lower():
                j-=1
            else:return False
        return True 



