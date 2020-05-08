class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        NO_OF_CHARS = 256
        count = [0] * NO_OF_CHARS 
        index=-1
        for i in s:
            count[ord(i)]+=1
            index = -1
            k = 0
        for i in s: 
            if count[ord(i)] == 1:
                index = k
                break
            k += 1
        return index 
