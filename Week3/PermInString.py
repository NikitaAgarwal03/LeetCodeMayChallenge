class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False
        dic = {}
        for ch in s1:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1         
        k = len(s1)
        N = len(s2)
        counter = len(dic)
        
        for i in range(k):
            ch = s2[i]
            if ch in dic:
                dic[ch] -= 1
                if dic[ch] == 0:
                    counter -= 1
                    
            if counter == 0:
                return True
            
        for i in range(k, N):
            ch = s2[i-k]
            if ch in dic:
                dic[ch] += 1
                if dic[ch] == 1:
                    counter += 1
                    
            ch = s2[i]
            if ch in dic:
                dic[ch] -= 1
                if dic[ch] == 0:
                    counter -= 1       
            if counter == 0:
                return True
            
        return False
