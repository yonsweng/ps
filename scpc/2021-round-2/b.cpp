#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

long long Answer;
int x[8], y[8];

int main(int argc, char** argv)
{
	int T, test_case;

	// freopen("input.txt", "r", stdin);

	cin >> T;
	for(test_case = 0; test_case  < T; test_case++)
	{
		Answer = 1600000000LL;
		
        int k;
        cin >> k;

        for(int i=0; i<8; i++)
            cin >> x[i] >> y[i];
            
        vector<int> p = {0, 1, 2, 3, 4, 5, 6, 7};

        do {
            long long X[8], Y[8];  // X[i] = 2*x[p[i]] + 2*f*k, where f = 1/2 or 3/2.
            X[0] = 2 * x[p[0]] + k;
            X[1] = 2 * x[p[1]] - k;
            X[2] = 2 * x[p[2]] - 3 * k;
            X[3] = 2 * x[p[3]] - 3 * k;
            X[4] = 2 * x[p[4]] - k;
            X[5] = 2 * x[p[5]] + k;
            X[6] = 2 * x[p[6]] + 3 * k;
            X[7] = 2 * x[p[7]] + 3 * k;
            Y[0] = 2 * y[p[0]] - 3 * k;
            Y[1] = 2 * y[p[1]] - 3 * k;
            Y[2] = 2 * y[p[2]] - k;
            Y[3] = 2 * y[p[3]] + k;
            Y[4] = 2 * y[p[4]] + 3 * k;
            Y[5] = 2 * y[p[5]] + 3 * k;
            Y[6] = 2 * y[p[6]] + k;
            Y[7] = 2 * y[p[7]] - k;
            sort(X, X + 8);
            sort(Y, Y + 8);
            long long mx = X[3], my = Y[3];
            long long s = 0;
            for(int i=0; i<8; i++) {
                s += abs(mx - X[i]);
                s += abs(my - Y[i]);
            }

            Answer = min(Answer, s / 2);
        } while(next_permutation(p.begin(), p.end()));

		cout << "Case #" << test_case+1 << endl;
		cout << Answer << endl;
	}

	return 0;
}