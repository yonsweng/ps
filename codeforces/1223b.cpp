#include <iostream>
#include <string>

using namespace std;

int main()
{
	// freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int q;
	cin >> q;
	while(q--) {
		string s, t;
		cin >> s >> t;

		bool ap[26] = {};
		for(char c : s)
			ap[c-'a'] = true;

		bool answer = false;
		for(char c : t)
			if(ap[c-'a']) {
				answer = true;
				break;
			}

		if(answer) cout << "YES\n";
		else cout << "NO\n";
	}

	return 0;
}