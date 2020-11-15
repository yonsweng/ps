#include <bits/stdc++.h>

using namespace std;
using ll = long long;

int get_dist(string &a, string &b, int adj[][26]) {
    int dist = 987654321;
    for(char a : a) {
        for(char b : b) {
            dist = min(dist, adj[a-'A'][b-'A']);
        }
    }
    return dist;
}

int main() {
    freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int T;
    cin >> T;
    for (int x = 1; x <= T; x++) {
        bool checked[26] = {};
        const int INF = 987654321;
        int adj[26][26];
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                adj[i][j] = INF;
            }
            adj[i][i] = 0;
        }

        int N, Q;
        cin >> N >> Q;
        vector<string> S(N + 1);
        for (int i = 1; i <= N; i++) {
            cin >> S[i];
            vector<char> s1, s2;
            for(char c : S[i]) {
                if(checked[c-'A']) {
                    s1.push_back(c);
                } else {
                    s2.push_back(c);
                }
            }
            for(char c1 : s1) {
                for(char c2 : s2) {
                    adj[c1-'A'][c2-'A'] = adj[c2-'A'][c1-'A'] = 1;
                }
            }
            for(char c : S[i]) {
                checked[c-'A'] = true;
            }
        }

        for (int k = 0; k < 26; k++) {
            for (int i = 0; i < 26; i++) {
                for (int j = 0; j < 26; j++) {
                    adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j]);
                }
            }
        }

        cout << "Case #" << x << ": ";
        for (int q = 1; q <= Q; q++) {
            int X, Y;
            cin >> X >> Y;
            if(X == Y) {
                cout << "1 ";
                continue;
            }
            int dist = get_dist(S[X], S[Y], adj);
            cout << (dist != INF ? (dist + 2) : -1) << ' ';
        }
        cout << '\n';
    }

    return 0;
}