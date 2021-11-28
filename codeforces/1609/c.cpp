// C++ program to generate all prime numbers
// less than N in O(N)
#include <iostream>
#include <vector>

using namespace std;
const long long MAX_SIZE = 1000001;
 
// isPrime[] : isPrime[i] is true if number is prime
// prime[] : stores all prime number less than N
// SPF[] that store smallest prime factor of number
// [for Exp : smallest prime factor of '8' and '16'
// is '2' so we put SPF[8] = 2 , SPF[16] = 2 ]
vector<long long >isprime(MAX_SIZE , true);
vector<long long >prime;
vector<long long >SPF(MAX_SIZE);
 
// function generate all prime number less then N in O(n)
void manipulated_seive(int N)
{
    // 0 and 1 are not prime
    isprime[0] = isprime[1] = false ;
 
    // Fill rest of the entries
    for (long long int i=2; i<N ; i++)
    {
        // If isPrime[i] == True then i is
        // prime number
        if (isprime[i])
        {
            // put i into prime[] vector
            prime.push_back(i);
 
            // A prime number is its own smallest
            // prime factor
            SPF[i] = i;
        }
 
        // Remove all multiples of  i*prime[j] which are
        // not prime by making isPrime[i*prime[j]] = false
        // and put smallest prime factor of i*Prime[j] as prime[j]
        // [ for exp :let  i = 5 , j = 0 , prime[j] = 2 [ i*prime[j] = 10 ]
        // so smallest prime factor of '10' is '2' that is prime[j] ]
        // this loop run only one time for number which are not prime
        for (long long int j=0;
             j < (int)prime.size() &&
             i*prime[j] < N && prime[j] <= SPF[i];
             j++)
        {
            isprime[i*prime[j]]=false;
 
            // put smallest prime factor of i*prime[j]
            SPF[i*prime[j]] = prime[j] ;
        }
    }
}
 
// driver  program to test above function
int main()
{
    manipulated_seive(1000001);
    // cout << isprime[4];
    int t;
    cin >> t;
    while(t--) {
        int n, e;
        cin >> n >> e;
        vector<int> a(n);
        for(int i=0; i<n; i++) cin >> a[i];

        long long answer = 0;
        for(int i=0; i<e; i++) {
            for(int j=i; j<n; j+=e) {
                if(isprime[a[j]]) {
                    
            int l = 0, r = 0;
                    // cout << j << '\n';
                    for(int k=j-e; k>=i; k-=e) {
                        if(a[k] == 1) l++;
                        else break;
                    }
                    for(int k=j+e; k<n; k+=e) {
                        if(a[k] == 1) r++;
                        else {
                            j = k - e;
                            break;
                        }   
                    }
                    answer += (long long)l * r + l + r;
                }
            }
        }
        cout << answer << '\n';
    }
 
    return 0;
}