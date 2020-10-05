#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    int x, y;
};
vector<Point> p;

// 반시계 방향이면 1, 일직선이면 0, 시계 방향이면 -1.
int ccw(Point &p1, Point &p2, Point &p3) {
    int z = (long long)(p2.x - p1.x) * (p3.y - p1.y) - (long long)(p2.y - p1.y) * (p3.x - p1.x);
    if(z > 0)
        return 1;
    else if(z == 0)
        return 0;
    else
        return -1;
}

long long sq_dist(Point &a, Point &b) {
    return (long long)(a.x - b.x) * (a.x - b.x) + (long long)(a.y - b.y) * (a.y - b.y);
}

bool comp(Point &a, Point &b) {
    int c = ccw(p[0], a, b);
    if(c == 1)
        return true;
    else if(c == 0) {
        if(sq_dist(p[0], a) < sq_dist(p[0], b))
            return true;
        else
            return false;
    } else
        return false;
}

// Return: the number of points in the convex hull.
int convex_hull(stack<Point> &s) {
    // y 좌표가 가장 작으면서 x가 가장 작은 점 찾기.
    int n = int(p.size()), mi = 0;
    for(int i=1; i<n; i++)
        if(p[i].y < p[mi].y || (p[i].y == p[mi].y && p[i].x < p[mi].x))
            mi = i;

    swap(p[0], p[mi]);

    // 반시계 방향으로 정렬.
    sort(p.begin() + 1, p.end(), comp);

    s.push(p[0]), s.push(p[1]);
    for(int i=2; i<n; i++) {
        Point a, b, c = p[i];
        do {
            b = s.top(), s.pop();
            a = s.top();
        } while(int(s.size()) >= 2 && ccw(a, b, c) <= 0);
        if(ccw(a, b, c) == 1)
            s.push(b);
        s.push(c);
    }

    return int(s.size());
}

int main() {
    freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int n;
    stack<Point> s;

    cin >> n;
    p.resize(n);
    for(int i=0; i<n; i++)
        cin >> p[i].x >> p[i].y;

    cout << convex_hull(s);

    return 0;
}