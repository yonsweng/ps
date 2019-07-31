#include <cstdio>

struct node {
	int left, right;
	long long sum;
} tree[4000000];

struct data {
	long long num;
	int tree_idx;
} d[1000001];

long long make_tree(int idx, int left, int right)
{
	if(left > right) return 0;

	tree[idx].left = left;
	tree[idx].right = right;

	if(left == right) {
		tree[idx].sum = d[left].num;
		d[left].tree_idx = idx;
		return tree[idx].sum;
	}

	int mid = (left + right) / 2;
	return tree[idx].sum = make_tree(idx*2, left, mid) + make_tree(idx*2+1, mid+1, right);
}

void update_tree(int idx, long long c)
{
	tree[idx].sum = c;
	idx = idx / 2;

	while(idx > 0) {
		tree[idx].sum = tree[idx*2].sum + tree[idx*2+1].sum;
		idx = idx / 2;
	}
}

long long get_sum(int idx, int left, int right)
{
	if(left <= tree[idx].left && tree[idx].right <= right)
		return tree[idx].sum;

	// out of range
	if(left > tree[idx].right || right < tree[idx].left)
		return 0;

	return get_sum(idx*2, left, right) + get_sum(idx*2+1, left, right);
}

int main()
{
	//freopen("input.txt", "r", stdin);

	int n, m, k;
	scanf("%d %d %d", &n, &m, &k);

	for(int i=1; i<=n; i++) {
		scanf("%lld", &d[i].num);
	}

	make_tree(1, 1, n);

	for(int i=1; i<=m+k; i++) {
		int a, b;
		long long c;
		scanf("%d %d %lld", &a, &b, &c);

		if(a == 1) {
			// change
			update_tree(d[b].tree_idx, c);
		} else {
			// query
			long long sum = get_sum(1, b, c);
			printf("%lld\n", sum);
		}
	}

	return 0;
}