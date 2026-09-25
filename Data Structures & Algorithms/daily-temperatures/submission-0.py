class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack  = []
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                continue
            elif temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
                continue
            else :
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    temp_ind = stack.pop()
                    result[temp_ind] = i - temp_ind 
                stack.append(i)
        return result 