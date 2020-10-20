#include <bits/stdc++.h>
using namespace std;

int C[1001][1001];

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);
    int T;
    cin >> T;
    for(int x=1; x<=T; x++) {
        long long answer = 0;
        int N;

        cin >> N;
        for(int i=1; i<=N; i++)
            for(int j=1; j<=N; j++)
                cin >> C[i][j];

        for(int k=1; k<=N; k++) {
            long long sum = 0;
            for(int i=1; i<=k; i++) {
                int j=N-k+i;
                sum += C[i][j];
            }
            answer = max(answer, sum);
        }
        for(int k=N-1; k>=1; k--) {
            long long sum = 0;
            for(int j=1; j<=k; j++) {
                int i=N-k+j;
                sum += C[i][j];
            }
            answer = max(answer, sum);
        }

        cout << "Case #" << x << ": " << answer << '\n';
    }
}