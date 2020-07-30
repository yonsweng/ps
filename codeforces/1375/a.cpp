#include <iostream>
#include <cmath>

using namespace std;

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int t;
    cin >> t;
    while(t-- > 0) {
        int n, a[100], diff[99];
        cin >> n;
        for(int i=1; i<=n; i++) cin >> a[i];

        int positive = 0, negative = 0;
        for(int i=1; i<n; i++) {
            diff[i] = a[i+1] - a[i];
            if(diff[i] >= 0) positive++;
            if(diff[i] <= 0) negative++;
        }

        if(positive < (n - 1) / 2) {  // - -> +
            for(int i=1; i<n; i++) {
                if(diff[i] < 0) {
                    if(abs(a[i]) > abs(a[i+1])) {
                        a[i] = -a[i];
                        for(int j=i; j>=1; j--) {
                            if(diff[j] > 0) positive--;
                            else if(diff[j] < 0) negative--;
                            diff[j] = a[j+1] - a[j];
                            if(diff[j] > 0) positive++;
                            else if(diff[j] < 0) negative++;
                        }
                    } else if(abs(a[i]) < abs(a[i+1])) {
                        a[i+1] = -a[i+1];
                        for(int j=i; j<n; j++) {
                            if(diff[j] > 0) positive--;
                            else if(diff[j] < 0) negative--;
                            diff[j] = a[j+1] - a[j];
                            if(diff[j] > 0) positive++;
                            else if(diff[j] < 0) negative++;
                        }
                    }
                    if(positive >= (n - 1) / 2) break;
                }
            }
        } else if(negative < (n - 1) / 2) {
            for(int i=1; i<n; i++) {
                if(diff[i] > 0) {
                    if(abs(a[i]) > abs(a[i+1])) {
                        a[i] = -a[i];
                        for(int j=i; j>=1; j--) {
                            if(diff[j] > 0) positive--;
                            else if(diff[j] < 0) negative--;
                            diff[j] = a[j+1] - a[j];
                            if(diff[j] > 0) positive++;
                            else if(diff[j] < 0) negative++;
                        }
                    } else if(abs(a[i]) < abs(a[i+1])) {
                        a[i+1] = -a[i+1];
                        for(int j=i; j<n; j++) {
                            if(diff[j] > 0) positive--;
                            else if(diff[j] < 0) negative--;
                            diff[j] = a[j+1] - a[j];
                            if(diff[j] > 0) positive++;
                            else if(diff[j] < 0) negative++;
                        }
                    }
                    if(negative >= (n - 1) / 2) break;
                }
            }
        }

        for(int i=1; i<=n; i++) cout << a[i] << ' ';
        cout << '\n';
    }

    return 0;
}