#include <iostream>

using namespace std;

// 반시계 방향이면 1, 일직선이면 0, 시계 방향이면 -1
int ccw(int x1, int y1, int x2, int y2, int x3, int y3) {
    int z = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);
    if(z > 0)
        return 1;
    else if(z == 0)
        return 0;
    else
        return -1;
}

int main() {
    freopen("input/3.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int x1, y1, x2, y2, x3, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    cout << ccw(x1, y1, x2, y2, x3, y3);

    return 0;
}