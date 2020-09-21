#include <iostream>
#include <string>

using namespace std;

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int P;
    cin >> P;

    while(P--) {
        int R;
        string S;
        cin >> R >> S;

        for(char c : S) {
            for(int i=0; i<R; i++) {
                cout << c;
            }
        }
        cout << '\n';
    }
}