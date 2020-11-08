#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

struct Fraction
{
    int num, den;

    Fraction(int n, int d)
    {
        num = n;
        den = d;

        if (den < 0)
        {
            num = -num;
            den = -den;
        }
    }

    bool operator==(const Fraction& f) const
    {
        return num * f.den == den * f.num;
    }

    bool operator<(const Fraction& f) const
    {
        return num * f.den < den * f.num;
    }
};

int m, full = 0;
std::pair<int, int> points[16];
std::map<Fraction, int> slopes;
std::vector<int> slVec;
std::vector<int> setSizes;

void countSets(int currSet, int start, int& result)
{
    if (currSet == full || start == (int)slVec.size())
    {
        int comb = 0;
        for (int s : setSizes)
            comb += (s/2) * ((s/2)-1) / 2;
        result = std::max(result, comb);
        return;
    }

    if ((currSet & slVec[start]) == 0)
    {
        int newSet = currSet | slVec[start];
        setSizes.push_back(__builtin_popcount(slVec[start]));
        countSets(newSet, start+1, result);
        setSizes.pop_back();
    }

    countSets(currSet, start+1, result);
}

int main()
{
    scanf("%d", &m);
    for (int i = 0; i < m; ++i)
    {
        int x, y;
        scanf("%d %d", &x, &y);
        points[i].first = x;
        points[i].second = y;
    }

    for (int i = 0; i < m; ++i)
    {
        for (int j = i+1; j < m; ++j)
        {
            Fraction slope(points[j].second - points[i].second, points[j].first - points[i].first);
            auto found = slopes.find(slope);
            if (found == slopes.end())
                slopes[slope] = (1<<i) + (1<<j);
            else
            {
                found->second |= 1<<i;
                found->second |= 1<<j;
            }
        }
    }

    for (auto p : slopes)
    {
        slVec.push_back(p.second);
        full |= p.second;
    }

    int result = 0;
    countSets(0, 0, result);
    printf("%d", result);
}