#include <iostream>

using namespace std;

int main()
{
	int a, b, c;
	cin >> a >> b >> c;

	int d[31] = {a % c, };  // d[i] : 10^(2^i) % c
	for(unsigned int i=1, p=2; p<=b; i++, p*=2)
		d[i] = (long long)d[i-1] * d[i-1] % c;

	long long r = 1;
	for(unsigned int i=0, p=1; p<=b; i++, p*=2) {
		if(b/p%2 == 1) {
			r = r * d[i] % c;
		}
	}

	cout << r;

	return 0;
}