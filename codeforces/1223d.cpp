#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>

#define INF 999999999

using namespace std;

int main()
{
	// freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int q;
	cin >> q;
	while(q--) {
		int n;
		cin >> n;

		vector<int> v;
		stack<int> s;
		for(int i=0; i<n; i++) {
			int ai;
			cin >> ai;

			while(!s.empty()) {
				if(ai < s.top()) {
					v.push_back(s.top());
					s.pop();
				}
				else break;
			}

			if(s.empty() || s.top() != ai)
				s.push(ai);
		}

		sort(v.begin(), v.end());

		int cnt = v.empty() ? 0 : 1;
		for(int i=1; i<v.size(); i++)
			if(v[i-1] != v[i]) cnt++;

		cout << cnt << '\n';
	}

	return 0;
}