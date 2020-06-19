#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    
    int n;
    int a[4] = {1, 2, 4, 8};

    cin >> n;

    int now = 3;

    vector<int> ans;

    while(n != 0)
    {
        if(n >= a[now])
        {
            n = n - a[now];
            ans.push_back(a[now]);
        }
        else
        {
            if(now >= 0)
            {
                now = now - 1;
            }
            else
            {
                break;
            }
        }

    }

    cout << ans.size() << endl;
    
    for(int i=0; i < ans.size(); i++){
        cout << ans[i] << endl;
    }

    return 0;
}