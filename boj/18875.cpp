#include <bits/stdc++.h>

using namespace std;

vector<int> color;

int get_color(int a) {
    if(color[a] == a) return a;
    return color[a] = get_color(color[a]);
}

void merge(int a, int b) {
    int pa = get_color(a), pb = get_color(b);
    color[pb] = pa;
}

int main() {
    freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<set<int>> in(N+1), out(N+1);
    while(M--) {
        int a, b;
        cin >> a >> b;
        in[b].insert(a);
        out[a].insert(b);
    }

    color.resize(N+1);
    for(int i=1; i<=N; i++) color[i] = i;

    set<int> alive;
    for(int i=1; i<=N; i++) alive.insert(i);

    queue<int> q;
    vector<bool> inq(N+1);
    for(int i=1; i<=N; i++) q.push(i), inq[i] = true;

    while(!q.empty()) {
        int i = q.front(); q.pop(); inq[i] = false;
        if(int(out[i].size()) >= 2) {
            int min_color = N + 1;
            for(int j : out[i]) {
                min_color = min(min_color, get_color(j));
            }
            set<int> tmp = out[i];
            for(int j : tmp) {
                if(j == min_color || out[i].find(j) == out[i].end()) continue;

                set<int> tmp1 = in[j];
                for(int k : tmp1) {
                    out[k].insert(min_color);
                    in[min_color].insert(k);
                    out[k].erase(j);
                    in[j].erase(k);

                    if(!inq[k]) q.push(k), inq[k] = true;
                }
                set<int> tmp2 = out[j];
                for(int k : tmp2) {
                    in[k].insert(min_color);
                    out[min_color].insert(k);
                    in[k].erase(j);
                    out[j].erase(k);

                    if(!inq[k]) q.push(k), inq[k] = true;
                }
                if(!inq[min_color]) q.push(min_color), inq[min_color] = true;

                merge(min_color, j);
                alive.erase(j);
            }
        }
    }

    for(int i=1; i<=N; i++) color[i] = get_color(i);

    vector<int> s;
    for(int a : alive) s.push_back(a);
    sort(s.begin(), s.end());
    s.erase(unique(s.begin(), s.end()), s.end());
    for(int i=1; i<=N; i++)
        color[i] = lower_bound(s.begin(), s.end(), color[i]) - s.begin() + 1;

    for(int i=1; i<=N; i++) cout << color[i] << '\n';

    return 0;
}