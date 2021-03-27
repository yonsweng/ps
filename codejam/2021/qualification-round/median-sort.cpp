#include <bits/stdc++.h>

using namespace std;

void preorder(int i, vector<pair<int, int>> &cdr, vector<int> &result_idx) {
    if(cdr[i].first != -1) {
        preorder(cdr[i].first, cdr, result_idx);
    }
    result_idx.push_back(i);
    if(cdr[i].second != -1) {
        preorder(cdr[i].second, cdr, result_idx);
    }
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int T, N, Q;
    cin >> T >> N >> Q;

    int questions = 0;
    while(T--) {
        vector<int> tree;
        vector<pair<int, int>> cdr;

        cout << 1 << ' ' << 2 << ' ' << 3 << endl;
        questions++;

        int m;
        cin >> m;

        tree.resize(3);
        cdr.resize(3);
        tree[0] = m;
        cdr[0] = make_pair(1, 2);
        cdr[1] = cdr[2] = make_pair(-1, -1);
        if(m == 1) {
            tree[1] = 2;
            tree[2] = 3;
        } else if(m == 2) {
            tree[1] = 1;
            tree[2] = 3;
        } else {
            tree[1] = 1;
            tree[2] = 2;
        }

        int left_cnt = 1, right_cnt = 1;

        for(int x=4; x<=N; x++) {
            bool left = (left_cnt <= right_cnt);
            int i = left ? 1 : 2, p = 0;
            while(true) {
                if(i == -1) {
                    tree.push_back(x);
                    cdr.emplace_back(-1, -1);
                    if(left) cdr[p].first = tree.size() - 1;
                    else cdr[p].second = tree.size() - 1;
                    break;
                }
                cout << tree[p] << ' ' << tree[i] << ' ' << x << endl;

                cin >> m;
                if(m == tree[p]) {
                    if(left) {  // left node
                        if(i <= 2) right_cnt++;
                        i = cdr[p].second;
                        left = false;
                    } else {    // right node
                        if(i <= 2) left_cnt++;
                        i = cdr[p].first;
                        left = true;
                    }
                } else if(m == tree[i]) {
                    if(left) {  // left node
                        if(i <= 2) left_cnt++;
                        p = i;
                        i = cdr[i].first;
                        left = true;
                    } else {    // right node
                        if(i <= 2) right_cnt++;
                        p = i;
                        i = cdr[i].second;
                        left = false;
                    }
                } else {
                    if(left) {  // left node
                        if(i <= 2) right_cnt++;
                        p = i;
                        i = cdr[i].second;
                        left = false;
                    } else {    // right node
                        if(i <= 2) left_cnt++;
                        p = i;
                        i = cdr[i].first;
                        left = true;
                    }
                }
            }
        }

        vector<int> result_idx;
        preorder(0, cdr, result_idx);
        for(int i : result_idx) {
            cout << tree[i] << ' ';
        }
        cout << endl;

        int respond;
        cin >> respond;
        if(respond == 0) {
            break;
        }
    }
}