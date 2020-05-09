class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        odd =1
        oddsum = 0
        while oddsum < num:
            oddsum += odd
            if oddsum == num:
                return True
            odd +=2
        return False
        
