#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct ijk {
    int i, j, k;
    ijk(int i, int j, int k) : i(i), j(j), k(k) {}
};

bool is_valid(int i, int j, int k, int m, int n) {
    if(i >= 0 && j >= 0 && i < m && j < n && k < m * n) return true;
    else return false;
}

int to_idx(int i, int j, int k, int m, int n) {
    return (i * n + j) * m * n + k;
}

vector<int> solution(int m, int n, int s, vector<vector<int>> time_map) {
    const int INF = 2147483647;
    pair<int, int> adj[4] = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};

    // min_map[i][j][k]: (i, j)에 k번만에 도착할 때 최소 비용
    vector<vector<vector<int>>> min_map(m);
    for(int i=0; i<m; i++) {
        min_map[i].resize(n);
        for(int j=0; j<n; j++) {
            min_map[i][j].resize(m*n);
            for(int k=0; k<m*n; k++)
                min_map[i][j][k] = INF;
        }
    }
    min_map[0][0][0] = 0;

    queue<ijk> q;
    vector<bool> in_q(m*n*m*n, false);
    q.emplace(0, 0, 0);
    in_q[to_idx(0, 0, 0, m, n)] = true;

    while(!q.empty()) {
        ijk now = q.front(); q.pop();
        in_q[to_idx(now.i, now.j, now.k, m, n)] = false;

        for(int l=0; l<4; l++) {
            ijk next = {now.i + adj[l].first, now.j + adj[l].second, now.k + 1};

            if(!is_valid(next.i, next.j, next.k, m, n)) continue;

            long long next_cost = min_map[now.i][now.j][now.k] + time_map[next.i][next.j];

            if(next_cost <= s
                && time_map[next.i][next.j] != -1
                && next_cost < min_map[next.i][next.j][next.k]) {

                min_map[next.i][next.j][next.k] = next_cost;

                if(!in_q[to_idx(next.i, next.j, next.k, m, n)]) {
                    q.push(next);
                    in_q[to_idx(next.i, next.j, next.k, m, n)] = true;
                }
            }
        }
    }

    
    vector<int> answer(2);

    for(int k=0; k<m*n; k++) {
        if(min_map[m-1][n-1][k] < INF) {
            answer[0] = k;
            answer[1] = min_map[m-1][n-1][k];
            break;
        }
    }

    return answer;
}

int main() {
    freopen("1.in", "r", stdin);

    int m, n, s;
    cin >> m >> n >> s;

    vector<vector<int>> time_map(m);
    for(int i=0; i<m; i++) {
        time_map[i].resize(n);
        for(int j=0; j<n; j++)
            cin >> time_map[i][j];
    }

    vector<int> answer = solution(m, n, s, time_map);
    for(int a : answer)
        cout << a << ' ';

    return 0;
}