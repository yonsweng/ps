#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);

	int t;
	scanf("%d", &t);

	for(int test_case=0; test_case<t; test_case++) {
		int a, b, c, ab, bc, ca;
		scanf("%d %d %d %d %d %d", &a, &b, &c, &ab, &bc, &ca);

		int answer = 0;

		for(int i=0; i<=min(a, b); i++) {
			for(int j=0; j<=min(b-i, c); j++) {
				int k = min(c-j, a-i);

				answer = max(answer, i*ab + j*bc + k*ca);
			}
		}

		printf("%d\n", answer);
	}

	return 0;
}