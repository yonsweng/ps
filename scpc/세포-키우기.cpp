#include <cstdio>

#define MAXN 200001
#define abs(n) ((n >= 0)? (n) : (-(n)))
#define min(a, b) ((a < b)? (a) : (b))
#define max(a, b) ((a > b)? (a) : (b))

int Answer;
int d[MAXN + 100];

int main(int argc, char** argv)
{
	int T, test_case;

	//freopen("input.txt", "r", stdin);

	scanf("%d", &T);
	for(test_case = 0; test_case < T; test_case++)
	{
		Answer = 0;

		for(int i = 0; i < MAXN + 100; i++) {
			d[i] = 999999999;
		}

		/////////////////////////////////////////////////////////////////////////////////////////////
		int l, r, n;
		scanf("%d %d", &l, &r);
		if(r - l > MAXN) {
			scanf("%d", &n);
			for(int i=0; i<n; i++) {
				int x, y;
				scanf("%d %d", &x, &y);
			}
			printf("Case #%d\n%d\n", test_case+1, Answer * 2);
			continue;
		}

		scanf("%d", &n);
		for(int i=0; i<n; i++) {
			int x, y;
			scanf("%d %d", &x, &y);

			for(int x0=l; x0<=r; x0++) {
				d[x0-l] = min(d[x0-l], max(abs(x0 - x), abs(y)));
				//printf("%d ", d[x0-l]);
			}
			//printf("\n");
		}
		/////////////////////////////////////////////////////////////////////////////////////////////
		
		for(int x0=l; x0<=r; x0++) {
			if(Answer < d[x0-l]) {
				Answer = d[x0-l];
			}
		}
		// Print the answer to standard output(screen).
		printf("Case #%d\n%d\n", test_case+1, Answer * 2);
	}

	return 0;//Your program should return 0 on normal termination.
}