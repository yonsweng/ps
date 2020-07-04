#include <iostream>
#include <cmath>
#include <queue>

using namespace std;

struct ij {
    int i, j;
    ij(int i, int j) : i(i), j(j) {}
} d[4] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

int n, m;
int a[300][300];

bool is_valid(int i, int j) {
    if(i >= 0 && i < n && j >= 0 && j < m) return true;
    else return false;
}

int find_pos_neighbors(int i, int j) {
    int cnt = 0;
    for(int k=0; k<4; k++)
        if(is_valid(i+d[k].i, j+d[k].j) && a[i+d[k].i][j+d[k].j] > 0) cnt++;
    return cnt;
}

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int t;
    cin >> t;
    while(t-- > 0) {
        cin >> n >> m;

        queue<ij> q;
        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++) {
                cin >> a[i][j];
                if(a[i][j] > 0) q.emplace(i, j);
            }

        bool fail = false;
        while(!q.empty()) {
            ij now = q.front(); q.pop();
            int pos_neighbors = find_pos_neighbors(now.i, now.j);
            if(a[now.i][now.j] > pos_neighbors) {
                int cnt = a[now.i][now.j] - pos_neighbors;
                for(int k=0; k<4 && cnt > 0; k++) {
                    if(is_valid(now.i+d[k].i, now.j+d[k].j)
                    && a[now.i+d[k].i][now.j+d[k].j] == 0) {
                        cnt--;
                        a[now.i+d[k].i][now.j+d[k].j] = 1;
                        q.emplace(now.i+d[k].i, now.j+d[k].j);
                    }
                }
                if(cnt > 0) {
                    fail = true;
                    break;
                }
            } else if(a[now.i][now.j] < pos_neighbors)
                a[now.i][now.j] = pos_neighbors;
        }

        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
                if(a[i][j]) a[i][j] = find_pos_neighbors(i, j);

        if(fail) cout << "NO\n";
        else {
            cout << "YES\n";
            for(int i=0; i<n; i++) {
                for(int j=0; j<m; j++)
                    cout << a[i][j] << ' ';
                cout << '\n';
            }
        }
    }

    return 0;
}