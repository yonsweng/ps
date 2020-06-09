#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	int t;
	char n[101];

	cin >> t;

	for(int test_case=0; test_case<t; test_case++) {
		char a[101] = {0, }, b[101] = {0, };

		cin >> n;

		for(int i=0; i<(int)strlen(n); i++) {
			if(n[i] == '4') {
				a[i] = '2';
				b[i] = '2';
			} else {
				a[i] = n[i];
				b[i] = '0';
			}
		}

		cout << "Case #" << test_case << ": " << a << ' ';

		bool flag0 = false;

		for(int i=0; i<(int)strlen(n); i++) {
			if(flag0) cout << b[i];
			else if(b[i] != '0') {
				flag0 = true;
				cout << b[i];
			}
		}

		cout << endl;
	}

	return 0;
}