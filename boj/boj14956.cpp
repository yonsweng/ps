#include <iostream>
#include <algorithm>

using namespace std;

pair<int, int> hilbert(int n, int m)
{
	pair<int, int> p;

	if(n == 2) {
		if(m == 0) {
			p = make_pair(1, 1);
		}
		else if(m == 1) {
			p = make_pair(1, 2);
		}
		else if(m == 2) {
			p = make_pair(2, 2);
		}
		else {  // m == 3
			p = make_pair(2, 1);
		}
	}
	else {
		int half = n / 2;
		int quadrant = m / (half * half);

		p = hilbert(half, m % (half * half));

		if(quadrant == 0) {
			swap(p.first, p.second);
		}
		else if(quadrant == 1) {
			p.second += half;
		}
		else if(quadrant == 2) {
			p.first += half;
			p.second += half;
		}
		else {  // quadrant == 3
			p = make_pair(2 * half - p.second + 1, half - p.first + 1);
		}
	}

	return p;
}

int main()
{
	int n, m;
	cin >> n >> m;

	pair<int, int> answer = hilbert(n, m - 1);

	cout << answer.first << ' ' << answer.second;

	return 0;
}
