#include <iostream>
#include <map>

using namespace std;

int main() {
    map<int, int> m;

    m[1] = 2;

    cout << (m.find(1) == m.end());
}