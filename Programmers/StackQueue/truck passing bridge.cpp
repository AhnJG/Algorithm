#include <string>
#include <vector>

using namespace std;

int sum_vec(vector<int> vec)
{
    int sum = 0;
    
    if(vec.empty())
    {
        return 0;
    }
    
    for(int i=0; i<vec.size(); i++)
    {
        sum += vec[i];
    }
    
    return sum;
}

int solution(int bridge_length, int weight, vector<int> truck) {
    int ans = 0;
    
    vector<int> on_bridge;
    vector<int> chk_time;
    
    // on_bridge.push_back(truck[0]);
    // chk_time.push_back(0);
    
    //(chk_time.size()==1 && chk_time[0]+1 == bridge_length)
    while(!(truck.empty() && on_bridge.empty()))
    {
        ans++;
        
        if(!chk_time.empty())
        {
            for(int i=0; i<chk_time.size(); i++)
            {
                chk_time[i] += 1;
            }
            
            if(chk_time[0] == bridge_length)
            {
                on_bridge.erase(on_bridge.begin());
                chk_time.erase(chk_time.begin());
            }
        }
        
        if(!truck.empty())
        {
            if(sum_vec(on_bridge)+truck[0] <= weight)
            {
                on_bridge.push_back(truck[0]);
                truck.erase(truck.begin());
                chk_time.push_back(0);   
            }                
        }
        
        
        // if(ans == 100)
        // {
        //     return ans;
        // }
    }
    
    return ans;
}