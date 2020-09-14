#include <string>
#include <vector>

#define INF 700000000

using namespace std;

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    vector<vector<int>> d(n+1);
    for(int i=0; i<=n; i++) {
        d[i].resize(n+1);
        for(int j=0; j<=n; j++) {
            d[i][j] = INF;
        }
        d[i][i] = 0;
    }

    for(vector<int> fare : fares) {
        int u = fare[0], v = fare[1], w = fare[2];
        d[u][v] = w;
        d[v][u] = w;
    }

    // Floyd
    for(int k=1; k<=n; k++) {
        for(int i=1; i<=n; i++) {
            for(int j=1; j<=n; j++) {
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }

    int answer = INF;
    for(int i=1; i<=n; i++) {
        answer = min(answer, d[s][i] + d[i][a] + d[i][b]);
    }

    return answer;
}

int main() {

}