#include <iostream>

#define INF 1000000001

using namespace std;

int main() {
    ios::sync_with_stdio(false), cin.tie(NULL);

    int t;
    cin >> t;
    while(t--) {
        int x, y, z;
        cin >> x >> y >> z;

        int a, b, c;
        bool yes = false;
        if(x == y && y == z) {
            yes = true;
            a = b = c = x;
        } else if(x == y && y > z) {
            yes = true;
            a = x;
            b = z;
            c = z;
        } else if(x < y && y == z) {
            yes = true;
            c = y;
            a = x;
            b = x;
        } else if(x == z && z > y) {
            yes = true;
            b = x;
            a = y;
            c = y;
        }

        if(yes) {
            cout << "YES\n";
            cout << a << ' ' << b << ' ' << c << '\n';
        } else {
            cout << "NO\n";
        }
    }
    return 0;
}