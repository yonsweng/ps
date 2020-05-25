#include <iostream>
#include <string>
using namespace std;
int main() {
    int A, B;
    string s;
    cin >> A >> B;
    if(A > B) s = ">";
    else if(A < B) s = "<";
    else s = "==";
    cout << s;
    return 0;
}