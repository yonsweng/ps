#include <vector>
#include <algorithm>

using namespace std;

struct MergeSortTree {
    struct Node {
        int s, e;
        vector<int> d;
        Node *l, *r;
        Node(int s, int e): s(s), e(e) {}
    };

    static Node *root;

    MergeSortTree(int s, int e, vector<int> &d) {
        root = new Node(s, e);
        init(d, root);
    }

    void init(vector<int> &d, Node *now) {
        if(now->s == now->e) {
            now->d.push_back(d[now->s]);
            return;
        }

        int m = (now->s + now->e) / 2;
        now->l = new Node(now->s, m), now->r = new Node(m+1, now->e);
        init(d, now->l), init(d, now->r);

        // Merge
        vector<int> &ld = now->l->d, &rd = now->r->d, &nd = now->d;
        int li = 0, ri = 0, ln = ld.size(), rn = rd.size();
        while(li < ln || ri < rn) {
            if(ri == rn) nd.push_back(ld[li++]);
            else if(li == ln) nd.push_back(rd[ri++]);
            else if(ld[li] < rd[ri]) nd.push_back(ld[li++]);
            else nd.push_back(rd[ri++]);
        }
    }

    // Return the number of elements larger than k in [i, j].
    int n_larger_than(int i, int j, int k, Node *now=root) {
        if(now->e < i || j < now->s)
            return 0;
        if(i <= now->s && now->e <= j)
            return now->d.end() - upper_bound(now->d.begin(), now->d.end(), k);
        else
            return n_larger_than(i, j, k, now->l) + n_larger_than(i, j, k, now->r);
    }
};