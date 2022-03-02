class Solution:
    def replaceDigits(self, s: str) -> str:
        alphabet='abcdefghijklmnopqrstuvwxyz'
        n=''
        for i in s:
            if i in alphabet:
                n=n+i
            else:
                p=alphabet[::]
                p=p[p.index(n[-1]):p.index(n[-1])+int(i)+1]
                n=n+p[-1]
        return(n)
