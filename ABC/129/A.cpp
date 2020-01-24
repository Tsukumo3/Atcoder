#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

int main()
{
   int p,q,r;
   cin >> p>>q>>r;

   int ans;
   ans = min(p+q, min(q+r, r+p));

   cout << ans << endl;

}