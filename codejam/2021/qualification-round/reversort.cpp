#include <bits/stdc++.h>

using namespace std;

int find_min_idx(int L[], int i, int N) {
    int min_val = L[i], min_idx = i;
    for(int j=i+1; j<=N; j++) {
        if(L[j] < min_val) {
            min_val = L[j];
            min_idx = j;
        }
    }
    return min_idx;
}

void my_reverse(int L[], int i, int j) {
    for(int k=i; k<=floor((j+i-1)/2.0); k++) {
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
        int N, L[101];
        cin >> N;
        for(int i=1; i<=N; i++) {
            cin >> L[i];
        }

        int y = 0;
        for(int i=1; i<=N-1; i++) {
            int j = find_min_idx(L, i, N);
            y += j - i + 1;
            my_reverse(L, i, j);
        }
        cout << "Case #" << x << ": " << y << '\n';
    }
}