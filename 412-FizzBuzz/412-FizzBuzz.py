# Last updated: 2/26/2026, 11:32:15 AM
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        fizz_buzz_dict = {3 : "Fizz", 5:'Buzz'}
        divisor = [3,5]

        for num in range(1,n+1):

            num_ans_str = []

            for key in divisor:
                if num % key == 0:
                    num_ans_str.append(fizz_buzz_dict[key])
            if not num_ans_str:
                num_ans_str.append(str(num))
            ans.append(''.join(num_ans_str))
        return ans
        