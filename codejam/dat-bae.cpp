#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

struct tree_node {
	int l;
	int r;
	int v;
} node[10000];

int main()
{
	int t;
	scanf("%d", &t);

	for(int test_case=1; test_case<=t; test_case++) {
		int n, b, f;
		scanf("%d%d%d", &n, &b, &f);

		memset(node, 0, sizeof(node));

		node[0].l = 0;
		node[0].r = n;
		node[0].v = b;

		int brokens[1030], bi = 0;

		int level;
		for(level=0; level<(int)ceil(log2(n)); level++) {
			char query[1030] = {0,}, qi = 0, answer[1030];

			for(int i=0; i<n; i++) {
				query[i] = '0';
			}

			// level 순회
			for(int i=(int)pow(2, level)-1; i<(int)pow(2, level+1)-1; i++) {
				int mid = (node[i].l + node[i].r) / 2;
				for(int j=node[i].l; j<mid; j++) {
					query[j] = '1';
				}
			}

			printf("%s\n", query);
			fflush(stdout);

			scanf("%s", answer);
			if(answer[0] == '-' && answer[1] == '1') return 0;

			// 0과 1 세기
			int ap = 0;
			for(int i=(int)pow(2, level)-1; i<(int)pow(2, level+1)-1; i++) {
				int tmp = ap + node[i].r - node[i].l - node[i].v;

				int ones = 0, zeros = 0;
				while(ap < tmp) {
					if(answer[ap] == '1') ones++;
					else zeros++;

					ap++;
				}

				if(node[i].l == node[i].r - 1) continue;

				int mid = (node[i].l + node[i].r) / 2;
				int left_child = i * 2 + 1, right_child = i * 2 + 2;

				node[left_child].l = node[i].l;  node[left_child].r = mid;  node[left_child].v = mid - node[i].l - ones;
				node[right_child].l = mid;  node[right_child].r = node[i].r;  node[right_child].v = node[i].r - mid - zeros;
			}
		}

		for(int i=0; i<4*n; i++) {
			if(node[i].l == node[i].r - 1 && node[i].v > 0) brokens[bi++] = node[i].l;
		}

		sort(brokens, brokens + bi);

		for(int i=0; i<bi; i++) {
			printf("%d ", brokens[i]);
		}
		printf("\n");
		fflush(stdout);

		int answer;
		scanf("%d", &answer);
		if(answer != 1) break;
	}
	return 0;
}