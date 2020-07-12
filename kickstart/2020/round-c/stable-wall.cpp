#include <iostream>
#include <set>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int case_num=1; case_num<=T; case_num++) {
        int R, C, cnt[26] = {};
        char w[30][30], ans[27] = {};
        set<int> lets, dep[26];
        bool chk[26] = {};

        cin >> R >> C;
        for(int i=0; i<R; i++)
            for(int j=0; j<C; j++) {
                cin >> w[i][j];
                lets.insert(w[i][j]-'A');
            }

        for(int i=0; i<R; i++)
            for(int j=0; j<C; j++)
                if(i+1 < R && w[i][j] != w[i+1][j])
                    dep[w[i+1][j]-'A'].insert(w[i][j]-'A');

        for(int from : lets)
            for(int to : dep[from])
                cnt[to]++;

        for(int i=0; i<lets.size(); i++)
            for(int let : lets)
                if(cnt[let] == 0 && !chk[let]) {
                    ans[i] = let + 'A';
                    for(int to : dep[let]) cnt[to]--;
                    chk[let] = true;
                    break;
                }

        if(ans[int(lets.size())-1])
            cout << "Case #" << case_num << ": " << ans << '\n';
        else
            cout << "Case #" << case_num << ": " << -1 << '\n';
    }
    return 0;
}