from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize a deque (double-ended queue) as a stack to evaluate the expression
        stack = deque()
        
        # Iterate through each token in the input list
        for val in tokens:
            # Check if the current token is an operator
            if val == '+':
                # Pop the top two elements from the stack, perform the addition, and push the result back onto the stack
                a, b = stack.popleft(), stack.popleft()
                stack.appendleft(a + b)
            elif val == '-':
                # Pop the top two elements from the stack, perform the subtraction, and push the result back onto the stack
                a, b = stack.popleft(), stack.popleft()
                stack.appendleft(b - a)
            elif val == '*':
                # Pop the top two elements from the stack, perform the multiplication, and push the result back onto the stack
                a, b = stack.popleft(), stack.popleft()
                stack.appendleft(a * b)
            elif val == '/':
                # Pop the top two elements from the stack, perform the integer division, and push the result back onto the stack
                a, b = stack.popleft(), stack.popleft()
                # Use int() to perform floor division for the result to match the behavior of RPN calculators
                stack.appendleft(int(b / a))
            else:
                # If the token is a number, convert it to an integer and push it onto the stack
                stack.appendleft(int(val))
        
        # The final result will be the only element left in the stack
        return stack[0]
