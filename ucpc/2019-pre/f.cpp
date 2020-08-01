#include <bits/stdc++.h>

using namespace std;

double d[7][7][999];

int calc_prize(int a, int b, int c) {
    if(a == b && b == c) {
        return 10000 + a * 1000;
    } else if(a == b) {
        return 1000 + a * 100;
    } else if(b == c) {
        return 1000 + b * 100;
    } else if(c == a) {
        return 1000 + c * 100;
    } else if(a > b && a > c) {
        return a * 100;
    } else if(b > c) {
        return b * 100;
    } else {
        return c * 100;
    }
}

// a: second prev, b: prev, n: remaining
double f(int a, int b, int n) {
    if(n == 0) {
        return 0.;
    }

    if(d[a][b][n] != -1) {
        return d[a][b][n];
    }

    double sum = 0.;
    for(int c=1; c<=6; c++) {
        double present = calc_prize(a, b, c);
        double future = f(b, c, n-1);
        sum += max(present, future);
    }

    return d[a][b][n] = sum / 6.;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(NULL);

    // initialize
    for(int a=1; a<=6; a++) {
        for(int b=1; b<=6; b++) {
            for(int n=1; n<=998; n++) {
                d[a][b][n] = -1;
            }
        }
    }

    int N;
    cin >> N;

    double sum = 0;
    for(int a=1; a<=6; a++) {
        for(int b=1; b<=6; b++) {
            sum += f(a, b, N-2);
        }
    }

    cout << fixed;
    cout.precision(6);
    cout << sum / 36.;
}