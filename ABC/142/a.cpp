#include <iostream>

using namespace std;

int main()
{
  int n;
  cin >> n;
  int a;
  a = n%2;
  std::cout << a << '\n';
  if(a==1)
  {
    double amari = ((n-1)/2+1)/n;
    std::cout << amari << '\n';
  }
  else
  {
    double amari = 0.5;
    std::cout << amari << '\n';
  }

}
