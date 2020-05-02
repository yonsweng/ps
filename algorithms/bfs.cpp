// BOJ 2178 미로 탐색 https://www.acmicpc.net/problem/2178
#include <iostream>
#include <queue>

#define MAXN 102

using namespace std;

struct Location {
    int i, j, cnt;

    Location(int i, int j, int cnt) : i(i), j(j), cnt(cnt) {}
};

int main() {
//    freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int N, M, ans = 0;
    char c[MAXN][MAXN] = {};
    bool v[MAXN][MAXN] = {};
    queue<Location> q;
    pair<int, int> d[4] = {{1,  0},
                           {-1, 0},
                           {0,  1},
                           {0,  -1}};

    cin >> N >> M;
    for (int i = 1; i <= N; i++)
        for (int j = 1; j <= M; j++)
            cin >> c[i][j];

    q.emplace(1, 1, 1);
    v[1][1] = true;
    while (!q.empty()) {
        Location here = q.front();
        q.pop();
        for (int k = 0; k < 4; k++) {
            Location next = Location(here.i + d[k].first, here.j + d[k].second, here.cnt + 1);
            if (c[next.i][next.j] == '1' && !v[next.i][next.j]) {
                if (next.i == N && next.j == M) {
                    ans = next.cnt;
                    break;
                }
                v[next.i][next.j] = true;
                q.push(next);
            }
        }
        if (ans) break;
    }

    cout << ans;

    return 0;
}