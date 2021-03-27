#include <bits/stdc++.h>

using namespace std;

void my_reverse(int L[], int i, int j) {
    for(int k=i; k<=int(floor((j+i-1)/2.0)); k++) {
        int tmp = L[k];
        L[k] = L[j-k+i];
        L[j-k+i] = tmp;
    }
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int T;
    cin >> T;
    for(int x = 1; x <= T; x++) {
        int N, C;
        cin >> N >> C;

        int L[101];
        for(int i=1; i<=N; i++) {
            L[i] = i;
        }

        bool possible = true;
        for(int i=N-1; i>=1; i--) {
            int quota = min(C-i+1, N-i+1);
            if(quota <= 0) {
                possible = false;
                break;
            }
            my_reverse(L, i, i+quota-1);
            C -= quota;
        }
        if(C > 0) {
            possible = false;
        }

        cout << "Case #" << x << ": ";
        if(possible) {
            for(int i=1; i<=N; i++) {
                cout << L[i] << ' ';
            }
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << '\n';
    }
}