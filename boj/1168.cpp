#include <bits/stdc++.h>

using namespace std;

int tree[100001];

void update(int idx, int val){
	while(idx<=100000){
		tree[idx]+=val;
		idx+=idx&(-idx);
	}
}

// [1...idx]의 합
int query(int idx){
	int ret=0;
	while(idx>0){
		ret+=tree[idx];
		idx-=idx&(-idx);
	}
	return ret;
}

int count(int s, int e, int alive) {
	if(s < e) {
		return query(e) - query(s);
	} else {
		return alive - query(s) + query(e);
	}
}

int main(){
	// freopen("input/1.in", "r", stdin);
	ios::sync_with_stdio(false), cin.tie(nullptr);
	int n, m;
	cin >> n >> m;
	for(int i=1;i<=n;i++)
		update(i, 1);

	int now=0, alive=n;
	cout << "<";
	while(alive > 0){
		int k = (m - 1) % alive + 1;
		int low = k;
		int high = n;
		int next = now;
		while(low <= high) {
			int mid = (low + high) / 2;
			int kmid = (now + mid - 1) % n + 1;
			if(count(now, kmid, alive) >= k) {
				high = mid - 1;
				next = kmid;
			} else {
				low = mid + 1;
			}
		}
		update(next, -1);
		cout << next;
		if(alive > 1) {
			cout << ", ";
		}
		now = next;
		alive--;
	}
	cout << ">";

	return 0;
}