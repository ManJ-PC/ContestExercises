#User function Template for python3

class Solution:
    def sumOfDigits (self, N):
        digits = []
        while (N > 0):
            digit = N % 10
            digits.append(digit)
            N //= 10
        return sum(digits)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.sumOfDigits(N))
# } Driver Code Ends

# Python 3 program to
# compute sum of digits in
# number.

# Function to get sum of digits


def getSum(n):

    sum = 0
    while (n != 0):

        sum = sum + int(n % 10)
        n = int(n/10)

    return sum

# Driver code
n = 687
print(getSum(n))


##########

#Back-end complete function Template for Python 3


class Solution:
    def sumOfDigits (self, N):
        count=0
        while(N>0):
            # extract the last digit
            b=N%10
            # add it to count
            count+=b
           #remove the last digit
            N=N//10
        return count