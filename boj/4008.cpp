#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

struct ConvexHull {
    struct Line {
        ll a, b;
    };

    vector<Line> lines;

    void push(Line line) {
        while(1) {
            int n = lines.size();
            if(n < 2) break;

            ll a2 = lines[n-2].a, a1 = lines[n-1].a, a0 = line.a;
            ll b2 = lines[n-2].b, b1 = lines[n-1].b, b0 = line.b;

            // new intersection is on the right.
            if((b1-b2)*(a1-a0) < (b0-b1)*(a2-a1)) break;

            lines.pop_back();
        }
        lines.push_back(line);
    }

    ll f(int i, ll x) {
        return lines[i].a * x + lines[i].b;
    }
};

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int n, a, b, c;
    cin >> n;
    cin >> a >> b >> c;

    vector<int> x(n+1);
    for(int i=1; i<=n; i++)
        cin >> x[i];

    vector<int> s(n+1);
    s[0] = 0;
    for(int i=1; i<=n; i++)
        s[i] = s[i-1] + x[i];

    ConvexHull ch;
    vector<ll> d(n+1);
    d[0] = 0;
    int k = 0;
    for(int i=1; i<=n; i++) {
        int j = i - 1;
        ch.push({-2*a*s[j], d[j]+(ll)a*s[j]*s[j]-(ll)b*s[j]});
        while(k+1 < ch.lines.size() && ch.f(k, s[i]) < ch.f(k+1, s[i])) k++;
        d[i] = ch.f(k, s[i]) + (ll)a*s[i]*s[i] + (ll)b*s[i] + c;
    }
    cout << d[n];
}