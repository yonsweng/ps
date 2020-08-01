#include <bits/stdc++.h>

using namespace std;

int N;
int p[1000];
int S[1000][1000][105];
int B[1000][1000][105];

int silver(int a, int b, int remained, int t1, int t2);
int bronze(int a, int b, int remained, int t1, int t2);

// t1 < t2
int silver(int a, int b, int remained, int t1, int t2) {
    if(S[a][b][(t2-t1)/2] != 0) return S[a][b][(t2-t1)/2];
    if(a == b) return p[a];
    int eat_a, eat_b;
    if(t1 + p[a]*2 < t2) {
        eat_a = p[a] + silver((a+1)%N, b, remained-p[a], t1+p[a]*2, t2);
    } else {
        eat_a = remained - bronze((a+1)%N, b, remained-p[a], t1+p[a]*2, t2);
    }
    if(t1 + p[b]*2 < t2) {
        eat_b = p[b] + silver(a, (b-1+N)%N, remained-p[b], t1+p[b]*2, t2);
    } else {
        eat_b = remained - bronze(a, (b-1+N)%N, remained-p[b], t1+p[b]*2, t2);
    }
    return S[a][b][(t2-t1)/2] = max(eat_a, eat_b);
}

// t1 > t2
int bronze(int a, int b, int remained, int t1, int t2) {
    if(B[a][b][(t1-t2)/2] != 0) return B[a][b][(t1-t2)/2];
    if(a == b) return p[a];
    int eat_a, eat_b;
    if(t2 + p[a]*2 < t1) {
        eat_a = p[a] + bronze((a+1)%N, b, remained-p[a], t1, t2+p[a]*2);
    } else {
        eat_a = remained - silver((a+1)%N, b, remained-p[a], t1, t2+p[a]*2);
    }
    if(t2 + p[b]*2 < t1) {
        eat_b = p[b] + bronze(a, (b-1+N)%N, remained-p[b], t1, t2+p[b]*2);
    } else {
        eat_b = remained - silver(a, (b-1+N)%N, remained-p[b], t1, t2+p[b]*2);
    }
    return B[a][b][(t1-t2)/2] = max(eat_a, eat_b);
}

int main() {
    // freopen("1.in", "r", stdin);

    int sum = 0;
    cin >> N;
    for(int i=0; i<N; i++) {
        cin >> p[i];
        sum += p[i];
    }

    if(N == 1) cout << p[0];
    else if(N == 2) {
        sort(p, p+N);
        cout << p[1];
    } else {
        int answer = 0;
        for(int i=0; i<N; i++) {
            int eat_i = sum - bronze((i+1)%N, (i-1+N)%N, sum - p[i], p[i]*2, 1);
            answer = max(answer, eat_i);
        }
        cout << answer;
    }
}