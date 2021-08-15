#include <iostream>
#include <complex>
#include <vector>

using namespace std;

typedef complex<double> cpx;
 
void fft(vector<cpx> &a, bool inv=false) {
    int n = a.size(), j = 0;
    for (int i = 1; i < n; i++) {
        int bit = n >> 1;
        while (!((j ^= bit) & bit)) bit >>= 1;
        if (i < j) swap(a[i], a[j]);
    }
    for (int i = 1; i < n; i *= 2) {
        double x = inv ? M_PI / i : -M_PI / i;
        cpx w = {cos(x), sin(x)};
        for (int j = 0; j < n; j += i * 2) {
            cpx th = {1, 0};
            for (int k = 0; k < i; k++) {
                cpx tmp = a[i + j + k] * th;
                a[i + j + k] = a[j + k] - tmp;
                a[j + k] += tmp;
                th *= w;
            }
        }
    }
    if (inv)
        for (int i = 0; i < n; i++)
            a[i] /= n;
}

void convolution(vector<cpx> a, vector<cpx> b, vector<cpx> &c) {
    int n = max(a.size(), b.size());
    int i = 0;
    while (1 << i < n * 2) i++;
    n = 1 << i;
    a.resize(n);
    b.resize(n);
    c.resize(n);
    fft(a);
    fft(b);
    for (int i = 0; i < n; i++)
        c[i] = a[i] * b[i];
    fft(c, true);
}

int main(int argc, char** argv)
{
	int T, test_case;

	// freopen("input.txt", "r", stdin);

	cin >> T;
	for(test_case = 0; test_case  < T; test_case++)
	{
		long long Answer = 0;
        int N, K;
        vector<cpx> d[2996];

        cin >> N >> K;

        for(int i=0; i<N+4*K-4; i++)
            d[i].resize(N+4*K-4);

        for(int i=2*K-2; i<2*K-2+N; i++) {
            for(int j=2*K-2; j<2*K-2+N; j++) {
                cin >> d[i][j];
            }
        }

        // Prepare the kernel
        vector<cpx> kernel[1199];

        for(int row=0; row<2*K-1; row++) {
            kernel[row].resize(2*K-1);

            int left_col = abs(K - 1 - row);
            for(int col=left_col; col<K; col++)
                kernel[row][col] = col - left_col + 1;

            for(int col=K; col<2*K-1-abs(K-1-row); col++)
                kernel[row][col] = 2*K-1-abs(K-1-row) - col;
        }

        // convolution
        vector<cpx> product[1199];
        for(int i=0; i<N+2*K-2; i++) {  // top of d
            for(int j=0; j<2*K-1; j++) {  // row of kernel
                // if(i + j >= 2 * K - 2 && i + j < N + 2 * K - 2)
                    convolution(d[i + j], kernel[j], product[j]);
            }

            vector<long long> summation(N+4*K-4-(2*K-2), 0);
            for(int j=0; j<2*K-1; j++) {  // row of product
                for(int k=2*K-2+abs(K-1-j); k<N+4*K-4-abs(K-1-j); k++) {  // column of product
                    if(product[j].size() < k) break;
                    summation[k-(2*K-2)] += (long long)round(product[j][k].real());
                }
            }

            for(int k=2*K-2; k<N+4*K-4; k++) {
                Answer = max(Answer, summation[k-(2*K-2)]);
            }
        }

		// Print the answer to standard output(screen).
		cout << "Case #" << test_case+1 << endl;
		cout << Answer << endl;
	}

	return 0;//Your program should return 0 on normal termination.
}