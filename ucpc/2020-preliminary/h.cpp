#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false), cin.tie(NULL);

    int N, h[100001];
    cin >> N;
    for(int i=1; i<=N; i++) cin >> h[i];

    int a = 0, b = 0, c = 0;
    for(int i=1; i<=N; i++) {
        a += h[i] % 2;
        b += h[i] / 2;
        c += h[i];
    }

    if(c % 3 == 0 && a <= b) cout << "YES";
    else cout << "NO";
}