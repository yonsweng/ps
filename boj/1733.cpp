#include <iostream>
#include <map>
#include <queue>
#include <vector>

using namespace std;

const int MAXN = 1000001;
int back_num[MAXN];
map<int, int> adj[MAXN];
bool visited[MAXN];
vector<int> st;
bool in_st[MAXN];
int cycle_num[MAXN], cycle_cnt;

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int N;
    cin >> N;

    for(int i=1; i<=N; i++) {
        int a, b;
        cin >> a >> b;
        adj[a][i] = b;
        adj[b][i] = a;
    }

    // delete leaves
    queue<int> q;
    for(int i=1; i<MAXN; i++) {
        if(adj[i].size() == 1) {
            q.push(i);
        }
    }

    while(!q.empty()) {
        int now = q.front();
        q.pop();

        int next = adj[now].begin()->second;  // node number
        int edge = adj[now].begin()->first;

        back_num[edge] = now;
        adj[now].erase(edge);
        adj[next].erase(edge);
        if(adj[next].size() == 1)
            q.push(next);
    }

    // find duplicate cycles
    bool fail = false;
    for(int i=1; i<MAXN; i++) {
        if(adj[i].size() != 2 && adj[i].size() != 0) {
            fail = true;
            break;
        }
    }

    if(fail)
        cout << -1;
    else {
        for(int i=1; i<MAXN; i++) {
            for(int now = i; !adj[now].empty();) {
                int next = adj[now].begin()->second, man = adj[now].begin()->first;
                back_num[man] = now;
                adj[now].erase(man);
                adj[next].erase(man);
                now = next;
            }
        }

        vector<bool> check(MAXN, false);
        for(int i=1; i<=N; i++) {
            if(check[back_num[i]]) {
                cout << -1;
                return 0;
            }
            check[back_num[i]] = true;
        }

        for(int i=1; i<=N; i++)
            cout << back_num[i] << '\n';
    }
}