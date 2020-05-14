class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for char in num:
            while k and stack and stack[-1] > char:
                stack.pop()
                k -= 1
            stack.append(char)
        while k:
            stack.pop()
            k -= 1
        return ''.join(stack).lstrip('0') or '0'
        
