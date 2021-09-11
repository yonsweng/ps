#include <string>
#include <vector>
#include <iostream>
#include <tuple>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> &board, vector<vector<int>> &skill) {
    int answer = 0;

    int n = board.size();
    int m = board[0].size();
    vector<int> accu(m);

    vector<tuple<int, int, int, int>> tuples;
    for(auto s : skill) {
        int type=s[0], r1=s[1], c1=s[2], r2=s[3], c2=s[4], degree=s[5];
        tuples.emplace_back(r1, c1, c2, degree*(2*type-3));
        tuples.emplace_back(r2+1, c1, c2, -degree*(2*type-3));
    }

    sort(tuples.begin(), tuples.end());

    int ti = 0;
    for(int i=0; i<n; i++) {
        while(ti < tuples.size() && get<0>(tuples[ti]) == i) {
            tuple<int, int, int, int> &t = tuples[ti];
            accu[get<1>(t)] += get<3>(t);
            if(get<2>(t)+1 < m)
                accu[get<2>(t)+1] -= get<3>(t);
            ti++;
        }
        int tj = 0; long long plus = 0;
        for(int j=0; j<m; j++) {
            plus += accu[j];
            answer = plus + board[i][j] > 0 ? answer + 1 : answer;
        }
    }

    return answer;
}

int main() {
    vector<vector<int>> board = {{5,5,5,5,5},{5,5,5,5,5},{5,5,5,5,5},{5,5,5,5,5}};
    vector<vector<int>> skill = {{1,0,0,3,4,4},{1,2,0,2,3,2},{2,1,0,3,1,2},{1,0,1,3,3,1}};
    int result = solution(board, skill);
    cout << result;
    return 0;
}