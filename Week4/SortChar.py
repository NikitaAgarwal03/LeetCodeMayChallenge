class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        res = []
        for c, n in count.most_common():
             res.extend([c] * n)
        return ''.join(res)
