class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = set({"(","{","["})
        closers = set({")","}","]"})
        mapping = {"(":")","[":"]","{":"}"}
        for par in s : 
            if par in openers:
                stack.append(par)
            if par in closers : 
                if not stack:
                    return False
                element = stack.pop()
                if mapping[element] != par :
                    return False 
        return False if len(stack) > 0 else True