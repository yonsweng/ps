#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("input/2.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    string s;
    cin >> s;

    long long ans = 0;
    stack<int> st, bk;
    stack<char> p;
    st.push(0);
    for(char c : s) {
        if(c == '(') {
            st.push(0);
            p.push(c);
        } else if(c == ')') {
            if(st.size() >= 2) {
                bk.push(st.top());
                st.pop();
                ans += ++st.top();
                p.push(c);
            } else {
                bk.push(st.top());
                st.top() = 0;
                p.push('-');
            }
        } else {
            if(p.top() == '(') {
                st.pop();
            } else if(p.top() == ')') {
                ans -= st.top()--;
                st.push(bk.top());
                bk.pop();
            } else {
                st.top() = bk.top();
                bk.pop();
            }
            p.pop();
        }
        cout << ans << '\n';
    }

    return 0;
}