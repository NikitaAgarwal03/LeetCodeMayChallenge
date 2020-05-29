class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        D = dislikes
        S = [set(), set()]
        while D :
            nxt_D = []
            for i, j in D :
                if i in S[0] : S[1].add(j)
                elif i in S[1] : S[0].add(j)
                elif j in S[0] : S[1].add(i)
                elif j in S[1] : S[0].add(i)
                else : nxt_D.append([i, j])
            if D == nxt_D :
                i, j = nxt_D.pop()
                S[0].add(i), S[1].add(j)
            D = nxt_D
        
        return not (S[0] & S[1])
