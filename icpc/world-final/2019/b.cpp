#include <iostream>
#include <cmath>

using namespace std;

long long sq(int x) { return (long long)x * x; }

// is (x, y) under the arc whose center is (x1, y1) and radius is r
bool under_arc(int two_x, int two_y, int two_x1, int two_y1, int two_r) {
    // not under arc
    if(two_y > two_y1 && sq(two_x-two_x1) + sq(two_y-two_y1) > sq(two_r))
        return false;
    else
        return true;
}

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int n, h, alpha, beta;
    int x[10001], y[10001];
    cin >> n >> h >> alpha >> beta;
    for(int i=1; i<=n; i++)
        cin >> x[i] >> y[i];

    // index of farthest point to which point i can make an arc.
    int from_left[10000];
    for(int i=1; i<=n-1; i++) {
        int j = n;  // pillar
        for(int k=j; k>=i; k--) {
            // check if point k is above the arc i-j.
            while(j >= k) {
                // if point k is under the arc
                if(under_arc(2*x[k], 2*y[k], x[i]+x[j], 2*h-(x[j]-x[i]), x[j]-x[i]))
                    break;
                j--;
            }
        }
        from_left[i] = j;
    }

    // from right to left
    int from_right[10001];
    for(int i=n; i>=2; i--) {
        int j = 1;  // pillar
        for(int k=j; k<=i; k++) {
            // check if point k is above the arc i-j.
            while(j <= k) {
                // if point k is under the arc
                if(under_arc(2*x[k], 2*y[k], x[i]+x[j], 2*h-(x[i]-x[j]), x[i]-x[j]))
                    break;
                j++;
            }
        }
        from_right[i] = j;
    }

    // dp[i]: minimum cost when build a pillar on point i
    long long dp[10001];
    bool is_pillar[10001] = {};
    dp[1] = (long long)alpha * (h - y[1]);
    is_pillar[1] = true;
    for(int i=2; i<=n; i++) {
        long long min_dp = 1e18;
        for(int j=1; j<i; j++) {
            if(is_pillar[j] && from_left[j] >= i && from_right[i] <= j) {
                is_pillar[i] = true;
                min_dp = min(min_dp, dp[j] + (long long)alpha*(h-y[i]) + beta*sq(x[i]-x[j]));
            }
        }
        if(is_pillar[i])
            dp[i] = min_dp;
    }

    if(is_pillar[n])
        cout << dp[n];
    else
        cout << "impossible";

    return 0;
}