#include <iostream>
#include <string>

using namespace std;

bool fill_s(string &s, int i, int n, int k) {
    char c = s[i];
    for(int j=i+k; j<n; j+=k) {
        if(c == '?') {
            c = s[j];
        } else {
            if(s[j] != '?' && s[j] != c) return false;
        }
    }
    for(int j=i; j<n; j+=k) s[j] = c;
    return true;
}

int main() {
    freopen("1.in", "r", stdin);
    int t;
    cin >> t;
    while(t--) {
        int n, k;
        cin >> n >> k;

        string s;
        cin >> s;

        bool no = false;
        for(int i=0; i<k; i++) {
            bool good = fill_s(s, i, n, k);
            if(good == false) {
                no = true;
                break;
            }
        }

        int q = 0, zero = 0, one = 0;
        for(int i=0; i<k; i++) {
            if(s[i] == '0') zero++;
            else if(s[i] == '1') one++;
            else q++;
        }

        if(!no && q + min(zero, one) >= max(zero, one)) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
}