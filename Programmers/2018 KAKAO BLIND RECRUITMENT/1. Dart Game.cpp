#include <string>

using namespace std;

int pow(int x, int y)
{
    int sum = x;
    for(int i=0; i<y-1; i++)
    {
        sum *= x;
    }
    return sum;
}

int solution(string dart) {
    int ans = 0;
    int chk = 1;
    int val = 0;
    int pre = 0;
    
    for(int i=0; i<dart.length(); i++)
    {
        if(chk == 3)
        {
            if(dart[i] >= '0' && dart[i] <='9')
            {
                chk = 1;
                ans += val;
                pre = val;
                val = 0;
            }
        }
        
        if(chk == 1)
        {
            if(dart[i+1] == '0')
            {
                val = 10;
                i++;
            }
            else
            {
                val = dart[i] - 48;    
            }
            chk ++;
        }
        else if(chk == 2)
        {
            if(dart[i] == 'D')
            {
                val = pow(val, 2);
            }
            else if(dart[i] == 'T')
            {
                val = pow(val, 3);
            }
            chk++;
        }
        else if(chk == 3)
        {
            if(dart[i] == '*')
            {
                val *= 2;
                
                if(pre != 0)
                {
                    ans -= pre;
                    pre *= 2;
                    ans += pre;
                }
            }
            else if(dart[i] == '#')
            {
                val *= -1;    
            }
            
            ans += val;
            chk = 1;
            pre = val;
            val = 0;
        }
    }
    ans += val;
    
    return ans;
}