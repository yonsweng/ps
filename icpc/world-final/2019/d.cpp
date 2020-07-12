#include <iostream>
#include <vector>

using namespace std;

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int n;
    cin >> n;
    vector<pair<char, int>> marker(n+1);
    for(int j=1; j<=n; j++)
        cin >> marker[j].first >> marker[j].second;

    // calc minimum
    vector<int> min_acc(1e6+1, 1e6+1);
    vector<int> acc(1e6+1, 0);
    for(int j=1; j<=n; j++) {
        int i = marker[j].second;
        if(marker[j].first == 's')
            ++acc[i];
        else
            min_acc[i] = min(min_acc[i], --acc[i]);
    }

    // find minimum
    int overlays = 0;
    for(int i=1; i<=1e6; i++) {
        if(acc[i] == 0 && min_acc[i] == 0)
            overlays++;
    }

    int max_overlays = overlays, cut_j = 1;
    vector<int> acc2(1e6+1, 0);
    for(int j=1; j<=n; j++) {
        int i = marker[j].second;
        if(acc[i] != 0) continue;
        if(marker[j].first == 's') {
            if(acc2[i]++ == min_acc[i])
                overlays--;
        } else if(--acc2[i] == min_acc[i]) {
            if(++overlays > max_overlays) {
                max_overlays = overlays;
                cut_j = j % n + 1;
            }
        }
    }

    cout << cut_j << ' ' << max_overlays;

    return 0;
}