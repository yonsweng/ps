#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL), ios::sync_with_stdio(false);

    int T;
    cin >> T;
    while(T-- > 0) {
        int A, B;
        cin >> A >> B;
        cout << A + B << '\n';
    }

    return 0;
}