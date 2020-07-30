#include <iostream>
#include <string>

using namespace std;

string t(int n) {
    if(n == 1) {
        return "#";
    } else if(n == 2) {
        return "##";
    } else {
        // p: n보다 작지 않은 가장 작은 2의 제곱수
        int p;
        for(p=4; p<n; p*=2);

        if(p == n) {
            string s;
            for(int i=0; i<n; i++) {
                s.push_back('#');
            }
            return s;
        } else {
            if(n <= p * 3 / 4) {
                string s = t(n - p / 4);
                s.resize(p);
                for(int i=p/2; i<p*3/4; i++) s[i] = '#';
                for(int i=p*3/4; i<p; i++) s[i] = '.';
                return s;
            } else {
                string s = t(p / 2) + t(n - p / 2);
                return s;
            }
        }
    }
}

int main() {
    int n;
    cin >> n;

    cout << t(n);
}