#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int case_num=1; case_num<=T; case_num++) {
        int N, K, A[200000];
        cin >> N >> K;
        for(int i=0; i<N; i++) cin >> A[i];

        int i = 0, cnt = 0;
        while(i < N) {
            if(A[i] == K) {
                int j;
                for(j=K-1; j>=1; j--)
                    if(A[++i] != j) break;
                if(j == 0) cnt++;
                continue;
            }
            i++;
        }
        cout << "Case #" << case_num << ": " << cnt << '\n';
    }
    return 0;
}