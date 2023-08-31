class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = 0
        square = 0
        curly = 0

        for elem in s:
            match elem:
                case "(":
                    parentheses+=1
                case ")":
                    parentheses-=1
                case "[":
                    square+=1
                case "]":
                    square-=1    
                case "{":
                    curly+=1 
                case "}":
                    curly-=1 
        
        if parentheses!=0 or square!=0 or curly!=0:
            return False
        return True
