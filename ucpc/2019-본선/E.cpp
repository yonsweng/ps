#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <string>
#include <iostream>

using namespace std;

string loc[100];
int x[100], y[100];
string oil[3];
int p[3];

int main() {
    freopen("1.in", "r", stdin);

    int a, b, c, n;
    scanf("%d %d %d", &a, &b, &c);
    scanf("%d", &n);

    char line[101];
    fgets(line, 100, stdin);  // empty
    for(int i=0; i<n; i++) {
        fgets(line, 100, stdin);
        int split_point = 0, space_cnt = 0;
        for(int j=strlen(line)-1; j>=0; j--) {
            if(line[j] == ' ') {
                space_cnt++;
                if(space_cnt == 2) {
                    split_point = j;
                    break;
                }
            }
        }
        sscanf(line + split_point, "%d %d", &x[i], &y[i]);
        line[split_point] = 0;
        for(int j=0; j<strlen(line); j++) {
            loc[i].push_back(line[j]);
        }
    }

    // 주유소
    for(int i=0; i<3; i++) {
        fgets(line, 100, stdin);
        int split_point = 0, space_cnt = 0;
        for(int j=strlen(line)-1; j>=0; j--) {
            if(line[j] == ' ') {
                space_cnt++;
                if(space_cnt == 1) {
                    split_point = j;
                    break;
                }
            }
        }
        sscanf(line + split_point, "%d", &p[i]);
        line[split_point] = 0;
        for(int j=0; j<strlen(line); j++) {
            oil[i].push_back(line[j]);
        }
    }

    for(int i=)

    int k;
    cin >> k;
    for(int i=0; i<k; i++) {
        string cmd;
        getline(cin, cmd);
        cout << cmd << endl;
    }
}