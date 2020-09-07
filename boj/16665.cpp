#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int gcd(int a, int b) {
   if(b == 0) return a;
   return gcd(b, a % b);
}

bool is_prime(int i) {
    for(int j=2; j<=sqrt(i); j++)
        if(i % j == 0) return false;
    return true;
}

// Return primes smaller than or equal to m.
vector<int> get_primes(int m) {
    vector<int> primes;
    for(int i=2; i<=m; i++)
        if(is_prime(i)) primes.push_back(i);
    return primes;
}

vector<int> get_b(int n) {
    vector<int> b, primes = get_primes(sqrt(n));
    for(int prime : primes)
        if(n % prime == 0) {
            b.push_back(prime);
            if(b.size() == 2) return b;
            if(n / prime != prime && is_prime(n / prime)) b.push_back(n / prime);
            if(b.size() == 2) return b;
        }
    return b;
}

int main() {
    freopen("1.in", "r", stdin);
    int n;
    cin >> n;

    vector<int> b = get_b(n);
    if(b.size() <= 1) {
        cout << "NO";
    } else {
        if(n % 2 == 0) {
            cout << "YES\n";
            cout << "2\n";
            cout << "1 " << n / b[1] << '\n';
            cout << (n - 1 - b[1]) / 2 << ' ' << n / 2;
        } else {
            int a[2];
            for(a[1]=1; a[1]<=b[0]; a[1]++) {
                int m = n - 1 - a[1] * b[1];
                if(m % b[0] == 0) {
                    a[0] = m / b[0];
                    break;
                }
            }
            int gcd0 = gcd(a[0] * b[0], n);
            int gcd1 = gcd(a[1] * b[1], n);
            cout << "YES\n";
            cout << "2\n";
            cout << a[0] * b[0] / gcd0 << ' ' << n / gcd0 << '\n';
            cout << a[1] * b[1] / gcd1 << ' ' << n / gcd1;
        }
    }
}