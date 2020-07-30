#include <iostream>
#include <string>

using namespace std;

struct Node {
    int left_child;
    int right_child;
} node[26];  // node[0]: A, node[1]: B, ...
string pre, in, post;

void preorder(int this_node) {
    if(this_node == -1) return;
    pre.push_back(this_node+'A');
    preorder(node[this_node].left_child);
    preorder(node[this_node].right_child);
}

void inorder(int this_node) {
    if(this_node == -1) return;
    inorder(node[this_node].left_child);
    in.push_back(this_node+'A');
    inorder(node[this_node].right_child);
}

void postorder(int this_node) {
    if(this_node == -1) return;
    postorder(node[this_node].left_child);
    postorder(node[this_node].right_child);
    post.push_back(this_node+'A');
}

int main() {
    int N;
    cin >> N;
    for(int i=0; i<N; i++) {
        char parent, left_child, right_child;
        cin >> parent >> left_child >> right_child;
        node[parent-'A'].left_child = left_child != '.' ? left_child-'A' : -1;
        node[parent-'A'].right_child = right_child != '.' ? right_child-'A' : -1;
    }

    preorder(0);
    inorder(0);
    postorder(0);

    cout << pre << '\n';
    cout << in << '\n';
    cout << post;
}