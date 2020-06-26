#include <iostream>

using namespace std;

int main(void)
{
	unsigned long long m;
	cin >> m;

	unsigned long long n;
	for(n=0;; n++) {
		unsigned long long sum = n;
		for(int i=0; i<n+1; i++) {
			sum += (sum + 1);
		}
		if(sum >= m) break;
	}

	cout << n;

	return 0;
}