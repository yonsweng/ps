#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for(int case_num=1; case_num<=t; case_num++) {
        int k;
        cin >> k;
        int a[10001];
        for(int i=1; i<=k; i++) {
            cin >> a[i];
        }
        a[0] = a[1];
        bool decreasing = false;
        int ans = 0, cnt = 0;
        for(int i=1; i<=k; i++) {
            if(a[i] - a[i-1] > 0) {
                if(decreasing) {
                    decreasing = false;
                    ans += max(0, cnt/4);
                    cnt = 0;
                }
                cnt++;
            } else if(a[i] - a[i-1] < 0) {
                if(!decreasing) {
                    decreasing = true;
                    ans += max(0, cnt/4);
                    cnt = 0;
                }
                cnt++;
            }
        }
        ans += max(0, cnt/4);
        cout << "Case #" << case_num << ": " << ans << '\n';
    }
    return 0;
}