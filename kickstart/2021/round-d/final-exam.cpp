#include <iostream>
#include <set>
#include <vector>

using namespace std;

void insert(set<pair<long long, long long> > &ps, long long a, long long b) {
    if(a <= b)
        ps.insert(make_pair(a, b));
}

int main() {
    int T;
    cin >> T;

    for(int x = 1; x <= T; x++) {
        int N, M;
        cin >> N >> M;

        set<pair<long long, long long> > ps;

        for(int i=0; i<N; i++) {
            long long A, B;
            cin >> A >> B;

            ps.insert(make_pair(A, B));
        }

        vector<long long> ys;

        for(int j=0; j<M; j++) {
            long long S;
            cin >> S;

            pair<long long, long long> pivot = make_pair(S, S);
            set<pair<long long, long long> >::iterator r = ps.lower_bound(pivot);
            if(r == ps.begin()) {
                long long a = (*r).first + 1;
                long long b = (*r).second;
                ps.erase(*r);
                insert(ps, a, b);
                ys.push_back(a - 1);
            } else if(r == ps.end()) {
                r--;
                if(S < (*r).second) {
                    long long a = (*r).first;
                    long long b = S - 1;
                    long long c = S + 1;
                    long long d = (*r).second;
                    ps.erase(*r);
                    insert(ps, a, b);
                    insert(ps, c, d);
                    ys.push_back(S);
                } else {
                    long long a = (*r).first;
                    long long b = (*r).second - 1;
                    ps.erase(*r);
                    insert(ps, a, b);
                    ys.push_back(b + 1);
                }
            } else {
                set<pair<long long, long long> >::iterator l = r;
                l--;

                if(S < (*l).second) {
                    long long a = (*l).first;
                    long long b = S - 1;
                    long long c = S + 1;
                    long long d = (*l).second;
                    ps.erase(*l);
                    insert(ps, a, b);
                    insert(ps, c, d);
                    ys.push_back(S);
                } else if(S - (*l).second <= (*r).first - S) {
                    long long a = (*l).first;
                    long long b = (*l).second - 1;
                    ps.erase(*l);
                    insert(ps, a, b);
                    ys.push_back(b + 1);
                } else {
                    long long a = (*r).first + 1;
                    long long b = (*r).second;
                    ps.erase(*r);
                    insert(ps, a, b);
                    ys.push_back(a - 1);
                }
            }
        }

        cout << "Case #" << x << ':';
        for(long long y : ys)
            cout << ' ' << y;
        cout << '\n';
    }
    return 0;
}