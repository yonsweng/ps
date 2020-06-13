#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> getPi(vector<int> &p) {
    vector<int> pi(p.size(), 0);
    int j = 0;
    for(int i=1; i<p.size(); i++) {
        while(j > 0 && p[i] != p[j])
            j = pi[j-1];
        if(p[i] == p[j])
            pi[i] = ++j;
    }
    return pi;
}

vector<int> kmp(vector<int> &t, vector<int> &p){
    vector<int> bi;
    vector<int> pi = getPi(p);
    int n = int(p.size());
    int j = 0;
    for(int i=0; i<t.size(); i++) {
        while(j > 0 && t[i] != p[j])
            j = pi[j-1];
        if(t[i] == p[j]) {
            if(j == n-1) {
                bi.push_back(i-n+1);
                j = pi[j];
            } else j++;
        }
    }
    return bi;
}

int main() {
    freopen("1.in", "r", stdin);

    int N, K, M, c;
    vector<int> C[100];

    cin >> N >> K;
    for(int i=0; i<N; i++) {
        cin >> M;
        while(M--) {
            cin >> c;
            C[i].push_back(c);
        }
    }

    bool virus = false;
    for(int i=0; i<C[0].size(); i++) {
        vector<int> P1;  // P1[]: C[0][i ~ i+K-1]
        vector<int> P2;  // P2[]: C[0][i+K-1 ~ i]
        for(int j=i; j<i+K; j++)
            P1.push_back(C[0][j]);
        for(int j=i+K-1; j>=i; j--)
            P2.push_back(C[0][j]);

        virus = true;
        for(int k=1; k<N; k++) {
            vector<int> Si1 = kmp(C[k], P1);
            vector<int> Si2 = kmp(C[k], P2);

            if(Si1.empty() && Si2.empty()) {
                virus = false;
                break;
            }
        }

        if(virus) break;
    }

    if(virus) cout << "YES";
    else cout << "NO";

    return 0;
}