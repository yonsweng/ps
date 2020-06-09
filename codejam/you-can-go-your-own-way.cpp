#include <cstdio>
#include <cstdlib>

char d[50001], m[50001];
bool row[50001], col[50001];

int main()
{
	int t;
	scanf("%d", &t);

	for(int test_case=1; test_case<=t; test_case++) {
		int n;
		scanf("%d", &n);
		scanf("%s", d);

		for(int i=0; i<=n; i++) {
			row[i] = col[i] = false;
		}

		int x=0, y=0;
		for(int i=0; i<2*(n-1); i++) {
			if(d[i] == 'E') {
				row[y] = true;
				x++;
			}
			else {
				col[x] = true;
				y++;
			}
		}

		/*for(int i=0; i<n; i++) {
			printf("%d %d\n", row[i], col[i]);
		}*/


		bool toggle = false;  // false : E, true : S
		int cnt = 0;
		x = 0;  y = 0;

		while(cnt < 2 * (n - 1)) {
			if(toggle) {
				while(col[x]) {
					m[cnt++] = 'E';
					x++;
				}
				row[y] = true;
				toggle = false;
			}
			else {
				while(row[y]) {
					m[cnt++] = 'S';
					y++;
				}
				col[x] = true;
				toggle = true;
			}
			//printf("%d %d\n", x, y);
		}
		m[2 * (n - 1)] = 0;

		printf("Case #%d: %s\n", test_case, m);
	}
	return 0;
}