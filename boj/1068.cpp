#include <iostream>
#include <vector>

using namespace std;

int parent[50];
vector<int> children[50];

int count_leaves(int this_node) {
    if(children[this_node].size() == 0)  // if leaf node
        return 1;

    int sum_leaves = 0;
    for(int child_node : children[this_node])
        sum_leaves += count_leaves(child_node);
    return sum_leaves;
}

int main() {
    int N, root, to_erase;
    cin >> N;  // <= 50
    for(int i=0; i<N; i++) {
        cin >> parent[i];
        if(parent[i] == -1)
            root = i;
    }
    cin >> to_erase;

    if(to_erase == root) {
        cout << 0;
        return 0;
    }

    parent[to_erase] = -1;  // erase the node

    for(int i=0; i<N; i++)
        if(parent[i] != -1)
            children[parent[i]].push_back(i);

    cout << count_leaves(root);
}