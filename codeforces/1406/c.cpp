#include <bits/stdc++.h>

using namespace std;

int getSz(int here, int dad, vector<vector<int>> &adj, vector<int> &sz){
    sz[here]=1;
    for(auto there : adj[here]){
        if(there==dad)continue;
        sz[here] += getSz(there, here, adj, sz);
    }
    return sz[here];
}

int get_centroid(int here, int dad, int cap, vector<vector<int>> &adj, vector<int> &sz){
    //cap <---- (tree size)/2
    for(auto there:adj[here]){
        if(there==dad)continue;
        if(sz[there]>cap) return get_centroid(there,here,cap, adj, sz);
    }
    return here;
}

int find_leaf(int here, int dad, vector<vector<int>> &adj) {
    if(adj[here].size() == 1) {
        return here;
    }
    int leaf = 0;
    for(int there : adj[here]) {
        if(there == dad) continue;
        leaf = find_leaf(there, here, adj);
        if(leaf) break;
    }
    return leaf;
}

int main(){
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int t;
    cin >> t;

    while(t--) {
        int n;
        cin >> n;

        vector<vector<int>> adj(n+1);
        vector<int> sz(n+1);

        for(int i=0; i<n-1; i++) {
            int x, y;
            cin >> x >> y;
            adj[x].push_back(y);
            adj[y].push_back(x);
        }

        int root = 1;
        getSz(root, -1, adj, sz);
        int centroid = get_centroid(1,-1,sz[root]/2, adj, sz);

        root = centroid;
        fill(sz.begin(), sz.end(), 0);
        getSz(root, -1, adj, sz);

        int max_sz = 0, max_root = 0;
        for(int sub_root : adj[root]) {
            if(sz[sub_root] > max_sz) {
                max_sz = sz[sub_root];
                max_root = sub_root;
            }
        }

        int leaf = find_leaf(max_root, root, adj);

        cout << leaf << ' ' << adj[leaf][0] << '\n';
        cout << leaf << ' ' << root << '\n';
    }
}