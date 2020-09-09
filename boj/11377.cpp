#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> works;
vector<int> worker;
vector<bool> visited;

bool assign(int i) {
    if(visited[i])
        return false;
    visited[i] = true;

    bool ret = false;
    for(int j : works[i])
        if(worker[j] != i && (!worker[j] || assign(worker[j]))) {
            worker[j] = i;
            ret = true;
            break;
        }

    visited[i] = false;
    return ret;
}

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);
    int N, M, K;
    cin >> N >> M >> K;

    works.resize(N+1);
    worker.resize(M+1);
    visited.resize(N+1);

    for(int i=1; i<=N; i++) {
        int nWorks;
        cin >> nWorks;
        for(int j=1; j<=nWorks; j++) {
            int work;
            cin >> work;
            works[i].push_back(work);
        }
    }

    for(int i=1; i<=N; i++)
        assign(i);

    int sum = 0;
    for(int i=1; i<=N && sum<K; i++)
        sum += assign(i);

    sum = 0;
    for(int i=1; i<=M; i++)
        if(worker[i])
            sum++;

    cout << sum;
}