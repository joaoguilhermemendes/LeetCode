class Solution(object):
    def isValid(self, s):
        cont = 0
        for elem in s:
            print(s[cont])
            if cont < len(s)-1:
                cont+=1
                print(s[cont])
