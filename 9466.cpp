#include <cstdio>

int main()
{
	int t;
	scanf("%d", &t);

	for(int test_case=0; test_case<t; test_case++) {
		int n;
		scanf("%d", &n);

		int s[100001];
		for(int i=1; i<=n; i++)
			scanf("%d", &s[i]);
			//s[i] = i;

		bool g[100001] = {false, };
		int visited[100001] = {0, };

		for(int i=1; i<=n; i++) {
			// Put i into a stack if i is not grouped.
			if(g[i] == false && visited[i] == 0) {
				int stack[100000], sp = 0;
				int now = i;

				// Loop until come to visited again.
				while(visited[now] == 0) {
					stack[sp++] = now;
					visited[now] = i;

					now = s[now];
				}

				if(visited[now] == i)
					while(sp > 0) {
						int top = stack[--sp];
						g[top] = true;

						if(top == now) break;
					}
			}
		}

		int cnt = 0;

		for(int i=1; i<=n; i++) {
			if(g[i] == false) cnt++;
		}

		printf("%d\n", cnt);
	}

	return 0;
}