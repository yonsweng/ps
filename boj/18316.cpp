#include <bits/stdc++.h>

#define point(S, T) ((S) - C * (T) * (T))

using namespace std;

int s[1010][1010];
bool inq[1010][1010];

int main() {
    freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int N, M, C;
    int m[1010];
    vector<int> adj[1010];

    cin >> N >> M >> C;
    for(int i=1; i<=N; i++) cin >> m[i];
    for(int i=1; i<=M; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
    }

    queue<pair<int, int>> q;

    q.emplace(1, 0), inq[1][0] = true;

    while(!q.empty()) {
        pair<int, int> p = q.front(); q.pop();
        int here = p.first, t_here = p.second;
        inq[here][t_here] = false;
        for(int next : adj[here]) {
            int new_point = point(s[here][t_here] + m[next], t_here + 1);
            if(new_point > point(s[next][t_here + 1], t_here + 1) && new_point > 0) {
                s[next][t_here + 1] = s[here][t_here] + m[next];
                if(!inq[next][t_here + 1])
                    q.emplace(next, t_here + 1), inq[next][t_here + 1] = true;
            }
        }
    }

    int maximum = 0;
    for(int i=0; i<1010; i++)
        maximum = max(maximum, point(s[1][i], i));
    cout << maximum;
    return 0;
}