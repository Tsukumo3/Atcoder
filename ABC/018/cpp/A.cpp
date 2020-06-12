#include <iostream>
#include <vector>
#include <algorithm>

#define rep(i,n) for(int i=0; i<n; i++)

using namespace std;

int main(){
    
    int input;

    vector<int> before, after;

    rep(i, 3)
    {
        cin >> input;
        before.push_back(input);
        after.push_back(input);
    }

    sort(after.begin(), after.end(), std::greater<int>());

    rep(i, 3){
        rep(j, 3){
            //cout << before[i] << " " << after[j] << endl; 
            if(before[i] == after[j]){
                cout << j+1 << endl; 
                break;
            }
        }
    }
    return 0;
}