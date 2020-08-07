#include <iostream>
#include <set>

using namespace std;

bool find6(set<int> &s4, int c[]) {
    for(int x : s4) {
        if(c[x] >= 6) return true;
    }
    return false;
}

bool find8(set<int> &s4, int c[]) {
    for(int x : s4) {
        if(c[x] >= 8) return true;
    }
    return false;
}

int main() {
    int n;
    cin >> n;
    int a[100001];
    int c[100001] = {};
    set<int> s2, s4;
    for(int i=1; i<=n; i++) {
        cin >> a[i];
        c[a[i]]++;
        if(c[a[i]] == 2) {
            s2.insert(a[i]);
        } else if(c[a[i]] == 4) {
            s2.erase(a[i]);
            s4.insert(a[i]);
        }
    }
    int q;
    cin >> q;
    for(int i=1; i<=q; i++) {
        char sign;
        int x;
        cin >> sign >> x;
        if(sign == '+') {
            c[x]++;
            if(c[x] == 2) {
                s2.insert(x);
            } else if(c[x] == 4) {
                s2.erase(x);
                s4.insert(x);
            }
        } else {
            c[x]--;
            if(c[x] == 1) {
                s2.erase(x);
            } else if(c[x] == 3) {
                s4.erase(x);
                s2.insert(x);
            }
        }
        if(s4.size() >= 2) {
            cout << "YES\n";
        } else if(s2.size() >= 2 && s4.size() >= 1) {
            cout << "YES\n";
        } else if(s2.size() >= 1 && find6(s4, c)) {
            cout << "YES\n";
        } else if(find8(s4, c)) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
}