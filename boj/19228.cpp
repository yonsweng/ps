#include <iostream>
#include <set>
#include <vector>

using namespace std;

long long comb(int n, int r) {
    if(n < r) return 0;
    
    long long c = 1;
    for(int i=n; i>n-r; i--) {
        c *= i;
    }
    for(int i=r; i>1; i--) {
        c /= i;
    }
    return c;
}

int main() {
    // freopen("1.in", "r", stdin);

    int t;
    cin >> t;
    while(t--) {
        long long k;
        cin >> k;

        multiset<int> fp;
        for(int i = 2; k > 0; i++) {
            fp.insert(k % i);
            k /= i;
        }

        vector<pair<int, int>> v;  // {remainder, cnt}
        for(int elt : fp) {
            if(!v.empty() && v[int(v.size())-1].first == elt) {
                v[int(v.size())-1].second++;
            } else {
                v.push_back({elt, 1});
            }
        }

        long long all = 1, zero_end, answer;

        for(int i=int(v.size())-1, n=fp.size(); i>0; i--) {
            all = all * comb(n + 1 - v[i].first, v[i].second);
            n -= v[i].second;
        }

        if(v[0].first == 0) {
            zero_end = 1;
            for(int i=int(v.size())-1, n=fp.size(); i>0; i--) {
                zero_end *= comb(n - v[i].first, v[i].second);
                n -= v[i].second;
            }
        } else {
            zero_end = 0;
        }

        answer = all - zero_end - 1;
        cout << answer << '\n';
    }
}