#include <iostream>

using namespace std;

int n;
int seq[80];

bool check(int i) {
    for(int j=1; j<=(i+1)/2; j++) {
        bool diff = false;
        for(int k=i; k>i-j; k--) {
            if(seq[k] != seq[k-j]) {
                diff = true;
                break;
            }
        }
        if(!diff) return false;
    }
    return true;
}

void backtracking(int i) {
    if(i == n) {
        for(int i=0; i<n; i++) cout << seq[i];
        exit(0);
    }
    for(int t=1; t<=3; t++) {
        seq[i] = t;
        if(check(i)) backtracking(i+1);
    }
}

int main() {
    cin >> n;
    backtracking(0);

    return 0;
}