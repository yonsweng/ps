#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        string s[1000];
        for(int i=0; i<n; i++) {
            cin >> s[i];
        }

        int cnt[26] = {};
        for(int i=0; i<n; i++) {
            for(char c : s[i]) {
                cnt[c-'a']++;
            }
        }

        bool no = false;
        for(int i=0; i<26; i++) {
            if(cnt[i] % n != 0) {
                no = true;
            }
        }

        if(!no) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
}