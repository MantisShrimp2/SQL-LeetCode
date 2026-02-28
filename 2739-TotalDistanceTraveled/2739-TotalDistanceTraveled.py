# Last updated: 2/28/2026, 5:58:11 PM
1class Solution(object):
2    def distanceTraveled(self, mainTank, additionalTank):
3        """
4        :type mainTank: int
5        :type additionalTank: int
6        :rtype: int
7        """
8        
9        mileage = 10  # km/liter
10        total = 0
11        while mainTank !=0:
12            if additionalTank == 0 and mainTank ==0:
13                return total
14            if mainTank >=5 and additionalTank >=1:
15                mainTank -= 5-1
16                additionalTank -=1
17                total += 5*mileage
18            else:
19                total += mainTank*mileage
20                mainTank=0
21
22        # while mainTank != 0:
23        #     if mainTank >= 5:
24        #         mainTank -= 5
25        #         total += mileage * 5
26        #     if additionalTank > 0:
27        #         mainTank += 1
28        #         additionalTank -= 1
29        #     else:
30        #         total += mileage * mainTank
31        #         mainTank = 0
32        return total
33
34