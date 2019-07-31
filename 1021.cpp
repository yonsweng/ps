#include <cstdio>
#include <list>

using namespace std;

int main()
{
	int n, m;
	scanf("%d %d", &n, &m);

	int b[50];
	for(int i=0; i<m; i++) {
		scanf("%d", &b[i]);
	}

	list<int> a;
	for(int i=1; i<=n; i++) {
		a.push_back(i);
	}

	int cnt = 0;
	list<int>::iterator iter = a.begin();
	for(int i=0; i<m; i++) {
		// Find b[i].
		int l = 0, r = 0;
		list<int>::iterator prev = iter;

		// Left
		while(*iter != b[i]) {
			if(iter == a.begin()) iter = a.end();
			iter--;
			l++;
		}

		// Right
		iter = prev;
		while(*iter != b[i]) {
			iter++;
			if(iter == a.end()) iter = a.begin();
			r++;
		}

		cnt += (l < r) ? l : r;  // Add smaller one.

		prev = iter;

		iter++;
		if(iter == a.end()) iter = a.begin();

		a.erase(prev);

		//printf("%d %d\n", l, r);
	}

	printf("%d", cnt);

	return 0;
}