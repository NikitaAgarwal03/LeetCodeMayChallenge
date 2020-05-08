class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rn= list(ransomNote)
        mg = list(magazine)
        for s in rn[:]:
            if( s in mg):
                rn.remove(s)
                mg.remove(s)
        if(len(rn) == 0):
            return True
        else:
            return False

