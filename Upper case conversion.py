class Solution:
    def transform(self, s):
        # for k in range(0, len(s)):
        #     print(f"{s[k]}")
        
        s = s[0].upper() + s[1:]
        for i in range(0,len(s)):#range(0, len(s))
            if(s[i] == ' ' and (i+1) <= len(s)): # 
                if (i+2) <= len(s):    
                    s = s[:i+1] + (s[i+1]).upper() + s[i+2:]
                elif i == len(s)-1:
                    s = s[:i+1] + (s[i+1]).upper()
        return s  
        
string transform(string str)
{
    for (int i = 0; i < str.length(); ++i)
    {
        if(i==0 || str[i-1] == ' ')
            str[i] = toupper(str[i]);
    }
    return str;
}