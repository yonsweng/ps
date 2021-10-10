// import bisect
// from sys import stdin


// def read_input():
//     n = int(stdin.readline())
//     a = list(map(int, stdin.readline().split()))
//     return n, a


// def solve(n, a):
//     s = sum(a)

//     if s * 2 % n != 0:
//         return 0

//     answer = 0
//     a.sort()
//     for i, ai in enumerate(a[:-1]):
//         aj = s * 2 // n - ai
//         answer += bisect.bisect_right(a[i+1:], aj) - bisect.bisect_left(a[i+1:], aj)
//     return answer


// def main():
//     t = int(stdin.readline())
//     for _ in range(t):
//         input = read_input()
//         answer = solve(*input)
//         print(answer)


// if __name__ == '__main__':
//     main()
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for(int i=0; i<n; i++) cin >> a[i];

        long long s = 0;
        for(int i=0; i<n; i++) s += a[i];

        if(s * 2 % n != 0) {
            cout << "0\n";
            continue;
        }

        long long answer = 0;
        sort(a.begin(), a.end());
        for(int i=0; i<n-1; i++) {
            int aj = s * 2 / n - a[i];
            int ub = upper_bound(a.begin() + i + 1, a.end(), aj) - a.begin();
            int lb = lower_bound(a.begin() + i + 1, a.end(), aj) - a.begin();
            answer += ub - lb;
        }

        cout << answer << '\n';
    }
}