#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> h) {
    vector<int> ans;
    
    for(int i=0; i<h.size(); i++)
    {
        bool chk = true;
        for(int j=i-1; j>=0; j--)
        {
            if(h[i] < h[j])
            {
                ans.push_back(j+1);
                chk = false;
                break;
            }
        }
        
        if(chk)
        {
            ans.push_back(0);
        }
    }
    return ans;
}