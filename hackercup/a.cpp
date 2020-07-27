#include <iostream>
#include <vector>

using namespace std;

int main() {
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int T;
    cin >> T;
    for(int case_num=1; case_num<=T; case_num++) {
        int N;
        cin >> N;

        vector<char> I(N+1), O(N+1);
        for(int i=1; i<=N; i++) cin >> I[i];
        for(int i=1; i<=N; i++) cin >> O[i];

        char P[51][51];
        for(int i=1; i<=N; i++) {
            P[i][i] = 'Y';
            for(int j=i-1; j>=1; j--) {
                if(I[j] == 'Y' && O[j+1] == 'Y') {
                    P[i][j] = 'Y';
                } else {
                    for(int k=j; k>=1; k--) {
                        P[i][k] = 'N';
                    }
                    break;
                }
            }
            for(int j=i+1; j<=N; j++) {
                if(I[j] == 'Y' && O[j-1] == 'Y') {
                    P[i][j] = 'Y';
                } else {
                    for(int k=j; k<=N; k++) {
                        P[i][k] = 'N';
                    }
                    break;
                }
            }
        }

        cout << "Case #" << case_num << ":\n";
        for(int i=1; i<=N; i++) {
            for(int j=1; j<=N; j++) {
                cout << P[i][j];
            }
            cout << '\n';
        }
    }
}