#include <bits/stdc++.h>

using namespace std;

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int t;
    cin >> t;
    while(t-- > 0) {
        string s;
        cin >> s;

        bool no = false;
        int i = 0;
        while(i < s.size()) {
            if(s[i] == '1') {
                if(i + 1 >= s.size() || s[i + 1] == '1' || i + 2 >= s.size() || s[i + 2] == '1') {
                    no = true;
                    break;
                }
                i += 3;
                while(i < s.size() && s[i] == '0') {
                    i++;
                }
                if(i >= s.size()) {
                    no = true;
                    break;
                }
                i++;
                if(s[i] == '0') continue;
                while(i < s.size() && s[i] == '1') {
                    i++;
                }
                if(i + 1 < s.size() && s[i] == '0' && s[i + 1] == '0') {
                    i--;
                }
            } else {
                if(i + 1 >= s.size() || s[i + 1] == '0') {
                    no = true;
                    break;
                }
                i += 2;
            }
        }

        if(!no) cout << "YES\n";
        else cout << "NO\n";
    }
}