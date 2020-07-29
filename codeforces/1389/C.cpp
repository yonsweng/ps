#include <iostream>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        string s;
        cin >> s;

        int cnt[100] = {};
        for(int i=0; i<s.size(); i++) {
            int num = (s[i]-'0');
            cnt[num]++;
        }

        int max = 0;
        for(int i=0; i<10; i++) {
            max = std::max(max, cnt[i]);
            cnt[i] = 0;
        }

        for(int i=0; i<s.size()-1; i++) {
            int num = (s[i]-'0')*10 + s[i+1]-'0';
            cnt[num]++;
        }
        for(int i=0; i<100; i++) {
            if(i / 10 != i % 10)
                max = std::max(max, cnt[i] * 2);
        }

        cout << int(s.size()) - max << '\n';
    }
}