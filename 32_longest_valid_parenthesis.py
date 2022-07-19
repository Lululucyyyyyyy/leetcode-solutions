class Solution:
    # stack implementation
    # time: O(n), space: O(n)
    def longestValidParentheses_stack(self, s: str) -> int:
        my_stack = [-1]
        res = 0
        for i, x in enumerate(s):
            if x == '(':
                my_stack.append(i)
            else:
                my_stack.pop()
                if len(my_stack) == 0:
                    my_stack.append(i)
                else:
                    res = max(res, i - my_stack[-1])
        return res

    # counter method
    # time: O(n), space: O(1)
    def longestValidParentheses(self, s: str) -> int:
        left = right = max1 = 0
        #scan left to right
        for x in s:
            if x == '(':
                left += 1
            else:
                right += 1
                
            if right == left:
                max1 = max(max1, 2*right)
            elif left <= right:
                left = right = 0
                
        #scan right to left
        left = right = 0
        for x in reversed(s):
            if x == '(':
                left += 1
            else:
                right += 1
                
            if right == left:
                max1 = max(max1, 2*left)
            elif left >= right:
                left = right = 0
        return max1