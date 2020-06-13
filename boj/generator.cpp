#include <iostream>

using namespace std;

int main() {
    freopen("1.in", "w", stdout);
    cout << "500 500\n";
    for(int i=1; i<=500; i++)
        cout << i << ' ' << i+1 << ' ' << -10000 << '\n';
    cout << "500 1 -10000\n";
    return 0;
}