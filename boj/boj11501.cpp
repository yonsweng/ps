#include <cstdio>
#include <algorithm>

using namespace std;

int p[1000000];
pair<int, int> s[1000000];

bool comp(pair<int, int> &a, pair<int, int> &b)
{
	return a.second > b.second;
}

int main()
{
	//freopen("input.txt", "r", stdin);

	int t;
	scanf("%d", &t);

	// 64bit integer

	for(int test_case=0; test_case<t; test_case++) {
		int n;
		scanf("%d", &n);

		for(int i=0; i<n; i++) {
			scanf("%d", &p[i]);
			s[i].first = i;
			s[i].second = p[i];
		}

		sort(s, s+n, comp);

		long long answer = 0;
		int flag = 0;
		for(int i=0; i<n; i++) {
			if(s[i].first >= flag) {
				long long sum = 0;
				for(int j = flag; j < s[i].first; j++) {
					sum += p[j];
				}
				answer += (long long)(s[i].first - flag) * p[s[i].first] - sum;
				flag = s[i].first + 1;
			}
		}

		printf("%lld\n", answer);
	}
	return 0;
}