#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<pair<int, int>> adj[100001];

int main() {
    // freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int N, M, C, S[100001], in[100001] = {};

    cin >> N >> M >> C;

    for(int i = 1; i <= N; i++)
        cin >> S[i];

    for(int i = 1; i <= C; i++) {
        int a, b, x;
        cin >> a >> b >> x;
        adj[a].emplace_back(b, x);
        in[b]++;
    }

    queue<int> q;
    for(int i = 1; i <= N; i++)
        if(in[i] == 0)
            q.push(i);

    while(!q.empty()) {
        int from = q.front();
        q.pop();
        for(pair<int, int> p : adj[from]) {
            int to = p.first, plus = p.second;
            S[to] = max(S[to], S[from] + plus);
            in[to]--;
            if(in[to] == 0)
                q.emplace(to);
        }
    }

    for(int i = 1; i <= N; i++)
        cout << S[i] << '\n';
}