#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
#include <set>
#include <map>

#define MAXN 500001

using namespace std;

int n, k;
int d[MAXN];
vector<int> rev[MAXN];
int answer[MAXN];
bool done[MAXN];
int run_stack[2 * MAXN];
vector<int> node_cnt;
vector<int> ring_nodes;
set<int> ring_node_set;
map<int, int> n_last;
vector<int> st;


void find_ring_nodes(int start, vector<int> &ring_nodes) {
    stack<int> s;
    set<int> visited;
    int i = start;
    while(visited.find(i) == visited.end()) {
        visited.insert(i);
        s.push(i);
        i = d[i];
    }

    ring_nodes.push_back(i);
    while(!s.empty() && s.top() != i) {
        ring_nodes.push_back(s.top());
        s.pop();
    }
    reverse(ring_nodes.begin(), ring_nodes.end());
}

int dfs(int i, vector<int> &st, map<int, int> &n_last, vector<int> &node_cnt, set<int> &ring_node_set) {
    done[i] = true;

    if(st.size() >= k + 1) {
        if(n_last.find(st[int(st.size())-k-1]) != n_last.end())
            n_last[st[int(st.size())-k-1]] += 1;
        else
            n_last[st[int(st.size())-k-1]] = 1;
    }

    if(st.size() < k) {
        if(st.size() >= node_cnt.size())
            node_cnt.push_back(1);
        else {
            node_cnt[st.size()] += 1;
            // cout << "case 1: " << i << ' ' << st.size() << ' ' << node_cnt[st.size()] << '\n';
        }
    }

    st.push_back(i);

    // cout << "stack " << i << ": ";
    // for(int a : st) cout << a << ' ';
    // cout << '\n';

    for(int j : rev[i]) {
        if(ring_node_set.find(j) == ring_node_set.end())
            answer[i] += dfs(j, st, n_last, node_cnt, ring_node_set);
    }

    // if(i == 1)
    //     cout << "n_last[1]: " << n_last[i] << '\n';
    answer[i] -= n_last.find(i) != n_last.end() ? n_last[i] : 0;

    st.pop_back();

    return answer[i];
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);

    cin >> n >> k;
    for(int i=1; i<=n; i++) {
        cin >> d[i];
        rev[d[i]].push_back(i);
        answer[i] = 1;
    }

    for(int start=1; start<=n; start++) {
        if(done[start])
            continue;

        ring_nodes.clear();
        find_ring_nodes(start, ring_nodes);

        ring_node_set.clear();
        for(auto node : ring_nodes) {
            ring_node_set.insert(node);
            // cout << node << ' ';
        }

        st.clear();
        int accu = 0;
        int idx;
        n_last.clear();
        for(idx=0; idx<ring_nodes.size(); idx++) {
            answer[ring_nodes[idx]] += accu;
            accu -= run_stack[idx];
            run_stack[idx] = 0;

            node_cnt.clear();
            dfs(ring_nodes[idx], st, n_last, node_cnt, ring_node_set);

            // cout << "node_cnt: ";
            for(int pp : node_cnt) {
                // cout << pp << ' ';
                accu += pp;
            }
            // cout << '\n';

            // for(map<int, int>::iterator it = n_last.begin(); it != n_last.end(); it++) {
            //     cout << it->first << ' ' << it->second << '\n';
            // }

            for(int j=0; j<node_cnt.size(); j++) {
                int p = idx + min(k - j, int(ring_nodes.size()) - 1);
                run_stack[p] += node_cnt[j];
            }
        }

        for(int i=0; i<int(ring_nodes.size()) - 1; i++) {
            if(accu <= 0) break;
            answer[ring_nodes[i % int(ring_nodes.size())]] += accu;
            accu -= run_stack[i + idx];
            run_stack[i + idx] = 0;
        }
    }

    for(int i=1; i<=n; i++)
        cout << answer[i] << '\n';

    return 0;
}