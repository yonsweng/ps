#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
int A[500][500];
int B[500][500];
int R[500], C[500];
int k;

bool comp(const pair<int, int> &a, const pair<int, int> &b) {
    return B[a.first][a.second] < B[b.first][b.second];
}

bool fill_for_free() {
    bool done = true;

    for(int i=0; i<N; i++) {
        int cnt = 0, ii, jj;
        for(int j=0; j<N; j++) {
            if(A[i][j] == -1) {
                cnt++;
                ii = i;
                jj = j;
            }
        }
        if(cnt == 1) {
            A[ii][jj] = 0;
        }
    }

    for(int j=0; j<N; j++)
        for(int i=0; i<N; i++) {

        }

    return done;
}

int pay_one(vector<pair<int, int>> &sorted) {
    int i = sorted[k].first, j = sorted[k].second;
    A[i][j] = 0;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(NULL);
    int T;
    cin >> T;
    for(int x=1; x<=T; x++) {
        cin >> N;
        for(int i=0; i<N; i++)
            for(int j=0; j<N; j++)
                cin >> A[i][j];
        for(int i=0; i<N; i++)
            for(int j=0; j<N; j++)
                cin >> B[i][j];
        for(int i=0; i<N; i++)
            cin >> R[i];
        for(int i=0; i<N; i++)
            cin >> C[i];

        int y = 0;
        vector<pair<int, int>> sorted;

        for(int i=0; i<N; i++)
            for(int j=0; j<N; j++)
                sorted.emplace_back(i, j);
        sort(sorted.begin(), sorted.end(), comp);

        k = 0;
        while(true) {
            if(fill_for_free()) break;
            y += pay_one(sorted);
        }

        cout << "Case #" << x << ": " << y << '\n';
    }
}