#include <bits/stdc++.h>
#define MAXN 501
using namespace std;

vector<int> adj[MAXN];
int visit_cnt, visited[MAXN];
int matched[MAXN];

int match(int from) {
    if(visited[from] == visit_cnt)
        return false;
    visited[from] = visit_cnt;

    for(int to : adj[from]) {
        if(!matched[to] || match(matched[to])) {
            matched[to] = from;
            return true;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(NULL);

    int N, K;
    cin >> N >> K;
    for(int i=0; i<K; i++) {
        int R, C;
        cin >> R >> C;
        adj[R].push_back(C);
    }

    int ans = 0;
    for(int i=1; i<=N; i++) {
        visit_cnt++;
        ans += match(i);
    }
    cout << ans;
}