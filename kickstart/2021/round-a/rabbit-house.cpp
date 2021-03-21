#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

const pair<int, int> d[4] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int G[302][302];
vector<pair<int, int>> V[2000001];

bool is_valid(int i, int j, int R, int C) {
    if(i >= 1 && i <= R && j >= 1 && j <= C) return true;
    else return false;
}

int main() {
    freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);
    int T;
    cin >> T;
    for(int x=1; x<=T; x++) {
        int R, C;
        cin >> R >> C;
        for(int i=1; i<=R; i++)
            for(int j=1; j<=C; j++)
                cin >> G[i][j];

        for(int i=1; i<=R; i++)
            for(int j=1; j<=C; j++)
                if(G[i][j] >= 2)
                    V[G[i][j]].emplace_back(i, j);


        long long y = 0;
        bool check[90301];

        for(int k=2000000; k>=2; k--) {
            bool inited = false;
            vector<pair<int, int>> indices;
            for(auto ij : V[k]) {
                int si = ij.first, sj = ij.second;
                if(G[si][sj] != k) continue;
                if(!inited) {
                    memset(check, 0, sizeof(bool) * 90301);
                    inited = true;
                }
                for(int l=0; l<4; l++) {
                    int ni = si + d[l].first, nj = sj + d[l].second;
                    if(is_valid(ni, nj, R, C) && !check[ni * C + nj] && G[ni][nj] < G[si][sj] - 1) {
                        y += (G[si][sj] - 1) - G[ni][nj];
                        G[ni][nj] = G[si][sj] - 1;
                        check[ni * C + nj] = true;
                        indices.emplace_back(ni, nj);
                    }
                }
            }
            V[k].clear();
            for(auto ij : indices) {
                int i = ij.first, j = ij.second;
                V[k-1].emplace_back(i, j);
            }
        }

        cout << "Case #" << x << ": " << y << '\n';
    }
}