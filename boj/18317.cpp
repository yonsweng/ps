#include <iostream>
#include <cstring>

#define MAXN 5002

using namespace std;

int cnt[MAXN][MAXN], h[4000001];
long long answer[MAXN][MAXN];
int N;

int main() {
    // freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int Q, A[5001];
    cin >> N >> Q;
    for(int i=1; i<=N; i++)
        cin >> A[i];

    const int BIAS = 2000000;
    for(int i=1; i<=N-2; i++) {
        for(int j=i+2; j<=N; j++) {
            h[A[j-1] + BIAS]++;
            cnt[i][j] = h[-(A[i] + A[j]) + BIAS];
        }
        for(int j=i+2; j<=N; j++)
            h[A[j-1] + BIAS]--;
    }

    // cnt[i][j] : A[i]와 A[j]를 포함하고 A[i...j]로 0을 만드는 경우의 수.
    // cnt_a[i][j] : A[i]를 포함하고 A[i...j]로 0을 만드는 경우의 수.
    // cnt_b[i][j] : A[j]를 포함하고 A[i...j]로 0을 만드는 경우의 수.
    // answer[i][j] : A[i...j]로 0을 만드는 경우의 수.

    for(int k=2; k<N; k++) {
        for(int i=1; i<=N-k; i++) {
            int j = i + k;
            answer[i][j] = cnt[i][j] + answer[i][j-1] + answer[i+1][j] - answer[i+1][j-1];
        }
    }

    for(int i=1; i<=Q; i++) {
        int a, b;
        cin >> a >> b;
        cout << answer[a][b] << '\n';
    }

    return 0;
}