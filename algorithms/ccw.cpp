struct Point {
    int x, y;
};

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