#include<iostream>
#include<algorithm>

using namespace std;

int A[5000];
pair<int, int> sum[12497500];

bool cmp(pair<int, int> a, pair<int, int> b){
	if(a.first < b.first)
		return true;
	else
		return false;
}

int main(void){
	//freopen("input.txt", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n,w;
	cin >> w >> n;
	for(int i = 0; i < n; i++)
		cin >> A[i];
	int p = 0;
	for(int i = 0; i < n; i++)
		for(int j = i + 1; j < n; j++){
			sum[p].second = i * 10000 + j;
			sum[p++].first = A[i] + A[j];
		}
	sort(sum, sum + p, cmp);
	for(int i = 0; i < p ; i++){
		int left = 0, right = p - 1;
		while(left <= right){
			int mid = (left + right) / 2;
			if(sum[i].first + sum[mid].first == w){
				int index[4] = {sum[i].second/10000, sum[i].second % 10000, sum[mid].second/10000, sum[mid].second % 10000};
				bool flag = false;
				for(int j = 0; j < 4; j++){
					for(int k = j + 1; k < 4; k++){
						if(index[j] == index[k]){
							flag = true;
							break;
						}
					}
					if(flag)
						break;
				}
				if(flag)
					break;
				else{
					cout << "YES\n";
					return 0;
				}
			}
			else if (sum[i].first + sum[mid].first < w){
				left = mid + 1;
			}
			else
				right = mid - 1;
		}
	}
	cout << "NO\n";
	return 0;
}