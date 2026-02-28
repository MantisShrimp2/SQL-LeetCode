# Last updated: 2/28/2026, 6:04:20 PM
class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        
        mileage = 10  # km/liter
        total = 0
        while mainTank !=0:
            if additionalTank == 0 and mainTank ==0:
                return total
            if mainTank >=5 and additionalTank >=1:
                mainTank -= 5-1
                additionalTank -=1
                total += 5*mileage
            else:
                total += mainTank*mileage
                mainTank=0

        # while mainTank != 0:
        #     if mainTank >= 5:
        #         mainTank -= 5
        #         total += mileage * 5
        #     if additionalTank > 0:
        #         mainTank += 1
        #         additionalTank -= 1
        #     else:
        #         total += mileage * mainTank
        #         mainTank = 0
        return total

