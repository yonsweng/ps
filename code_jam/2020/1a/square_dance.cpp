// long long caution
#include <iostream>

using namespace std;
int R, C;
pair<int, int> d[4] = {{-1, 0},
                       {1,  0},
                       {0,  -1},
                       {0,  1}};

int rc_to_idx(int r, int c) {
    return (r - 1) * C + c;
}

int main() {
    freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int T;
    cin >> T;
    for (int case_num = 1; case_num <= T; case_num++) {
        int s[100001] = {}, ss[100001] = {};

        cin >> R >> C;
        for (int r = 1; r <= R; r++) {
            for (int c = 1; c <= C; c++)
                cin >> s[rc_to_idx(r, c)];
        }

        long long interest = 0;
        for (int round = 1; ; round++) {
            for(int i=1; i <= R * C; i++) ss[i] = s[i];
            bool eli = false;
            for (int r = 1; r <= R; r++) {
                for (int c = 1; c <= C; c++) {
                    int idx = rc_to_idx(r, c);
                    interest += s[idx];

                    int sum = 0, cnt = 0;
                    for (int k = 0; k < 4; k++) {
                        int rr = r + d[k].first, cc = c + d[k].second;
                        if (rr > 0 && rr <= R && cc > 0 && cc <= C) {
                            sum += ss[rc_to_idx(rr, cc)];
                            cnt++;
                        }
                    }
                    if (s[idx] && s[idx] * cnt < sum) {
                        s[idx] = 0;
                        eli = true;
                    }
                }
            }
            if(!eli) break;
        }

        cout << "Case #" << case_num << ": " << interest << '\n';
    }

    return 0;
}