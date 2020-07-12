#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for(int case_num=1; case_num<=t; case_num++) {
        int n;
        cin >> n;
        int v[200000];
        for(int i=0; i<n; i++) {
            cin >> v[i];
        }
        int cnt = 0, max = -1;
        for(int i=0; i<n; i++) {
            if(v[i] > max) {
                if(i == n-1 || v[i] > v[i+1]) {
                    cnt++;
                }
            }
        }
        cout << "Case #" << case_num << ": " << cnt << '\n';
    }
    return 0;
}