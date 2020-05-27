class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums.count(0) == nums.count(1):
            return len(nums)
        dictcount = {}		
        maxlength,count = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                maxlength = i + 1
            if count in dictcount:
                maxlength = max(maxlength,i-dictcount[count])
            else:
                dictcount[count] = i
        return maxlength
