#include <iostream>

using namespace std;

struct S {
    int a, b;
};

int main() {
    S *s;
    s = new S{1, 3};
    cout << s->a << s->b;
}