#include <iostream>

using namespace std;

int main(){

    int a,b;

    int n,w;

    int flag = 0;

    int count = 0;

    int aNum, bNum;

    cin >> a >> b >>n >> w;
    for (int i=1;i<n;i++){
        if (i*a + (n-i)*b == w){
            aNum = i;
            bNum = n-i;
            count++;
            flag = 1;
        }


    }

    if (!flag || count>=2) cout << "-1" << "\n";
    else {
        cout << aNum << " " << bNum << "\n";
    }

}