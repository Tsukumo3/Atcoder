#include <iostream>
#include <string>

using namespace std;

int main(){
    
    string input;

    cin >> input;

    int last = input.size();

    string ans;

    if(input[last-1] == 'o' || input[last-1] == 'k' || input[last-1] == 'u'){
        ans = "YES";
    }
    else if(input[last-1] == 'h' && input[last-2] == 'c' ||){

    }
    else{
        ans = "NO";
    }

    cout << ans << endl;
}