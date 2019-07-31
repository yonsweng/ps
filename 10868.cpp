#include <cstdio>
#include <climits>
#include <algorithm>

int tree[400000];

int find_min(int idx, int left, int right, int a, int b)
{
	if(a <= left && right <= b)
		return tree[idx];

	if(b < left || right < a)
		return INT_MAX;

	return std::min(find_min(idx*2, left, (left+right)/2, a, b), find_min(idx*2+1, (left+right)/2+1, right, a, b));
}

int main()
{
	int n, m;
	scanf("%d %d", &n, &m);

	int leaf_idx;
	for(leaf_idx=1; leaf_idx<n; leaf_idx*=2);

	for(int i=0; i<n; i++)
		scanf("%d", &tree[leaf_idx+i]);
	for(int i=leaf_idx+n; i<leaf_idx*2; i++)
		tree[i] = INT_MAX;

	// Fill the segment tree
	for(int i=leaf_idx-1; i>=1; i--)
		tree[i] = (tree[i*2] < tree[i*2+1]) ? tree[i*2] : tree[i*2+1];

	for(int i=1; i<=m; i++) {
		int a, b;
		scanf("%d %d", &a, &b);

		printf("%d\n", find_min(1, 1, leaf_idx, a, b));
	}

	return 0;
}