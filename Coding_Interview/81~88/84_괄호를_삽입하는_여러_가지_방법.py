#괄호를 삽입하는 여러 가지 방법
#https://leetcode.com/problems/different-ways-to-add-parentheses

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        
        answer = []
        
        for idx, value in enumerate(expression):
            if value in '*+-':
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1:])
                
                for i in left:
                    for j in right:
                        answer.append(eval("{}{}{}".format(i, value, j)))
            
        return answer
