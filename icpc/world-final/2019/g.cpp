#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

#define MAX 1000000

using namespace std;

int n, next_i[20][MAX];

int d, pos[MAX];  // pos: 그룹 번호
// 접미사 비교에 사용할 비교 함수
bool cmp(int i, int j){
    // 먼저 자신의 위치의 문자를 비교
    if(pos[i] != pos[j]) return pos[i] < pos[j];
    // 문자가 같으면 d칸 뒤의 문자끼리 비교
    i = next_i[d][i];
    j = next_i[d][j];
    return (i < n && j < n) ? (pos[i] < pos[j]) : (i > j);
}
// S를 사용해 sa 배열을 만드는 함수
vector<int> construct_sa(string &s) {
    vector<int> sa(n);
    // 전처리
    for(int i=0; i<n; i++){
        sa[i] = i;
        pos[i] = s[i]; // 제일 첫 번째 루프에서는 제자리 문자로 비교
    }
    // d를 2배씩 늘려가면서 매번 앞에서부터 d*2글자만 보고 접미사 정렬
    for(d=0; d<20; d++){
        sort(sa.begin(), sa.end(), cmp);
        // temp: 새로운 그룹 번호
        vector<int> temp(MAX, 0);
        // 앞에서부터 훑으면서 각 접미사가 서로 다른 그룹에 속할 때마다 그룹 번호 증가시킴
        for(int i=0; i<n-1; i++)
            temp[i+1] = temp[i] + cmp(sa[i], sa[i+1]);
        // pos 배열을 temp 배열로 대체
        for(int i=0; i<n; i++)
            pos[sa[i]] = temp[i];
        // 모든 접미사가 다른 그룹으로 나뉘어졌다면 종료
        if(temp[n-1] == n-1) break;
    }
    return sa;
}

// -1 if s < q, 0 if s == q, 1 if s > q
int compare(string &s, string &q, int si) {
    for(int i=0; i<q.size(); i++) {
        if(si >= n || s[si] < q[i]) {
            return -1;
        } else if(s[si] > q[i]) {
            return 1;
        }
        si = next_i[0][si];
    }
    return 0;
}

int lowerBound(string &s, vector<int> &sa, string &q) {
    int l = 0, r = n;
    int lb = n;
    while(l < r) {
        int m = (l + r) / 2;
        int cp = compare(s, q, sa[m]);
        if(cp == -1) {
            // go right
            l = m + 1;
        } else if(cp == 0) {
            // go left
            lb = min(lb, m);
            r = m;
        } else {
            // go left
            r = m;
        }
    }
    return lb;
}

int upperBound(string &s, vector<int> &sa, string &q) {
    int l = 0, r = n;
    int ub = 0;
    while(l < r) {
        int m = (l + r) / 2;
        int cp = compare(s, q, sa[m]);
        if(cp == -1) {
            // go right
            l = m + 1;
        } else if(cp == 0) {
            // go right
            ub = max(ub, m + 1);
            l = m + 1;
        } else {
            // go left
            r = m;
        }
    }
    return ub;
}
 
int main(){
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int k;
    cin >> n >> k;
    string s;
    s.resize(n);
    for(int i=n-1; i>=0; i--) {
        char c; int p;
        cin >> c >> p;
        s[i] = c;
        next_i[0][i] = n - p;
    }

    for(int j=1; j<20; j++) {
        for(int i=0; i<n; i++) {
            next_i[j][i] = next_i[j-1][next_i[j-1][i]];
        }
    }

    vector<int> sa = construct_sa(s);

    while(k--) {
        string q;
        cin >> q;
        int lb = lowerBound(s, sa, q);
        int ub = upperBound(s, sa, q);
        cout << max(0, ub - lb) << '\n';
    }

    return 0;
}