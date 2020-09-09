#include <iostream>

using namespace std;

int remained(bool check[], int n) {
    for(int i=1; i<=n; i++) {
        if(!check[i])
            return i;
    }
    return 0;
}

int main() {
    int n, p[10001];
    bool check[10001] = {};

    cin >> n;

    int left, right;
    for(left = 1, right = 2; right <= n; right++) {
        int mod1, mod2;

        cout << "? " << left << ' ' << right << endl;
        cin >> mod1;

        cout << "? " << right << ' ' << left << endl;
        cin >> mod2;

        if(mod1 < mod2) {
            p[right] = mod2;
            check[mod2] = true;
        } else {
            p[left] = mod1;
            left = right;
            check[mod1] = true;
        }
    }

    p[left] = remained(check, n);

    cout << "! ";
    for(int i=1; i<=n; i++) {
        cout << p[i] << ' ';
    }
    cout << endl;
}
