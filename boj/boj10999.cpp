#include <cstdio>

int tree[4000000], prop[4000000];



int main()
{
	int n, m, k;
	scanf("%d %d %d", &n, &m, &k);

	int leaf_idx;
	for(leaf_idx=1; leaf_idx<n; leaf_idx*=2);

	for(int i=leaf_idx; i<leaf_idx+n; i++)
		scanf("%d", &tree[i]);

	// Fill the segment tree
	for(int i=leaf_idx-1; i>=1; i--)
		tree[i] = tree[i*2] + tree[i*2+1];



	return 0;
}