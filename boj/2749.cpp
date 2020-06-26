#include <iostream>
#include <cmath>

using namespace std;

long long b[60][2][2];

void multiply(long long u[][2], long long v[][2], long long dest[][2])
{
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			long long sum = 0;
			for (int k = 0; k < 2; k++) {
				sum += u[i][k] * v[k][j] % 1000000;
			}
			dest[i][j] = sum % 1000000;
		}
	}
}

int main()
{
	long long n;
	cin >> n;

	const int MAXK = log2(n);
	//cout << MAXK;

	// B0
	b[0][0][0] = 1;  b[0][0][1] = 1;
	b[0][1][0] = 1;  b[0][1][1] = 0;

	// Calc Bk
	for (int k = 1; k <= MAXK; k++) {
		multiply(b[k - 1], b[k - 1], b[k]);

		/*for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 2; j++) {
				cout << b[k][i][j] << '\t';
			}
			cout << '\n';
		}
		cout << '\n';*/
	}

	// Calc An
	long long a[2][2] = { {1, 0}, {0, 1} };
	for (int k = 0; n > 0; k++) {
		if (n % 2 == 1) {
			// copy
			long long tmp[2][2];
			for (int i = 0; i < 2; i++) {
				for (int j = 0; j < 2; j++) {
					tmp[i][j] = a[i][j];
				}
			}

			multiply(tmp, b[k], a);
		}

		/*for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 2; j++) {
				cout << a[i][j] << '\t';
			}
			cout << '\n';
		}*/

		n /= 2;
	}

	cout << a[0][1];

	return 0;
}

// n <= 1000000000000000000