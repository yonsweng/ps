#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
const int MAXN = 1e5;
int idx[MAXN * 2], lt[MAXN * 8], ct[MAXN * 8];

struct st {
    int x, y1, y2, t;
} line[MAXN * 2];

void update(int i, int tl, int tr, int ql, int qr, int t) {
    if (tr < ql || qr < tl) {
        return;
    }

    if (ql <= tl && tr <= qr) {
        ct[i] += t;
    } else {
        int mid = (tl + tr) / 2;
        update(i * 2 + 1, tl, mid, ql, qr, t);
        update(i * 2 + 2, mid + 1, tr, ql, qr, t);
    }

    if (ct[i] > 0) {
        lt[i] = idx[tr + 1] - idx[tl];
    } else {
        lt[i] = (tl == tr) ? 0 : (lt[i * 2 + 1] + lt[i * 2 + 2]);
    }
}

long long solution(vector<vector<int>> rectangles) {
    ll res = 0;
    int n = rectangles.size();
    for (int i = 0; i < n; i++) {
        int x1 = rectangles[i][0];
        int y1 = rectangles[i][1];
        int x2 = rectangles[i][2];
        int y2 = rectangles[i][3];
        line[i] = {x1, y1, y2, 1};
        line[i + n] = {x2, y1, y2, -1};
        idx[i] = y1;
        idx[i + n] = y2;
    }
    sort(line, line + 2 * n, [](st i, st j) { return i.x < j.x; });
    sort(idx, idx + 2 * n);
    int e = unique(idx, idx + 2 * n) - idx;
    for (int i = 0; i < 2 * n; i++) {
        if (i) res += (long long)lt[0] * (line[i].x - line[i - 1].x);
        update(0, 0, e - 1, lower_bound(idx, idx + e, line[i].y1) - idx,
               lower_bound(idx, idx + e, line[i].y2) - idx - 1, line[i].t);
    }
    return res;
}

int main() {
    vector<vector<int>> rectangles = {{0, 1, 4, 4}, {3, 1, 5, 3}};
    cout << solution(rectangles);
}