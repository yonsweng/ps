#include <iostream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    while(!cin.eof()) {
        string line;
        getline(cin, line);

        istringstream in(line);
        int a = -1, b = -1;
        in >> a >> b;

        if(a == -1 && b == -1) break;

        cout << a + b << '\n';
    }
}