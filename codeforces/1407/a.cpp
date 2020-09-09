#include <iostream>

using namespace std;

int main() {
    // freopen("1.in", "r", stdin);
    int t;
    cin >> t;
    while(t--) {
        int a[1000], n;
        cin >> n;

        int zeros = 0, ones = 0;
        for(int i=0; i<n; i++) {
            cin >> a[i];
            if(a[i] == 0) zeros++;
            else ones++;
        }

        if(zeros >= ones) {
            cout << n/2 << '\n';
            for(int i=0; i<n/2; i++) cout << "0 ";
            cout << '\n';
        } else {
            if((n / 2) % 2 == 0) {
                cout << n/2 << '\n';
                for(int i=0; i<n/2; i++) cout << "1 ";
                cout << '\n';
            } else {
                cout << n/2+1 << '\n';
                for(int i=0; i<n/2+1; i++) cout << "1 ";
                cout << '\n';
            }
        }
    }
}