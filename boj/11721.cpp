#include <iostream>
#include <string>

using namespace std;

int main()
{
	// freopen("2.in", "r", stdin);

	string str;
	cin >> str;

	int cnt = 0;
	for(int i=0; i<(int)str.size(); i++) {
		cout << str[i];
		if(++cnt == 10) {
			cout << '\n';
			cnt = 0;
		}
	}

	return 0;
}