from collections import defaultdict
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N == 1:
            return 1
        count = defaultdict(int)
        for i in trust:
            count[i[1]] += 1
            count[i[0]] -= 1
            
        for key, value in count.items():
            if value == N - 1:
                return key
        return -1
