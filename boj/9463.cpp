#include <cstdio>
#include <algorithm>

int find_sti(int st[], int begin, int end, int sti, int idx)
{
	if(begin < end) {
		int mid = (begin + end) / 2;
		if(idx <= mid) return find_sti(st, begin, mid, sti*2, idx);
		else return find_sti(st, mid+1, end, sti*2+1, idx);
	}
	else
		return sti;
}

void update_st(int st[], int sti)
{
	if(sti > 0) {
		st[sti]++;
		update_st(st, sti/2);
	}
}

int count_st(int st[], int begin, int end, int sti, int left, int right)
{
	if(right < begin || end < left)
		return 0;
	else if(left <= begin && end <= right)
		return st[sti];
	else {
		int mid = (begin + end) / 2;
		return count_st(st, begin, mid, sti*2, left, right) + count_st(st, mid+1, end, sti*2+1, left, right);
	}
}

int main()
{
//	freopen("input.txt", "r", stdin);

	int t;
	scanf("%d", &t);

	for(int test_case=0; test_case<t; test_case++) {
		int n;
		scanf("%d", &n);

		std::pair<int, int> edge[100001];

		for(int i=1; i<=n; i++) {
			int a;
			scanf("%d", &a);
			edge[a].first = i;
		}
		for(int i=1; i<=n; i++) {
			int b;
			scanf("%d", &b);
			edge[b].second = i;
		}

		std::sort(edge+1, edge+1+n);

		long long sum = 0;
		int st[300000] = {0, };  // segment tree

		// Make a segment tree
		for(int i=1; i<=n; i++) {
			// Count larger than edge[i].second
			sum += count_st(st, 1, n, 1, edge[i].second+1, n);
			update_st(st, find_sti(st, 1, n, 1, edge[i].second));
		}

		printf("%lld\n", sum);
	}

	return 0;
}