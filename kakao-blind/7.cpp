#include <string>
#include <vector>
#include <map>

#define INF 2147483647
#define MAXN 600002
#define S 0
#define E (2*n+1)

using namespace std;

vector<int> adj[MAXN];
map<int, int> cap[MAXN], flow[MAXN], dist[MAXN];

int solution(vector<int> sales, vector<vector<int>> links) {
    int answer = 0;
    int n = sales.size();
    
    // src -> 1~n
    for(int i=1; i<=n; i++) {
        adj[S].push_back(i);
        adj[i].push_back(S);
        cap[S][i] = INF;
        cap[i][S] = 0;
        flow[S][i] = 0;
        flow[i][S] = 0;
        dist[S][i] = sales[i-1];
        dist[i][S] = 0;
    }
    
    for(auto link : links) {
        adj[link[0]].push_back(n+link[0]);
        adj[n+link[0]].push_back(link[0]);
        cap[link[0]][n+link[0]] = 1;
        cap[n+link[0]][link[0]] = 0;
        flow[link[0]][n+link[0]] = 0;
        flow[n+link[0]][link[0]] = 0;
        dist[link[0]][n+link[0]] = 0;
        dist[n+link[0]][link[0]] = 0;
        
        adj[link[1]].push_back(n+link[0]);
        adj[n+link[0]].push_back(link[1]);
        cap[link[1]][n+link[0]] = 1;
        cap[n+link[0]][link[1]] = 0;
        flow[link[1]][n+link[0]] = 0;
        flow[n+link[0]][link[1]] = 0;
        dist[link[1]][n+link[0]] = 0;
        dist[n+link[0]][link[1]] = 0;
    }
    
    // group -> sink
    for(int i=n+1; i<=2*n; i++) {
        adj[i].push_back(E);
        adj[E].push_back(i);
        cap[i][E] = 1;
        cap[E][i] = 0;
        flow[i][E] = 0;
        flow[E][i] = 0;
        dist[i][E] = 0;
        dist[E][i] = 0;
    }
    
    int min_swaps = 0;
    while(1) {
        // SPFA
        queue<int> q; int d[MAXN], p[MAXN]; bool inq[MAXN] = {};
        fill_n(d, n+2, INF), fill_n(p, n+2, -1);
        q.push(S), d[S] = 0, inq[S] = true;
        while(!q.empty()) {
            int u = q.front(); q.pop(), inq[u] = false;
            for(int v : adj[u]) {
                int e = d[u] + dist[u][v] * (flow[u][v] >= 0 ? 1 : -1);
                if(cap[u][v] - flow[u][v] > 0 && d[v] > e) {
                    d[v] = e, p[v] = u;
                    if(!inq[v]) q.push(v), inq[v] = true;
                }
            }
        }
        if(p[E] == -1) break;  // If no path.

        // Flow
        for(int u=E; p[u]!=-1; u=p[u]) {
            min_swaps += dist[p[u]][u] * (flow[p[u]][u] >= 0 ? 1 : -1);
            flow[p[u]][u]++, flow[u][p[u]]--;
        }
    }
    cout << min_swaps << '\n';
    
    return answer;
}