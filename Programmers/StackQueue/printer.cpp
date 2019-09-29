#include <string>
#include <vector>

using namespace std;

int solution(vector<int> v, int location) {
    int answer = 1;
    
    while(!v.empty())
    {
        int f = v.front();
        v.erase(v.begin());
        bool ck = true;
        
        for(int i=0; i<v.size(); i++)
        {
            if(f < v[i])
            {
                v.push_back(f);
                ck = false;
                break;
            }
        }
        
        if(ck)
        {
            if(location == 0)
            {
                break;
            }
            answer++;
        }
        location --;
        if(location < 0)
        {
            location = v.size() - 1;
        }
        
    }
    return answer;
}  
 
