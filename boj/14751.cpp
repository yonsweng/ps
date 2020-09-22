#include <bits/stdc++.h>

#define FOR(i, n) for(int i = 1; i <= (n); i++)
#define INF 1e18

using namespace std;

int maxY, minY;

struct Line {
    int num;
    int upperX, lowerX;
    Line() {}
    Line(double upperX, double lowerX) : upperX(upperX), lowerX(lowerX) {}
    bool operator<(Line &l) {
        if(upperX - lowerX > l.upperX - l.lowerX)
            return true;
        else if(upperX - lowerX == l.upperX - l.lowerX && lowerX < l.lowerX)
            return true;
        else
            return false;
    }
};

// -1 if a < b, 0 if a == b, else 1.
// int comp(double a, double b) {
//     if(abs(a - b) < 1e-9)
//         return 0;
//     else if(a < b)
//         return -1;
//     else
//         return 1;
// }

double inter_y(Line &l1, Line &l2) {
    return (l2.lowerX - l1.lowerX) * (maxY - minY) / double(l1.upperX - l1.lowerX - l2.upperX + l2.lowerX) + minY;
}

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int n, m;
    vector<Line> lines;

    cin >> maxY >> minY;
    cin >> n;

    lines.resize(n + 1);

    FOR(i, n) {
        int upperX, lowerX;
        cin >> upperX >> lowerX;

        lines[i].num = i;
        lines[i].upperX = upperX;
        lines[i].lowerX = lowerX;
    }

    sort(lines.begin() + 1, lines.end());  // slope decreasing

    stack<pair<int, double>> st;
    st.emplace(1, minY);
    for(int i = 2; i <= n; i++) {
        while(!st.empty()) {
            double interY = inter_y(lines[st.top().first], lines[i]);
            if(interY >= maxY)  // out of range
                break;
            if(interY > st.top().second) {
                st.emplace(i, interY);
                break;
            }
            st.pop();
        }
        if(st.empty())
            st.emplace(i, minY);
    }

    vector<pair<double, Line>> ch;
    while(!st.empty()) {
        ch.emplace_back(st.top().second, lines[st.top().first]);
        st.pop();
    }
    reverse(ch.begin(), ch.end());

    cin >> m;
    FOR(i, m) {
        double query;
        cin >> query;

        // binary search
        int lo = 0, hi = ch.size(), answer = 0;
        while(lo < hi) {
            int mid = (lo + hi) / 2;
            if(query >= ch[mid].first) {
                answer = ch[mid].second.num;
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        cout << answer << '\n';
    }
}