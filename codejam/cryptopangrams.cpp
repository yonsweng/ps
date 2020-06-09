#include <cstdio>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

int p[10000] = {2, }, pn = 1;

bool isPrime(int k)
{
	for(int d=2; d <= sqrt(k); d++) {
		if(k % d == 0) return false;
	}
	return true;
}

int gcd(int a, int b)
{
	while(a > 0 && b > 0) {
		if(a > b) {
			a = a % b;
		}
		else {
			b = b % a;
		}
	}

	return (a > b)? a : b;
}

bool visited[103];

void dfs(int a[], int i, int l, int d[])
{
	if(a[i] != 0 || visited[i]) return;

	visited[i] = true;

	if(i > 0) {
		if(a[i-1] == 0)
			dfs(a, i-1, l, d);
		if(a[i-1])
			a[i] = d[i] / a[i-1];
	}

	if(a[i] != 0) return;

	if(i+1 <= l) {
		if(a[i+1] == 0)
			dfs(a, i+1, l, d);
		if(a[i+1])
			a[i] = d[i+1] / a[i+1];
	}
}

int main()
{
	int t;
	scanf("%d", &t);

	for(int test_case = 1; test_case <= t; test_case++) {
		int n, l, d[101], a[103] = {0,}, b[102];
		char ans[102]={0,};
		scanf("%d%d", &n, &l);

		for(int i=0; i<=l; i++) visited[i] = false;

		// n보다 작거나 같은 소수 찾기
		for(int k=p[pn-1]+1; k<=n; k++) {
			if(isPrime(k)) p[pn++] = k;
		}

		for(int i=1; i<=l; i++) {
			scanf("%d", &d[i]);
		}

		for(int i=1; i<l; i++) {
			 int g = gcd(d[i], d[i+1]);
			 if(isPrime(g))
			 	a[i] = g;
		}

		for(int i=0; i<=l; i++) {
			if(a[i] == 0)
				dfs(a, i, l, d);
		}

		for(int i=0; i<=l; i++) {
			b[i] = a[i];
		}
		sort(b, b+l+1);

		// 중복 제거
		int bp = 0;
		for(int i=1; i<=l; i++) {
			if(b[bp] != b[i]) {
				b[++bp] = b[i];
			}
		}

		map<int, char> m;
		for(int i=0; i<=bp; i++) {
			m[b[i]] = 'A' + i;
		}

		for(int i=0; i<=l; i++) {
			ans[i] = m[a[i]];
		}

		printf("Case #%d: %s\n", test_case, ans);
	}

	return 0;
}

/*
1
103 31
217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053
*/