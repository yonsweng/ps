#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    int a[100];
    for(int i=0; i<n; i++) {
        cin >> a[i];
    }

    int sum = 0;
    for(int i=0; i<n-2; i++) {
        for(int j=i+1; j<n-1; j++) {
            for(int k=j+1; k<n; k++) {
                if(a[i] + a[j] + a[k] <= m) {
                    sum = max(sum, a[i] + a[j] + a[k]);
                }
            }
        }
    }

    cout << sum;
    return 0;
}