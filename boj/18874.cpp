#include <bits/stdc++.h>

#define MAXN 100000
#define MAXY 100000

using namespace std;

int N;

template<typename T>
class SegTree
{
private:
    int count;
    std::vector<T> tree;
    std::vector<T> lazy;

    T initialize(int index, int start, int end, const std::vector<T>& original)
    {
        if (start == end)
            return tree[index] = original[start];
        
        int mid = (start + end) / 2;
        T left = initialize(index * 2, start, mid, original);
        T right = initialize(index * 2 + 1, mid + 1, end, original);

        return tree[index] = (left + right);
    }

    void propagate(int index, int start, int end)
    {
        if (lazy[index] != 0)
        {
            tree[index] += lazy[index] * (end - start + 1);

            if (start != end)
            {
                lazy[index * 2] += lazy[index];
                lazy[index * 2 + 1] += lazy[index];
            }

            lazy[index] = 0;
        }
    }

    T query(int index, int nodeStart, int nodeEnd, int reqStart, int reqEnd)
    {
        propagate(index, nodeStart, nodeEnd);

        int nodeMid = (nodeStart + nodeEnd) / 2;

        if (nodeStart > reqEnd || nodeEnd < reqStart)
            return 0;

        else if (nodeStart >= reqStart && nodeEnd <= reqEnd)
            return tree[index];
        
        else
        {
            T left = query(index * 2, nodeStart, nodeMid, reqStart, reqEnd);
            T right = query(index * 2 + 1, nodeMid + 1, nodeEnd, reqStart, reqEnd);
            return left + right;
        }
    }

    void update(T add, int dataStart, int dataEnd, int treeIndex, int treeStart, int treeEnd)
    {
        propagate(treeIndex, treeStart, treeEnd);

        int treeMid = (treeStart + treeEnd) / 2;

        if (dataEnd < treeStart || treeEnd < dataStart)
            return;
        
        if (dataStart <= treeStart && treeEnd <= dataEnd)
        {
            tree[treeIndex] += add * (treeEnd - treeStart + 1);
            if (treeStart != treeEnd)
            {
                lazy[treeIndex * 2] += add;
                lazy[treeIndex * 2 + 1] += add;
            }
            return;
        }

        update(add, dataStart, dataEnd, treeIndex * 2, treeStart, treeMid);
        update(add, dataStart, dataEnd, treeIndex * 2 + 1, treeMid + 1, treeEnd);

        tree[treeIndex] = tree[treeIndex * 2] + tree[treeIndex * 2 + 1];
    }
    
public:
    SegTree(const std::vector<T>& original)
    {
        count = (int)original.size();
        int treeHeight = (int)ceil(log2(count));
        int vecSize = (1 << (treeHeight + 1));
        tree.resize(vecSize);
        lazy.resize(vecSize);
        initialize(1, 0, count - 1, original);
    }

    SegTree(int size)
    {
        count = size;
        int treeHeight = (int)ceil(log2(count));
        int vecSize = (1 << (treeHeight + 1));
        tree.resize(vecSize);
        lazy.resize(vecSize);
    }

    T query(int start, int end)
    {
        return query(1, 0, count - 1, start, end);
    }

    void update(T add, int start, int end)
    {
        update(add, start, end, 1, 0, count - 1);
    }
};

vector<int> idx[MAXN + 1];

int main() {
    freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    cin >> N;

    vector<int> A(N + 1);
    for(int i=1; i<=N; i++) {
        cin >> A[i];
        idx[A[i]].push_back(i);
    }

    SegTree<int> st(N + 1);

    st.update(1, 1, N);

    long long sum = 0;
    cout << 0 << '\n';
    for(int j=1; j<N; j++) {
        for(int k : idx[j-1]) {
            st.update(-1, k, k);
            sum += st.query(1, k-1);
        }
        cout << sum << '\n';
    }
}