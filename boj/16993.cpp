#include <iostream>

using namespace std;

struct Ret {
    int sum, lmax, rmax, tmax;
};

const int INF = 100000001;
const int TREE_SIZE = 400000;
int sum[TREE_SIZE], lmax[TREE_SIZE], rmax[TREE_SIZE], tmax[TREE_SIZE];

void update(int i, int tl, int tr, int q, int v) {
    if(q < tl || tr < q)
        return;

    if(tl == tr) {
        sum[i] = lmax[i] = rmax[i] = tmax[i] = v;
        return;
    }

    int mid = (tl + tr) / 2;
    int l = i * 2, r = i * 2 + 1;
    update(l, tl, mid, q, v);
    update(r, mid + 1, tr, q, v);

    sum[i] = sum[l] + sum[r];
    lmax[i] = max(lmax[l], sum[l] + lmax[r]);
    rmax[i] = max(rmax[r], sum[r] + rmax[l]);
    tmax[i] = max(rmax[l] + lmax[r], max(tmax[l], tmax[r]));
}

Ret query(int i, int tl, int tr, int ql, int qr) {
    if(qr < tl || tr < ql)
        return {0, -INF, -INF, -INF};

    if(ql <= tl && tr <= qr)
        return {sum[i], lmax[i], rmax[i], tmax[i]};

    int mid = (tl + tr) / 2;
    int l = i * 2, r = i * 2 + 1;
    Ret lret = query(l, tl, mid, ql, qr);
    Ret rret = query(r, mid + 1, tr, ql, qr);

    int ret_sum = lret.sum + rret.sum;
    int ret_lmax = max(lret.lmax, lret.sum + rret.lmax);
    int ret_rmax = max(rret.rmax, rret.sum + lret.rmax);
    int ret_tmax = max(lret.rmax + rret.lmax, max(lret.tmax, rret.tmax));
    return {ret_sum, ret_lmax, ret_rmax, ret_tmax};
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int N, M;
    cin >> N;
    for(int i=1; i<=N; i++) {
        int a;
        cin >> a;
        update(1, 1, N, i, a);
    }
    cin >> M;
    for(int i=1; i<=M; i++) {
        int a, b;
        cin >> a >> b;
        cout << query(1, 1, N, a, b).tmax << '\n';
    }

    return 0;
}