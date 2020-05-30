class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        m = defaultdict(lambda:defaultdict(set))
        map(lambda pr: m[0][pr[0]].add(pr[1]) or (m[1][pr[1]].add(pr[0])),prerequisites)
        m[2][0].update(set(filter(lambda c: not m[0][c], xrange(numCourses))))
        while m[2][0]:
            v = (lambda x: (m[2][1].add(x) or x))(m[2][0].pop())
            m[2][0].update(filter(lambda o: m[0][o].discard(v) or (not m[0][o] and o not in m[2][1]), m[1][v]))
        return len(m[2][1]) == numCourses
