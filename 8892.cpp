#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	int t;
	cin >> t;

	for(int test_case=0; test_case<t; test_case++) {
		int k;
		cin >> k;

		char words[100][10001];

		for(int i=0; i<k; i++) {
			cin >> words[i];
		}

		pair<int, int> answer;

		bool out = false;

		// Concatenating
		for(int i=0; i<k; i++) {
			for(int j=0; j<k; j++) {
				if(i != j) {
					bool palindrome = true;
					// words[i] words[j]
					int len1 = strlen(words[i]), len2 = strlen(words[j]);
					char *left = &words[i][0], *right = &words[j][len2-1];

					for(int l=0; l<(len1+len2+1)/2; l++) {
						if(*left != *right) {
							palindrome = false;
							break;
						}

						// over words[i]
						if(l == len1 - 1) left = &words[j][0];
						else left++;

						// over words[j]
						if(l == len2 - 1) right = &words[i][len1-1];
						else right--;
					}

					if(palindrome) {
						answer = make_pair(i, j);
						out = true;
						break;
					}
				}
			}
			if(out) break;
		}

		if(out) cout << words[answer.first] << words[answer.second] << endl;
		else cout << 0 << endl;
	}
	return 0;
}