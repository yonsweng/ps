#include <iostream>
#include <ctime>
#define min(a, b) ((a < b)? a : b)
#define MAXN 600000
using namespace std;

int f[MAXN+1];

int main(int argc, char** argv)
{
    //clock_t start_t = clock();
	int T;

	//freopen("input.txt", "r", stdin);

    for(long long n = 0; n <= MAXN; n++) {
        f[n] = 999999999;
    }

    f[0] = 0;
    for(long long n = 0; n < MAXN; n++) {
        for(long long m = n + 1, term = 1; m <= MAXN; m += ++term) {
            f[m] = min(f[m], f[n] + term);
        }
    }
    /* for(long long n = 0; n < 100; n++) {
        cout << n << " " << f[n] << endl;
    }*/

	cin >> T;
	for(int test_case = 0; test_case < T; test_case++)
	{
		int Answer = 0;

		long long x, y;
        cin >> x >> y;

        for(long long n = x; n <= y; n++) {
            if(n <= MAXN && Answer < f[n]) {
                Answer = f[n];
            }
        }
		
		// Print the answer to standard output(screen).
		cout << "Case #" << test_case+1 << endl;
		cout << Answer << endl;
	}



    //cout << (clock() - start_t) / (double)CLOCKS_PER_SEC << endl;

	return 0;
}
