#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct MergeSortTree {
    struct Node {
        int s, e;
        vector<int> d;
        Node *l, *r;
        Node(int s, int e): s(s), e(e) {}
    } *root;

    MergeSortTree(int s, int e) {
        root = new Node(s, e);
    }

    void init(vector<int> &d, Node *now) {
        if(now->s == now->e) {
            now->d.push_back(d[now->s]);
            return;
        }

        int m = (now->s + now->e) / 2;
        now->l = new Node(now->s, m);
        now->r = new Node(m+1, now->e);
        init(d, now->l);
        init(d, now->r);

        // Merge
        vector<int> &ld = now->l->d, &rd = now->r->d;
        int ln = ld.size(), rn = rd.size();
        int li = 0, ri = 0;
        while(li < ln || ri < rn) {
            if(ri == rn)
                now->d.push_back(ld[li++]);
            else if(li == ln)
                now->d.push_back(rd[ri++]);
            else {
                if(ld[li] < rd[ri])
                    now->d.push_back(ld[li++]);
                else
                    now->d.push_back(rd[ri++]);
            }
        }
    }

    // Return the number of elements larger than k in [i, j].
    int n_larger_than(int i, int j, int k, Node *now) {
        if(now->e < i || j < now->s)
            return 0;
        if(i <= now->s && now->e <= j)
            return now->d.end() - upper_bound(now->d.begin(), now->d.end(), k);
        else
            return n_larger_than(i, j, k, now->l) + n_larger_than(i, j, k, now->r);
    }
};

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> A(N+1);
    for(int i=1; i<=N; i++)
        cin >> A[i];

    MergeSortTree mst(1, N);
    mst.init(A, mst.root);

    int M;
    cin >> M;

    int ans = 0;
    while(M--) {
        int a, b, c;
        cin >> a >> b >> c;

        int i = a ^ ans, j = b ^ ans, k = c ^ ans;
        ans = mst.n_larger_than(i, j, k, mst.root);
        cout << ans << '\n';
    }
}