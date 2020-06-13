#include <iostream>
#include <vector>

using namespace std;

int N, W, C, H, M;
bool h[2002], m[2002];
vector<int> adj[2002][31];
bool visit[2002][2002];

bool dfs(int h, int a) {
    if(visit[h][a]) return false;
    visit[h][a] = true;

    if(m[h] && m[a]) return true;  // arrived

    bool ret = false;
    if(h == a) {  // go together
        for(int c=1; c<=C; c++)
            for(int t : adj[h][c])
                ret = (ret || dfs(t, t));
    } else {
        for(int c=1; c<=C; c++)
            for(int ht : adj[h][c])
                for(int at : adj[a][c])
                    ret = (ret || dfs(ht, at));
    }

    return ret;
}

int main() {
    // freopen("1.in", "r", stdin);

    cin >> N >> W >> C >> H >> M;
    int tmp;
    for(int i=0; i<H; i++) {
        cin >> tmp;
        h[tmp] = true;
    }
    for(int i=0; i<M; i++) {
        cin >> tmp;
        m[tmp] = true;
    }
    for(int i=0; i<W; i++) {
        int s, c, t;
        cin >> s >> c >> t;
        adj[s][c].push_back(t);
    }

    for(int i=0; i<N; i++)
        if(h[i]) {
            m[N] = (m[i] || m[N]);
            for(int c=1; c<=C; c++)
                for(int t : adj[i][c])
                    adj[N][c].push_back(t);
        } else {
            m[N+1] = (m[i] || m[N+1]);
            for(int c=1; c<=C; c++)
                for(int t : adj[i][c])
                    adj[N+1][c].push_back(t);
        }

    if(dfs(N, N+1)) cout << "YES";
    else cout << "NO";

    return 0;
}