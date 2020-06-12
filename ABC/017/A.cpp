#include <iostream>
#include <string>

//データ型に新しい名前（エイリアス、シノニム）をつける
typedef long long ll;

using namespace std;

int main(){
    int s[3];
    int e[3];
    for(int i=0; i<3; i++){
        cin >> s[i] >> e[i];
    }
    int ans = 0;

    for(int i=0; i<3; i++){
        ans = ans + s[i]*e[i]*0.1;
    }
    cout << ans << endl;
}