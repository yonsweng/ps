#include <bits/stdc++.h>

using namespace std;

char toggle(char c) {
    return (c == '0') ? '1' : '0';
}

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int T;
    cin >> T;
    while(T--) {
        int n;
        cin >> n;
        char a[100002], b[100002];
        cin >> a + 1;
        cin >> b + 1;
        vector<int> answer;

        int left = 1, i = n, right = n;
        bool toggled = false;

        for(int j=n; j>=1; j--) {
            char ai = toggled ? toggle(a[i]) : a[i];
            if(ai != b[j]) {
                if(!toggled) {
                    if(a[left] == b[j]) {
                        answer.push_back(1);
                        a[left] = toggle(a[left]);
                    }
                    answer.push_back(j);
                    toggled = !toggled;
                    right = i;
                    i = left;
                } else {
                    if(toggle(a[right]) == b[j]) {
                        answer.push_back(1);
                        a[right] = toggle(a[right]);
                    }
                    answer.push_back(j);
                    toggled = !toggled;
                    left = i;
                    i = right;
                }
            }
            if(!toggled) i--;
            else i++;
        }
        cout << answer.size();
        for(int elt : answer) {
            cout << ' ' << elt;
        }
        cout << '\n';
    }
}