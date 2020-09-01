#include <iostream>
#include <algorithm>

using namespace std;

int a[100000];

// f(c, n) = c^0 + c^1 + ... + c^(n-1)
// long long f(int c, int n) {
//     long long p = 1, sum = 0;
//     for(int i=0; i<n; i++, p*=c)
//         sum += abs(p - a[i]);
//     return sum;
// }

int main() {
    int n;
    cin >> n;
    for(int i=0; i<n; i++) cin >> a[i];

    sort(a, a+n);

    long long sum = 0;
    for(int i=0; i<n; i++) sum += a[i];

    long long answer = 1e14;
    for(int c=1; ; c++) {
        bool out = false;
        long long p = 1, f_val = 0;
        for(int i=0; i<n; i++, p*=c) {
            f_val += abs(p - a[i]);
            if(p > 1e10) {
                out = true;
                break;
            }
        }
        if(out)
            break;
            
        if(f_val < answer)
            answer = f_val;
    }

    cout << answer;
}