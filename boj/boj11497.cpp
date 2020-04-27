#include <cstdio>
#include <algorithm>

int main()
{
	//freopen("input.txt", "r", stdin);

	int t;
	scanf("%d", &t);
	for(int test_case=0; test_case<t; test_case++) {
		int n, d[10000];
		scanf("%d", &n);
		for(int i=0; i<n; i++) {
			scanf("%d", &d[i]);
		}

		std::sort(d, d+n);

		int max_diff = (d[1] - d[0] > d[2] - d[0]) ? (d[1] - d[0]) : (d[2] - d[0]);
		for(int i=2; i<n; i++) {
			if(max_diff < d[i] - d[i-2]) {
				max_diff = d[i] - d[i-2];
			}
		}

		printf("%d\n", max_diff);
	}

	return 0;
}
