#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Student {
	int d;
	vector<int> A;

	bool operator<(const Student& b) const {
		return d < b.d;
	}
} s[100000];

int K, cnt[31];

void push_one(int i)
{
	for(int a : s[i].A) {
		cnt[a]++;
	}
}

void pop_one(int i)
{
	for(int a : s[i].A) {
		cnt[a]--;
	}
}

int calc_efficiency(int n)
{
	int p = 0, q = 0;
	for(int a=1; a<=K; a++) {
		if(cnt[a]) p++;
		if(cnt[a] == n) q++;
	}

	return (p - q) * n;
}

int main()
{
	freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N, D;
	cin >> N >> K >> D;

	for(int i=0; i<N; i++) {
		int M;
		cin >> M >> s[i].d;

		for(int j=0; j<M; j++) {
			int tmp;
			cin >> tmp;
			s[i].A.push_back(tmp);
		}
	}

	sort(s, s + N);

	int answer = 0;

	int i = 0, j = 0;
	while(j < N) {
		if(s[j].d - s[i].d <= D) {
			push_one(j++);
			answer = max(answer, calc_efficiency(j-i));
		}
		else {
			pop_one(i++);
		}
	}

	cout << answer;

	return 0;
}