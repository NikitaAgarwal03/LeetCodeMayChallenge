class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def binary(n):
            count1=0
            while n!=0:
                n=n & (n-1)
                count1+=1
            return count1
        res=[]
        for i in range(0,num+1):
            res.append(binary(i))
        return res
            
        
