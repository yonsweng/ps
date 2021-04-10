#include <bits/stdc++.h>

using namespace std;

bool check_999(string &s) {
    for(char c : s) {
        if(c != '9') return false;
    }
    return true;
}

int main() {
    // freopen("input/1.in", "r", stdin);
    // freopen("output/1.out", "r", stdout);

    ios::sync_with_stdio(false), cin.tie(nullptr);

    int T;
    cin >> T;

    for(int x=1; x<=T; x++) {
        int y = 0;
        int N;
        string X[100];

        cin >> N;
        for(int i=0; i<N; i++)
            cin >> X[i];

        for(int i=0; i<N-1; i++) {
            if(X[i].size() < X[i+1].size()) {
                continue;
            }
            int j;
            for(j=0; j<X[i].size(); j++) {
                if(X[i+1].size() == j) {
                    string sub = X[i].substr(j);
                    if(check_999(sub)) {
                        X[i+1].append(sub.size()+1, '0');
                        y += sub.size()+1;
                    } else {
                        X[i+1].append(sub.substr(0, int(sub.size())-1));
                        X[i+1].append(1, sub[int(sub.size())-1]+1);
                        y += sub.size();
                    }
                    break;
                } else if(X[i][j] < X[i+1][j]) {
                    int dy = abs(int(X[i].size()) - int(X[i+1].size()));
                    X[i+1].append(dy, '0');
                    y += dy;
                    break;
                } else if(X[i][j] > X[i+1][j]) {
                    int dy = abs(int(X[i].size()) - int(X[i+1].size())) + 1;
                    X[i+1].append(dy, '0');
                    y += dy;
                    break;
                }
            }
            if(j == X[i].size()) {
                if(X[i+1].size() == X[i].size()) {
                    X[i+1].append(1, '0');
                    y += 1;
                }
            }
        }

        cout << "Case #" << x << ": " << y << '\n';
    }
}