#include <iostream>
#include <vector>
#include <queue>

#define MAXN 500
#define INF 1e9

using namespace std;

int main()
{
    // freopen("1.in", "r", stdin);
    int F;
    cin >> F;
    while(F--) {
        int N, M, W, S, E, T;
        cin >> N >> M >> W;
        vector<vector<pair<int, int>>> adj(N+1);
        while(M--) {
            cin >> S >> E >> T;
            adj[S].emplace_back(E, T);
            adj[T].emplace_back(S, T);
        }
        while(W--) {
            cin >> S >> E >> T;
            adj[S].emplace_back(E, -T);
        }

        bool cycle = false;
        vector<int> dist(N+1, INF);
        dist[1] = 0;
        for(int i=1; i<=N; i++) {
            bool updated = false;
            for(int s=1; s<=N; s++) {
                for(pair<int, int> tmp : adj[s]) {
                    int e = tmp.first, w = tmp.second;
                    if(dist[e] > dist[s] + w) {
                        dist[e] = dist[s] + w;
                        if(i == N) {
                            cycle = true;
                            break;
                        }
                    }
                }
                if(cycle) break;
            }
        }
        if(cycle) cout << "YES\n";
        else cout << "NO\n";
    }
	return 0;
}