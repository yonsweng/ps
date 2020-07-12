#include <cstdio>
#include <list>

#define INF 1e6

using namespace std;

int a[1001][1001];

int main() {
    // freopen("1.in", "r", stdin);
    int t;
    scanf("%d", &t);
    for(int case_num=1; case_num<=t; case_num++) {
        int n, q;
        scanf("%d %d", &n, &q);

        list<int> l;
        l.push_back(INF);
        for(int i=1; i<n; i++) {
            int tmp;
            scanf("%d", &tmp);
            l.push_back(i);
            l.push_back(tmp);
        }
        l.push_back(n);
        l.push_back(INF);

        list<int> l_copy = l;

        for(int i=1; i<=n; i++) {
            list<int>::iterator it = l.begin();

            for(int j=0; j<i*2-1; j++) {
                it++;
            }

            for(int j=1; j<=n; j++) {
                a[i][j] = *it;
                auto left = --it;
                ++it;
                auto right = ++it;
                --it;
                l.erase(it);
                if(*left < *right) {
                    it = l.erase(left);
                    --it;
                } else {
                    it = l.erase(right);
                }
            }

            l = l_copy;
        }

        printf("Case #%d:", case_num);
        for(int i=1; i<=q; i++) {
            int s, k;
            scanf("%d %d", &s, &k);
            printf(" %d", a[s][k]);
        }
        printf("\n");
    }
    return 0;
}