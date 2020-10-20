#include <bits/stdc++.h>
using namespace std;

int main() {
    // freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);
    int T;
    cin >> T;
    for(int x=1; x<=T; x++) {
        long long answer = 0;
        int W, N;
        vector<int> X;
        multiset<long long> dq;

        cin >> W >> N;

        X.resize(W);
        for(int i=0; i<W; i++)
            cin >> X[i];

        dq.insert(X[0]);
        multiset<long long>::iterator it = dq.begin();
        for(int i=1; i<W; i++) {
            int mid = *it;
            mid = mid > 0 ? mid % N : (N - mid) % N;
            int left, right;
            int left_dist, right_dist;
            if(X[i] >= mid) {
                right = X[i];
                left = X[i] - N;
            } else {
                left = X[i];
                right = X[i] + N;
            }
            left_dist = mid - left;
            right_dist = right - mid;

            if(left_dist < right_dist) {
                dq.insert(*it - left_dist);
                it--;
                // answer += left_dist;
            }
            else {
                dq.insert(*it + right_dist);
                it++;
                // answer += right_dist;
            }
        }

        int mid = 0, i = 0;
        for(multiset<long long>::iterator it=dq.begin(); it!=dq.end(); it++, i++) {
            if(i == int(dq.size()) / 2) {
                mid = *it;
                break;
            }
        }


        for(multiset<long long>::iterator it=dq.begin(); it!=dq.end(); it++) {
            int left, right;
            int left_dist, right_dist;
            if(X[i] < 1) {
                right = X[i];
                left = X[i];
            } else {
                left = X[i];
                right = X[i] + N;
            }
            left_dist = mid - left;
            right_dist = right - mid;

            if(left_dist < right_dist) {
                dq.insert(left);
                it--;
                // answer += left_dist;
            }
            else {
                dq.insert(right);
                it++;
                // answer += right_dist;
            }

            answer += dist;
        }

        cout << "Case #" << x << ": " << answer << '\n';
    }
}