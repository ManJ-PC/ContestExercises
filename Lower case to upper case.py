#User function Template for python3
class Solution:
    def to_upper(self, str):
        strUP = ""
        dif = ord('A') - ord('a')
        for i in str:
            strUP +=  chr(ord(i)+dif)
        return strUP
        
        #return map(sum, str + dif)
        #return map(lambda x:ord(x), str)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        str = input().strip()
        ob = Solution()
        print(ob.to_upper(str))
# } Driver Code Ends

#Back-end complete function Template for Python 3
class Solution:
    def to_upper(self, str):
        ans=''
        for i in str:
            ans+=chr(ord(i)-32)
        return ans