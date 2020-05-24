class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i,j,result = 0,0,[]
        while i < len(A) and j < len(B):
            a1,a2 = A[i]
            b1,b2 = B[j]
            if b1 <= a1 <= b2 or a1<=b1<=a2:
                result.append([max(a1,b1),min(a2,b2)])
            if a2 > b2:
                j+=1
            elif a2  == b2:
                i+=1
                j+=1
            else:
                i+=1
        return result
