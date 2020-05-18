#include <iostream>

using namespace std;

bool is_sq[10000001];

int main() {
    for(int i=0; i<=3162; i++) is_sq[i*i] = true;

    ios::sync_with_stdio(false), cin.tie(NULL);
    int T;
    cin >> T;
    for(int case_num=1; case_num<=T; case_num++) {
        int N, A[100001], S[100001] = {}, ans = 0;

        cin >> N;
        for(int i=1; i<=N; i++) cin >> A[i];

        for(int i=1; i<=N; i++) S[i] = S[i-1] + A[i];

        for(int i=1; i<=N; i++)
            for(int j=0; j<i; j++)
                if(S[i]-S[j] >= 0 && is_sq[S[i]-S[j]]) ans++;

        cout << "Case #" << case_num << ": " << ans << '\n';
    }
    return 0;
}