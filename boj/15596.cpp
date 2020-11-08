#include <vector>
long long sum(std::vector<int> &a) {
    long long s = 0;
    for(int a : a)
        s += a;
    return s;
}