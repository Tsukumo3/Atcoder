#include <iostream>
using namespace std;

int main(){
    
    int n, s, t, w;
    cin >> n >> s >> t;
    
    int a[n];
    cin >> a[0];
   

    for(int i=1; i<n; i++){
        cin >> a[i];
    }

    w = 0;
    int ans = 0;

    for(int i=0; i<n; i++){
        w = w + a[i];
        if(s <= w && w <= t){
            ++ans;
        }
    }

    cout << ans << endl;
    return 0;
}