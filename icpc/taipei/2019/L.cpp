#include <iostream>
#include <algorithm>
#include <cmath>
#define x first
#define y second
#define dis(a, b) 1LL*(a.x-b.x)*(a.x-b.x)+1LL*(a.y-b.y)*(a.y-b.y)

const int MAXN = 4096;
int T, n;
typedef std::pair<int, int> point;
point p[MAXN], ch[MAXN], ra, rb;
long long ccw(point a, point b, point c)
{
    return 1LL * (b.x - a.x) * (c.y - a.y) - 1LL * (c.x - a.x) * (b.y - a.y);
}

double getDistWithLine(point l1, point l2, point p)
{
    long long a = l2.y - l1.y;
    long long b = l1.x - l2.x;
    long long c = -l1.x * (l2.y-l1.y) + l1.y * (l2.x-l1.x);
    return (a * p.x + b * p.y + c) / sqrt(a*a+b*b);
}

int main()
{
    scanf("%d", &T);

    while (T--)
    {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
            scanf("%d %d", &p[i].x, &p[i].y);

        std::swap(p[0], *std::min_element(p, p+n));
        std::sort(p+1, p+n, [](point l, point r) {
            long long c = ccw(p[0], l, r);
            return c > 0 || !c && l<r;
        });

        int sz = 0;
        for (int i = 0; i < n; ++i)
        {
            while (sz > 1 && ccw(ch[sz-2], ch[sz-1], p[i]) <= 0)
                --sz;

            ch[sz++] = p[i];
        }

        double answer = 0;
        for (int i = 0, j = 1; i < sz; ++i)
        {
            while (ccw(ch[i], ch[(i+1)%sz], {ch[i].x + ch[(j+1) % sz].x - ch[j].x, ch[i].y + ch[(j+1) % sz].y - ch[j].y}) > 0)
                j = (j+1) % sz;
            double dist = sqrt(dis(ch[i], ch[j]));
            double h1 = 0, h2 = 0;
            for (int current = (i+1)%sz; current != j; current = (current+1)%sz)
                h1 = std::max(h1, getDistWithLine(ch[i], ch[j], ch[current]));
            for (int current = (j+1)%sz; current != i; current = (current+1)%sz)
                h2 = std::max(h2, getDistWithLine(ch[i], ch[j], ch[current]));

            answer = std::max(answer, dist * (h1+h2) / 2);
        }
        printf("%lf", answer);

        // long long temp = (long long)round(answer*2);
        // printf("%lld", temp / 2);
        // if (temp % 2)
        //     printf(".5\n");
        // else printf("\n");
    }
}