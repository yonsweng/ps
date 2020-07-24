#include <iostream>
#include <deque>

using namespace std;

int main() {
    freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int N, M, K, Q;
    cin >> N >> M >> K >> Q;

    deque<pair<int, long long>> A;
    for(int i=0; i<N; i++) {
        int a;
        cin >> a;
        if(a == A.back().first) {
            A.back().second ++;
        } else {
            A.emplace_back(a, 1);
        }
    }

    while(Q--) {
        int o;
        cin >> o;
        if(o == 1) {
            int L, R;
            cin >> L >> R;
        } else if(o == 2) {
            int i;
            cin >> i;
        } else if(o == 3) {
            int p; long long q;
            cin >> p >> q;
        } else {
            int t;
            cin >> t;
        }
    }
}