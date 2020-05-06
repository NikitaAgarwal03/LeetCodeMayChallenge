class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        
        for item in nums:
            if(item in freq):
                freq[item] +=1
            else:
                freq[item]=1
        for num,count in freq.items():
            if(count > (len(nums)/2)):
                majority= num
                return majority
