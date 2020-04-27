#include <iostream>
#include <vector>

using namespace std;

int main()
{
	// 1000보다 작은 triangle numbers 구하기
	vector<int> tri;
	for(int i=1; ; i++) {
		int tri_num = i * (i + 1) / 2;
		if(tri_num <= 998) tri.push_back(tri_num);
		else break;
	}

	int t;
	cin >> t;

	for(int test_case=0; test_case<t; test_case++) {
		int k;
		cin >> k;

		int flag = false;
		for(int a=0; a<(int)tri.size(); a++) {
			for(int b=a; b<(int)tri.size(); b++) {
				for(int c=b; c<(int)tri.size(); c++) {
					if(tri[a] + tri[b] + tri[c] == k) {
						flag = true;
						break;
					}
				}
				if(flag) break;
			}
			if(flag) break;
		}

		if(flag) cout << 1 << endl;
		else cout << 0 << endl;
	}

	return 0;
}