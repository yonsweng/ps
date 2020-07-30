#include <bits/stdc++.h>

using namespace std;

struct Contest {
    int s, e;
    Contest() {}
    Contest(int s, int e) : s(s), e(e) {}
    bool operator<(const Contest &a) const {
        if(e < a.e) return true;
        else if(e == a.e && s < a.s) return true;
        else return false;
    }
};

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    // read the input
    int n, k;
    cin >> n >> k;
    vector<Contest> contests(n);
    for(int i=0; i<n; i++)
        cin >> contests[i].s >> contests[i].e;

    // sort by the end day
    sort(contests.begin(), contests.end());

    multiset<Contest> chosen;
    int hs_e = 0, answer = 0;
    for(int i=0; i<n; i++) {
        // if we can choose hyungseob
        if(hs_e < contests[i].s) {
            // if we can pull from chosen
            if(!chosen.empty() && chosen.begin()->e < contests[i].s) {
                auto it = chosen.upper_bound(Contest(0, contests[i].s));
                chosen.erase(--it);
                chosen.insert(contests[i]);
            } else {
                if(chosen.size() == k - 1) {
                    // choose hyungseob
                    hs_e = contests[i].e;
                    answer++;
                } else
                    chosen.insert(contests[i]);
            }
        }
    }
    cout << answer;
    return 0;
}

/*
7 2
1 2
2 3
3 4
4 5
5 6
6 7
7 8
2

7 1
1 2
2 3
3 4
4 5
5 6
6 7
7 8
4

7 3
1 2
2 3
3 4
4 5
5 6
6 7
7 8
0

1 1
500 1000
1

1 100
500 1000
0
*/