#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
	//freopen("input.txt", "r", stdin);

	vector<int> primes;  // primes from 2 to 333

	for(int n=2; n<1000; n++) {
		// Check if n is a prime.
		bool isPrime = true;

		for(int m=2; m<=sqrt(n); m++) {
			if(n % m == 0) {
				isPrime = false;
			}
		}

		if(isPrime) {
			primes.push_back(n);
		}
	}

	//printf("%lu", primes.size());  // 67

	int t;
	scanf("%d", &t);

	for(int test_case=0; test_case<t; test_case++) {
		int k;
		scanf("%d", &k);

		bool ok = false;

		for(int a=0; a<primes.size(); a++) {
			for(int b=a; b<primes.size(); b++) {
				for(int c=b; c<primes.size(); c++) {
					if(primes[a] + primes[b] + primes[c] == k) {
						ok = true;
						printf("%d %d %d\n", primes[a], primes[b], primes[c]);
						break;
					}
				}
				if(ok) break;
			}
			if(ok) break;
		}

		if(!ok) {
			printf("0\n");
		}
	}
	return 0;
}