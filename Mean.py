#User function Template for python3

class Solution:
    def mean(self, N , A):
        return sum(A)//N 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A = list(map(int,input().split()))
        
        ob = Solution()
        print(ob.mean(N,A))
# } Driver Code Ends

#Back-end complete function Template for Python 3

class Solution:
    def mean(self, N , A):
        
        S = sum(A)      # Getting Sum of the Array
        
        ans = S//N      # The Sum is divided with N to get it's Mean.
        
        return ans