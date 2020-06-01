class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1,l2 = len(word1), len(word2)
        if l1 == 0 : return l2
        if l2 == 0 : return l1
        edit = [j for j in range(l2+1)]
        for i in range(1, l1+1):
            left_top, edit[0] = edit[0], i
            for j in range(1, l2+1):
                left_top, edit[j] = edit[j], min( edit[j] + 1, edit[j - 1] + 1, left_top + (0 if word1[i-1] ==                                       word2[j-1] else 1))
        return edit[l2]
