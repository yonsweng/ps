#include <iostream>

using namespace std;

int dp[1002][1002];
int police[1001][1001];

int min_distance(int i, int j, int W, int x[], int y[]) {
  if (dp[i][j] != -1) {
    return dp[i][j];
  }
  if (i == W + 1 || j == W + 1) {
    return dp[i][j] = 0;
  }
  int k = max(i, j) + 1;
  int d1 = min_distance(k, j, W, x, y) + abs(x[i] - x[k]) + abs(y[i] - y[k]);
  int d2 = min_distance(i, k, W, x, y) + abs(x[j] - x[k]) + abs(y[j] - y[k]);
  if (d1 <= d2) {
    police[i][j] = 1;
  } else {
    police[i][j] = 2;
  }
  return dp[i][j] = min(d1, d2);
}

int main() {
  int N, W;
  cin >> N >> W;

  int x[W + 2], y[W + 2];

  // initialize dp
  for (int i = 0; i < W + 2; i++) {
    for (int j = 0; j < W + 2; j++) {
      dp[i][j] = -1;
    }
  }

  x[0] = 1;
  y[0] = 1;
  x[1] = N;
  y[1] = N;
  for (int i = 2; i < W + 2; i++) {
    cin >> x[i] >> y[i];
  }

  cout << min_distance(0, 1, W, x, y) << endl;

  // trace police
  int i = 0, j = 1;
  while (i != W + 1 && j != W + 1) {
    cout << police[i][j] << endl;
    if (police[i][j] == 1) {
      i = max(i, j) + 1;
    } else {
      j = max(i, j) + 1;
    }
  }

  return 0;
}

/*
5
1
3 3
*/