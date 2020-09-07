#include <bits/stdc++.h>

using namespace std;

#define MAXN 100005
#define pb push_back
#define sz(v) ((int)(v).size())
 
int N;
int D[MAXN];
 
int bfs(int s, vector<int> con[], vector<int> conv[])
{
    for (int i=1;i<=N;i++) D[i] = 2e9;
    queue <int> que;
    D[s] = 0; que.push(s);
    while (!que.empty()){
        int q = que.front(); que.pop();
        for (int i=sz(con[q]);i--;){
            int t = con[q][i], v = conv[q][i];
            if (D[t] < 2e9) continue;
            D[t] = D[q] + v; que.push(t);
        }
    }
    int ret = 1;
    for (int i=2;i<=N;i++) if (D[ret] < D[i]) ret = i;
    return ret;
}
 
int main()
{
    int t;
    cin >> t;
    while(t--) {
        int a, b, da, db;
        scanf("%d %d %d %d %d", &N, &a, &b, &da, &db);

        vector <int> con[MAXN], conv[MAXN];
        for (int i=1;i<N;i++){
            int a, b, c=1; scanf("%d %d", &a, &b);
            con[a].pb(b); conv[a].pb(c);
            con[b].pb(a); conv[b].pb(c);
        }

        bfs(a, con, conv);
        if(D[b] <= da) {
            printf("Alice\n");
            continue;
        }

        int y = bfs(1, con, conv);
        int z = bfs(y, con, conv);
        if(da < (D[z] + 1) / 2 && db > 2 * da) {
            printf("Bob\n");
        } else printf("Alice\n");
    }
}