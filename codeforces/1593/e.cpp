#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

void find_leaves(int p, int u, vector<set<int> > &adj, vector<int> &leaves) {
    if(adj[u].size() <= 1)
        leaves.push_back(u);

    for(int v : adj[u])
        if(v != p)
            find_leaves(u, v, adj, leaves);
}

int remove_node(int u, vector<set<int> > &adj) {
    int candidate = *(adj[u].begin());
    adj[candidate].erase(u);
    return candidate;
}

int main() {
    // freopen("input.txt", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int t;
    cin >> t;

    while(t--) {
        int n, k;
        cin >> n >> k;

        int remain = n;

        vector<set<int> > adj(n + 1);
        for(int i=0; i<n-1; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].insert(v);
            adj[v].insert(u);
        }

        vector<int> leaves;
        find_leaves(0, 1, adj, leaves);

        while(remain > 0 && k-- > 0) {
            vector<int> candidates;
            for(auto leaf : leaves) {
                candidates.push_back(remove_node(leaf, adj));
                remain--;
            }

            leaves.clear();

            sort(candidates.begin(), candidates.end());
            candidates.erase(unique(candidates.begin(),candidates.end()),candidates.end());
            for(auto candidate : candidates) {
                if(adj[candidate].size() <= 1) {
                    leaves.push_back(candidate);
                }
            }
        }

        cout << remain << '\n';
    }


    return 0;
}