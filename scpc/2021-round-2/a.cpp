#include <iostream>

using namespace std;

long long Answer;

long long count(int R) {
    long long cnt = 0;
    int y = R - 1;
    for(int x = 1; x < R; x++) {
        while((long long)x * x + (long long)y * y >= (long long)R * R) y--;
        cnt += y; 
    }
    return cnt;
}

int main(int argc, char** argv)
{
	int T, test_case;

	// freopen("input.txt", "r", stdin);

	cin >> T;
	for(test_case = 0; test_case  < T; test_case++)
	{
		Answer = 0;

        int R;
        cin >> R;

        Answer = 4 * count(R) + 4 * R - 3;
		
		cout << "Case #" << test_case+1 << endl;
		cout << Answer << endl;
	}

	return 0;//Your program should return 0 on normal termination.
}