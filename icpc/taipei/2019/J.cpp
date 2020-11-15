#include <iostream>
#include <algorithm>

int n, m;
bool data[15][501];

bool isFull(bool current[])
{
    for (int i = 0; i < n; ++i)
        if (!current[i])
            return false;
    return true;
}

int countMin(int index, bool current[])
{
    if (index == m)
    {
        if (isFull(current))
            return 0;
        else return 100;
    }

    bool next[500];
    for (int i = 0; i < n; ++i)
        next[i] = current[i] | data[index][i];
    return std::min(countMin(index+1, current), countMin(index+1, next) + 1);
}

int main()
{
    int T;
    scanf("%d", &T);

    while (T--)
    {
        scanf("%d %d", &n, &m);

        for (int i = 0; i < m; ++i)
        {
            char line[501];
            scanf("%s", line);
            for (int j = 0; j < n; ++j)
                data[i][j] = (line[j] == '1');
        }

        bool current[500];
        std::fill(current, current+n, false);
        int count = countMin(0, current);
        printf("%d\n", count > m ? -1 : count);
    }

    return 0;
}