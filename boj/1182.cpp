#include <iostream>

using namespace std;

int subseq(int a[], int n, int s, int i, int sum)
{
	if(i == n) {
		if(sum == s)
			return 1;
		else
			return 0;
	}
	else
		return subseq(a, n, s, i+1, sum) + subseq(a, n, s, i+1, sum+a[i]);
}

int main()
{
	int n, s;
	cin >> n >> s;

	int a[20];
	for(int i=0; i<n; i++)
		cin >> a[i];

	int answer = 0;

	for(int i=0; i<n; i++)
		answer += subseq(a, n, s, i+1, a[i]);

	cout << answer;

	return 0;
}