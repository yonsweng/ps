#include <cstdio>
#include <vector>

using namespace std;

int main()
{
    int n, m;
    scanf("%d %d", &n, &m);

    vector<int> v(n);
    for (int i=0; i<n; i++)
        v[i] = i + 1;

    int now = 0;
    printf("<");
    while (v.size() > 1)
    {
        now = (now + m - 1) % v.size();
        printf("%d, ", v[now]);
        v.erase(v.begin() + now);
    }
    printf("%d>", v[0]);

    return 0;
}