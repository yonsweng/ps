#include <bits/stdc++.h>

#define MAXN 500001

using namespace std;

int n;  // n: # of stations
int k;  // k: max # of legs
int d[MAXN];  // i -> d[i]
bool is_ring[MAXN];
bool closed[MAXN];
bool visited[MAXN];
vector<int> children[MAXN];
int f[MAXN];  // # of nodes k legs apart
int g[MAXN];  // # of nodes <= k legs apart
vector<int> ancestors;
deque<pair<int, int>> apart;  // nodes < k legs apart. {node_num, legs}

void find_ring(int here) {
    stack<int> st;

    // until revisit
    while(!closed[here] && !visited[here]) {
        visited[here] = true;
        st.push(here);
        here = d[here];
    }

    if(!closed[here]) {
        while(!st.empty()) {
            int top = st.top();
            st.pop();
            is_ring[top] = true;
            if(top == here) {
                break;
            }
        }
    }
}

void construct_f(int here) {
    if(ancestors.size() >= k) {
        f[ancestors[int(ancestors.size())-k]]++;
    }

    ancestors.push_back(here);
    
    for(int child : children[here]) {
        if(!is_ring[child])
            construct_f(child);
    }

    ancestors.pop_back();
}

void construct_g(int here) {
    int n_children = 0;
    int sum_g = 0;
    int sum_f = 0;

    for(int child : children[here]) {
        if(!is_ring[child]) {
            construct_g(child);
            n_children++;
            sum_g += g[child];
            sum_f += f[child];
        }
    }

    g[here] = sum_g - sum_f + 1;
}

void construct_apart(int here, int depth) {
    if(depth >= k) return;

    apart.emplace_back(here, depth);

    for(int child : children[here]) {
        if(!is_ring[child]) {
            construct_apart(child, depth+1);
        }
    }
}

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    cin >> n >> k;
    for(int i=1; i<=n; i++) {
        cin >> d[i];
    }

    // find ring nodes
    for(int i=1; i<=n; i++) {
        if(!closed[i]) {
            fill_n(visited, n+1, false);
            find_ring(i);

            // visited -> closed
            for(int j=1; j<=n; j++) {
                if(visited[j]) {
                    closed[j] = true;
                }
            }
        }
    }

    // find root nodes of trees
    vector<int> roots;
    for(int i=1; i<=n; i++) {
        if(!is_ring[i] && is_ring[d[i]]) {
            roots.push_back(d[i]);
        }
    }

    // construct children vector
    for(int i=1; i<=n; i++) {
        children[d[i]].push_back(i);
    }

    for(int root : roots) {
        construct_f(root);
        construct_g(root);
        g[root]--;
    }

    // construct apart vector
    for(int root : roots) {
        construct_apart(root, 0);
        apart.pop_front();

        bool visited[MAXN] = {};
        int now = root;
        visited[now] = true;
        for(int i=1; i<=k; i++) {
            if(apart.empty()) break;
            now = d[now];

            if(visited[now]) break;
            visited[now] = true;

            g[now] += apart.size();

            while(!apart.empty()) {
                if(apart[apart.size()-1].second + i == k) {
                    apart.pop_back();
                } else {
                    break;
                }
            }
        }

        apart.clear();
    }

    // ring nodes
    fill_n(visited, n+1, false);
    for(int i=1; i<=n; i++) {
        if(is_ring[i] && !visited[i]) {
            int now = i;
            vector<int> saves;
            while(!visited[now]) {
                visited[now] = true;
                saves.push_back(now);
                now = d[now];
            }

            if(saves.size() > k) {
                for(int saved : saves) {
                    g[saved] += k + 1;
                }
            } else {
                for(int saved : saves) {
                    g[saved] += saves.size();
                }
            }
        }
    }

    for(int i=1; i<=n; i++) {
        cout << g[i] << '\n';
    }

    return 0;
}