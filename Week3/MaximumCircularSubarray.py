class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total = curr_max = curr_min = 0
        maximum = float("-inf")
        minimum = float("inf")
        for num in A:
            total += num
            curr_max = max(0, curr_max) + num
            maximum = max(maximum, curr_max)
            curr_min = min(0, curr_min) + num
            minimum = min(minimum, curr_min)
        if total == minimum:
            return maximum
        return max(maximum, total - minimum)
