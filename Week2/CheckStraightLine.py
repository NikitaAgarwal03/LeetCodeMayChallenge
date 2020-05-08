class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) == 2:
            return True
        elif len(coordinates) > 2:
            for i in range(2, len(coordinates)):
                if coordinates[1][0] - coordinates[0][0] != 0:
                    m = ((coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0]))
                    b = coordinates[0][1] - m*coordinates[0][0]
                    if coordinates[i][1] == m*coordinates[i][0] + b:
                        return True
                    else:
                        return False
        else:
            return False
    
        
