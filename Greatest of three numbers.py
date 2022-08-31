#User function Template for python3

class Solution:
    def greatestOfThree(self,A,B,C):
        # if A >= B and A >= C:
        #     return A
        # if B >= C and B >= A:
        #     return B
        # else:
        #     return C
        return max(A,B,C)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split(' '))
        ob=Solution()
        print(ob.greatestOfThree(A,B,C))   
# } Driver Code Ends

#Back-end complete function Template for Python 3

class Solution:
    def greatestOfThree(self,A,B,C):
        #using inbuilt function
        return max(A,max(B,C))