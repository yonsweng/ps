#include <iostream>

using namespace std;

bool isYoon(int year) {
    if(year % 4 == 0 && (year % 100 != 0 || year % 400 == 0))
        return true;
    else
        return false;
}

int main() {
    int year;
    cin >> year;

    if(isYoon(year)) cout << 1;
    else cout << 0;

    return 0;
}