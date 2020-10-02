#include <iostream>
#include <string>

using namespace std;

int main(){

    int x;

    cin >> x;

    string s;

    if (x >= 1200)
    {
        s = "ARC";
    }
    else
    {
        s = "ABC";
    }

    cout << s << endl;

    return 0;
}
