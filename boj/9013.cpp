#include <iostream>
#include <vector>
#include <algorithm>

#define MAX_N 100000
#define MAX_K 100

using namespace std;

int N, K;
int values[MAX_N], parents[MAX_N];
vector<int> adj[MAX_N];
int d[MAX_N][MAX_K+1][2];

int dp(int cur) {
    int n_nodes = 1;
    d[cur][1][1] = values[cur];

    for(int next : adj[cur]) {
        int n_next = dp(next);
        n_nodes += n_next;

        for(int k=min(K, n_nodes); k>0; k--) {
            for(int j=0; j<=k; j++)
                d[cur][k][0] = max(d[cur][k][0], d[cur][k-j][0] + max(d[next][j][0], d[next][j][1]));
            for(int j=0; j<k; j++)
                d[cur][k][1] = max(d[cur][k][1], d[cur][k-j][1] + d[next][j][0]);
        }
    }

    return n_nodes;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(NULL);

    int T;
    cin >> T;

    while (T--) {
        cin >> N >> K;
        for(int i=0; i<N; i++) cin >> values[i];
        for(int i=1; i<N; i++) cin >> parents[i];

        // init
        for(int i=0; i<N; i++)
            adj[i].clear();
        for(int i=0; i<N; i++)
            for(int j=0; j<=K; j++)
                d[i][j][0] = d[i][j][1] = 0;

        int max_value = *max_element(values, values + N);
        if(max_value <= 0) {
            cout << max_value << '\n';
            continue;
        }

        for(int child=1; child<N; child++)
            adj[parents[child]].push_back(child);

        dp(0);

        int answer = 0;
        for(int i=0; i<=K; i++)
            answer = max(answer, max(d[0][i][0], d[0][i][1]));

        cout << answer << '\n';
    }
}
