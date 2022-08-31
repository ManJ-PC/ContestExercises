#User function Template for python3
class Solution:
    def oddEven (ob,N):
        if N % 2:
            return "odd" # odd result is 1
        else:
            return "even" # because rest is 0 so else


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())

        ob = Solution()
        print(ob.oddEven(N))
# } Driver Code Ends


#Back-end complete function Template for Python 3
class Solution:
    def oddEven(ob,N):
        if N%2==0:
            return "even"
        else:
            return "odd"