#include <iostream>
#include <string>

using namespace std;

int main(){
    
    int x;
    int y;

    cin >> x >> y;

    int ans;
    ans = max(x, y);

    printf("%d\n", ans);

    return 0;
}