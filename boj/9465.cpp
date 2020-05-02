#include <iostream>

using namespace std;

int score[100000][3], d[100000][3];

int main()
{
	int t;
	cin >> t;

	for(int test_case=0; test_case<t; test_case++) {
		int n;
		cin >> n;

		for(int j=0; j<2; j++) {
			for(int i=0; i<n; i++) {
				cin >> score[i][j];
			}
		}

		for(int j=0; j<3; j++) {
			d[0][j] = score[0][j];
		}

		for(int i=1; i<n; i++) {
			for(int j=0; j<3; j++) {
				int max = 0;
				for(int k=0; k<3; k++) {
					if(k != j && d[i-1][k] + score[i][j] > max)
						max = d[i-1][k] + score[i][j];
				}
				d[i][j] = max;
			}
		}

		int max = 0;
		for(int j=0; j<3; j++) {
			if(max < d[n-1][j])
				max = d[n-1][j];
		}

		cout << max << endl;
	}

	return 0;
}