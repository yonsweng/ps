#include <iostream>
#include <vector>
#include <queue>

#define MAXN 10

using namespace std;

int di[4] = {0, 0, 1, -1}, dj[4] = {1, -1, 0, 0};
int M, N;
int g[MAXN][MAXN], res[MAXN][MAXN];

int gogo(vector<pair<int, int>> &virus) {
    queue<pair<int, int>> q;
    for(pair<int, int> v : virus) {
        q.push(v);
    }

    while(!q.empty()) {
        pair<int, int> p = q.front();
        q.pop();

        int i = p.first, j = p.second;

        for(int k=0; k<4; k++) {
            int ii = i + di[k], jj = j + dj[k];

            if(g[ii][jj] == 0) {
                g[ii][jj] = 2;
                q.emplace(ii, jj);
            }
        }
    }

    int cnt = 0;
    for(int i=1; i<=N; i++) {
        for(int j=1; j<=M; j++) {
            if(g[i][j] == 0) {
                cnt += 1;
            }
        }
    }

    return cnt;
}

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    vector<pair<int, int>> empty, virus;

    cin >> N >> M;

    for(int i=1; i<=N; i++)
        g[i][0] = g[i][M+1] = 1;
    for(int j=1; j<=M; j++)
        g[0][j] = g[N+1][j] = 1;

    for(int i=1; i<=N; i++)
        for(int j=1; j<=M; j++) {
            cin >> g[i][j];
            res[i][j] = g[i][j];
            if(g[i][j] == 0)
                empty.emplace_back(i, j);
            else if(g[i][j] == 2)
                virus.emplace_back(i, j);
        }

    int max_safe = 0;
    for(int i=0; i<empty.size(); i++) {
        for(int j=i+1; j<empty.size(); j++) {
            for(int k=j+1; k<empty.size(); k++) {
                for(int ii=1; ii<=N; ii++)
                    for(int jj=1; jj<=M; jj++)
                        g[ii][jj] = res[ii][jj];

                g[empty[i].first][empty[i].second] = 1;
                g[empty[j].first][empty[j].second] = 1;
                g[empty[k].first][empty[k].second] = 1;
                max_safe = max(gogo(virus), max_safe);
            }
        }
    }

    cout << max_safe;
}