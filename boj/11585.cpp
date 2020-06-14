#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> getPi(string &p) {
    vector<int> pi(p.size(), 0);
    int j = 0;
    for(int i=1; i<p.size(); i++) {
        while(j > 0 && p[i] != p[j])
            j = pi[j-1];
        if(p[i] == p[j])
            pi[i] = ++j;
    }
    return pi;
}

vector<int> kmp(string &t, string &p) {
    vector<int> bi, pi = getPi(p);
    int n = p.size(), j = 0;
    for(int i=0; i<t.size(); i++) {
        while(j > 0 && t[i] != p[j])
            j = pi[j-1];
        if(t[i] == p[j]) {
            if(j == n-1) {
                bi.push_back(i-n+1);
                j = pi[j];
            } else j++;
        }
    }
    return bi;
}

int gcd(int a, int b) { 
   if (b == 0) 
      return a; 
   return gcd(b, a % b);  
}

int main() {
	// freopen("1.in", "r", stdin);

	int N;
    string p, t;

    cin >> N;
    p.resize(N);
    t.resize(2*N-1);
    for(int i=0; i<N; i++)
        cin >> p[i];
    for(int i=0; i<N; i++)
        cin >> t[i];

    // Copy t[0 ~ N-2] to t[N ~ 2*N-2]
    for(int i=0; i<N-1; i++)
        t[i+N] = t[i];

    auto bi = kmp(t, p);
    int cnt = bi.size();
    int d = gcd(cnt, N);
    cout << cnt / d << "/" << N / d;

	return 0;
}