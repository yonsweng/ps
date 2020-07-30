#include <vector>
#include <iostream>

using namespace std;

struct Node {
    int element;
    vector<Node *> children;
};

int main() {
    Node *head = new Node;
    head->element = 1;

    Node *new1 = new Node;
    new1->element = 2;

    Node *new2 = new Node;
    new2->element = 3;

    head->children.push_back(new1);
    head->children.push_back(new2);

    cout << head->children[0]->element;
}