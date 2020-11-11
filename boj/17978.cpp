#include <bits/stdc++.h>

using namespace std;

struct Vec3 {
    int i, j, k;
};

Vec3 cross(Vec3 &x, Vec3 &y) {
    return {x.j*y.k-x.k*y.j, x.k*y.i-x.i*y.k, x.i*y.j-x.j*y.i};
}

int inner(Vec3 &x, Vec3 &y) {
    return x.i * y.i + x.j * y.j + x.k * y.k;
}

int main() {
    // freopen("input/1.in", "r", stdin);

    int n, k;
    scanf("%d %d", &n, &k);
    vector<int> r(n+1), g(n+1), b(n+1);
    for(int i=1; i<=n; i++) {
        scanf("%d %d %d", &r[i], &g[i], &b[i]);
    }

    if(k == 1) {
        long long sum_sq = 0, r_sum = 0, g_sum = 0, b_sum = 0;
        for(int i=1; i<=n; i++) {
            sum_sq += r[i] * r[i] + g[i] * g[i] + b[i] * b[i];
            r_sum += r[i];
            g_sum += g[i];
            b_sum += b[i];
        }
        long long sq_sum = (long long)r_sum * r_sum
                         + (long long)g_sum * g_sum
                         + (long long)b_sum * b_sum;
        printf("%.6lf", sum_sq - sq_sum / (double)n);
    } else {
        if(n <= 2) {
            printf("0.000000");
            return 0;
        }
        double answer = 1e18;
        for(int ai = 1; ai <= n - 2; ai++) {
            for(int bi = ai + 1; bi <= n - 1; bi++) {
                for(int ci = bi + 1; ci <= n; ci++) {
                    vector<int> S1, S2;

                    // 법선 벡터
                    Vec3 x = {r[bi] - r[ai], g[bi] - g[ai], b[bi] - b[ai]};
                    Vec3 y = {r[ci] - r[ai], g[ci] - g[ai], b[ci] - b[ai]};
                    Vec3 z = cross(x, y);

                    for(int i = 1; i <= n; i++) {
                        if(i == ai || i == bi || i == ci) {
                            continue;
                        }
                        Vec3 w = {r[i] - r[ai], g[i] - g[ai], b[i] - b[ai]};
                        if(inner(w, z) > 0) {
                            S1.push_back(i);
                        } else {
                            S2.push_back(i);
                        }
                    }

                    for(int al = 0; al < 2; al++) {
                        for(int bl = 0; bl < 2; bl++) {
                            for(int cl = 0; cl < 2; cl++) {
                                if(al == bl && bl == cl) continue;

                                vector<int> s1 = S1, s2 = S2;
                                if(al == 0) {
                                    s1.push_back(ai);
                                } else {
                                    s2.push_back(ai);
                                }
                                if(bl == 0) {
                                    s1.push_back(bi);
                                } else {
                                    s2.push_back(bi);
                                }
                                if(cl == 0) {
                                    s1.push_back(ci);
                                } else {
                                    s2.push_back(ci);
                                }

                                // 계산
                                long long sum_sq1 = 0, r_sum1 = 0, g_sum1 = 0, b_sum1 = 0;
                                long long sum_sq2 = 0, r_sum2 = 0, g_sum2 = 0, b_sum2 = 0;
                                int n1 = s1.size(), n2 = s2.size();

                                if(n1 == 0 || n2 == 0) {
                                    continue;
                                }

                                for(int i : s1) {
                                    sum_sq1 += r[i] * r[i] + g[i] * g[i] + b[i] * b[i];
                                    r_sum1 += r[i];
                                    g_sum1 += g[i];
                                    b_sum1 += b[i];
                                }
                                long long sq_sum1 = (long long)r_sum1 * r_sum1
                                                  + (long long)g_sum1 * g_sum1
                                                  + (long long)b_sum1 * b_sum1;
                                for(int i : s2) {
                                    sum_sq2 += r[i] * r[i] + g[i] * g[i] + b[i] * b[i];
                                    r_sum2 += r[i];
                                    g_sum2 += g[i];
                                    b_sum2 += b[i];
                                }
                                long long sq_sum2 = (long long)r_sum2 * r_sum2
                                                  + (long long)g_sum2 * g_sum2
                                                  + (long long)b_sum2 * b_sum2;
                                double temp = sum_sq1 + sum_sq2 - sq_sum1 / (double)n1 - sq_sum2 / (double)n2;
                                answer = min(answer, temp);
                            }
                        }
                    }
                }
            }
        }
        printf("%.6lf", answer);
    }

    return 0;
}