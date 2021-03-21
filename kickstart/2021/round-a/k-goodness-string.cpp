#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int x=1; x<=T; x++) {
        int N, K;
        char S[200001];
        cin >> N >> K;
        cin >> S;

        int G = 0;
        for(int i=0; i<N/2; i++) {
            if(S[i] != S[N-i-1]) {
                G++;
            }
        }

        int y = abs(G - K);

        cout << "Case #" << x << ": " << y << '\n';
    }
}