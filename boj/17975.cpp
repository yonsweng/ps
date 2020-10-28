#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    int x, y, w;
    bool operator<(Point &p) {
        return y < p.y || (y == p.y && x < p.x);
    }
};

const int TREE_SIZE = 8000;
int sum[TREE_SIZE], lmax[TREE_SIZE], rmax[TREE_SIZE], tmax[TREE_SIZE];

void update(int i, int tl, int tr, int q, int v) {
    if(q < tl || tr < q)
        return;

    if(tl == tr) {
        sum[i] += v;
        lmax[i] = rmax[i] = tmax[i] = max(0, sum[i]);
        return;
    }

    int mid = (tl + tr) / 2, l = i * 2, r = i * 2 + 1;
    update(l, tl, mid, q, v);
    update(r, mid + 1, tr, q, v);

    sum[i] = sum[l] + sum[r];
    lmax[i] = max(lmax[l], sum[l] + lmax[r]);
    rmax[i] = max(rmax[r], sum[r] + rmax[l]);
    tmax[i] = max(rmax[l] + lmax[r], max(tmax[l], tmax[r]));
}

int main() {
    // freopen("input/2.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    // Input
    int n1, n2, n, c1, c2;
    cin >> n1;
    vector<Point> P(n1);
    for(int i = 0; i < n1; i++)
        cin >> P[i].x >> P[i].y;
    cin >> n2;
    n = n1 + n2;
    P.resize(n);
    for(int i = n1; i < n; i++)
        cin >> P[i].x >> P[i].y;
    cin >> c1 >> c2;
    for(int i = 0; i < n1; i++)
        P[i].w = c1;
    for(int i = n1; i < n; i++)
        P[i].w = -c2;

    // Coordinate compression
    vector<int> x(n);
    for(int i = 0; i < n; i++)
        x[i] = P[i].x;
    sort(x.begin(), x.end());
    x.erase(unique(x.begin(), x.end()), x.end());
    for(int i = 0; i < n; i++)
        P[i].x = lower_bound(x.begin(), x.end(), P[i].x) - x.begin();

    // Sort by y coordinate
    sort(P.begin(), P.end());

    // Sweeping
    const int MAX_X = int(x.size()) - 1;
    int answer = 0, prev_y = -1000000001;
    P.resize(n + 1);
    P[n].y = 1000000001;
    for(int i = 0; i < n; i++) {
        if(prev_y == P[i].y)
            continue;
        prev_y = P[i].y;
        for(int j = i; j < n; j++) {
            update(1, 0, MAX_X, P[j].x, P[j].w);
            if(P[j+1].y != P[j].y)
                answer = max(answer, tmax[1]);
        }
        fill_n(sum, TREE_SIZE, 0);
        fill_n(lmax, TREE_SIZE, 0);
        fill_n(rmax, TREE_SIZE, 0);
        fill_n(tmax, TREE_SIZE, 0);
    }

    cout << answer;
}