#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<pair<int, int>> d = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int f(int ai, int aj, int bi, int bj, int cnt, bool turnB, vector<vector<int>> &board) {
    int curr_board = turnB ? board[bi][bj] : board[ai][aj];
    if(curr_board == 0)
        return cnt;

    int n = board.size(), m = board[0].size();
    int f_value = cnt;
    for(auto p : d) {
        if(!turnB) {
            int new_i = ai + p.first, new_j = aj + p.second;
            if(new_i >= 0 && new_i < n && new_j >= 0 && new_j < m && board[new_i][new_j]) {
                board[ai][aj] = 0;
                f_value = max(f_value, 100 - f(new_i, new_j, bi, bj, cnt+1, !turnB, board));
                board[ai][aj] = 1;
            }
        } else {
            int new_i = bi + p.first, new_j = bj + p.second;
            if(new_i >= 0 && new_i < n && new_j >= 0 && new_j < m && board[new_i][new_j]) {
                board[bi][bj] = 0;
                f_value = max(f_value, 100 - f(ai, aj, new_i, new_j, cnt+1, !turnB, board));
                board[bi][bj] = 1;
            }
        }
    }

    return f_value;
}

int solution(vector<vector<int>> board, vector<int> aloc, vector<int> bloc) {
    int answer = f(aloc[0], aloc[1], bloc[0], bloc[1], 0, false, board);
    if(answer > 50) answer = 100 - answer;
    return answer;
}

int main() {
    vector<vector<int>> board = {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}};
    vector<int> aloc = {1, 0};
    vector<int> bloc = {1, 2};
    int result = solution(board, aloc, bloc);
    cout << result;
    return 0;
}