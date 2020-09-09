#include <iostream>
#include <vector>

using namespace std;

int gcd(int a, int b) {
   if(b == 0) return a;
   return gcd(b, a % b);
}

int main() {
    // freopen("1.in", "r", stdin);
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        
        vector<int> a(n);
        int M = 0, mi = -1;
        for(int i=0; i<n; i++) {
            cin >> a[i];
            if(a[i] > M) {
                M = a[i];
                mi = i;
            }
        }

        vector<int> answer;
        answer.push_back(M);
        a.erase(a.begin() + mi);
        int curr_gcd = M;

        for(int i=1; i<n; i++) {
            int M = 0, mi = -1;
            for(int j=0; j<a.size(); j++) {
                int g = gcd(a[j], curr_gcd);
                if(g > M) {
                    M = g;
                    mi = j;
                }
            }
            answer.push_back(a[mi]);
            a.erase(a.begin() + mi);
            curr_gcd = M;
        }

        for(int k : answer) cout << k << ' ';
        cout << '\n';
    }
}
