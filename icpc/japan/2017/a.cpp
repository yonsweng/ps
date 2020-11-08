#include <iostream>
#include <algorithm>
#define BLACK 1
#define WHITE 0

typedef long long Long;
Long dp[100][2];
int l, k;

Long countCases(int start, int before)
{
    if (start == l && before == BLACK)
        return 1;
    else if (start >= l)
        return 0;

    Long& result = dp[start][before];

    if (result != -1)
        return result;

    result = countCases(start+1, before ? WHITE : BLACK) + (before ? 1 : 0);
    if (before == WHITE && start + k <= l)
        result += countCases(start+k, BLACK);

    return result;
}

int main()
{
    scanf("%d %d", &l, &k);

    std::fill(&dp[0][0], &dp[0][0] + sizeof(dp) / sizeof(Long), -1);
    Long result = countCases(1, BLACK) + countCases(k, BLACK);
    printf("%lld", result);

    return 0;
}