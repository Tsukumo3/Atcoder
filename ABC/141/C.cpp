#include <iostream>
#include <string>

using namespace std;

int main(){

    int n,k,q;
    int a[q];
    int p[n];

    //input
    cin >> n >> k >> q;
    for(int i = 0; i < q; i++)
    {
      cin >> a[i];
    }

    for(int i = 0; i < n; i++)
    {
      p[i] = 1-k;
    }


    for(int i = 0; i < q;i++)
    {
      p[a[i]-1] = p[a[i]-1] + 1;
    }

    for(int i = 0; i < n;i++)
    {
      printf("%d\n",p[i]);
      if(p[i] > 0)
      {
        printf("Yes\n");
      }
      else
      {
        printf("No\n");
      }
    }


    return 0;
}
