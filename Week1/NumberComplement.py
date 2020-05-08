class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        x= bin(num).replace("0b", "")
        binary=list(x)        
        for i in range(len(binary)):
            if(int(binary[i]) & 1 == 1):
                binary[i] = '0'
            elif(int(binary[i]) & 1== 0):
                binary[i] = '1'
        y= int("".join(binary))
        binstr=str(y)
        output = int(binstr,2)
        return output

