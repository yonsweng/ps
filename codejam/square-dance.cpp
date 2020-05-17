#include <iostream>
#include <vector>
#include <set>

using namespace std;

bool need_eli(int i, int j, vector<vector<int>> &s,
              vector<vector<int>> &l, vector<vector<int>> &r, vector<vector<int>> &u, vector<vector<int>> &d) {
    int sum = 0, cnt = 0;
    if (~l[i][j]) sum += s[i][l[i][j]], cnt++;
    if (~r[i][j]) sum += s[i][r[i][j]], cnt++;
    if (~u[i][j]) sum += s[u[i][j]][j], cnt++;
    if (~d[i][j]) sum += s[d[i][j]][j], cnt++;

    if (s[i][j] * cnt < sum) return true;
    else return false;
}

int main() {
//    freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int T;
    cin >> T;
    for (int case_num = 1; case_num <= T; case_num++) {
        int R, C;
        cin >> R >> C;

        set<pair<int, int>> c_eli;
        vector<vector<int>> s, l, r, u, d;
        s = l = r = u = d = vector<vector<int>>(R, vector<int>(C));
        long long sum = 0;

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                cin >> s[i][j];
                sum += s[i][j];
                l[i][j] = j - 1;
                r[i][j] = j + 1 < C ? j + 1 : -1;
                u[i][j] = i - 1;
                d[i][j] = i + 1 < R ? i + 1 : -1;
            }
        }

        for (int i = 0; i < R; i++)
            for (int j = 0; j < C; j++)
                if (need_eli(i, j, s, l, r, u, d)) c_eli.emplace(i, j);

        long long total = 0, interest = sum;
        for (bool eli = true; eli;) {
            set<pair<int, int>> c_eli_cp = c_eli;
            c_eli = {};
            eli = false;
            total += interest;

            for (pair<int, int> p : c_eli_cp) {
                int i = p.first, j = p.second;
                interest -= s[i][j];
                s[i][j] = 0;
                eli = true;
            }

            for (pair<int, int> p : c_eli_cp) {
                int i = p.first, j = p.second;
                if (~l[i][j]) {
                    r[i][l[i][j]] = r[i][j];
                    if (s[i][l[i][j]] && need_eli(i, l[i][j], s, l, r, u, d))
                        c_eli.emplace(i, l[i][j]);
                }
                if (~r[i][j]) {
                    l[i][r[i][j]] = l[i][j];
                    if (s[i][r[i][j]] && need_eli(i, r[i][j], s, l, r, u, d))
                        c_eli.emplace(i, r[i][j]);
                }
                if (~u[i][j]) {
                    d[u[i][j]][j] = d[i][j];
                    if (s[u[i][j]][j] && need_eli(u[i][j], j, s, l, r, u, d))
                        c_eli.emplace(u[i][j], j);
                }
                if (~d[i][j]) {
                    u[d[i][j]][j] = u[i][j];
                    if (s[d[i][j]][j] && need_eli(d[i][j], j, s, l, r, u, d))
                        c_eli.emplace(d[i][j], j);
                }
            }
        }
        cout << "Case #" << case_num << ": " << total << '\n';
    }

    return 0;
}