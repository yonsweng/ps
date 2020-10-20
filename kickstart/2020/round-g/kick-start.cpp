#include <bits/stdc++.h>

using namespace std;

int main() {
    // freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int T;
    cin >> T;
    for(int x=1; x<=T; x++) {
        string S;
        cin >> S;

        vector<int> kick, start;

        // Find "KICK".
        for(int i=0; i<int(S.size())-3; i++) {
            if(S[i] == 'K' && S[i+1] == 'I' && S[i+2] == 'C' && S[i+3] == 'K') {
                kick.push_back(i);
            }
        }

        // Find "START".
        for(int i=0; i<int(S.size())-4; i++) {
            if(S[i] == 'S' && S[i+1] == 'T' && S[i+2] == 'A' && S[i+3] == 'R' && S[i+4] == 'T') {
                start.push_back(i);
            }
        }

        int answer = 0;
        for(int k : kick) {
            answer += int(start.size()) - int(upper_bound(start.begin(), start.end(), k) - start.begin());
        }
        cout << "Case #" << x << ": " << answer << '\n';
    }
}