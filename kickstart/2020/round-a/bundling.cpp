#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
char s[2000001];
int K;

struct Trie {
    // 현재 노드에서 해당 문자를 받으면 가는 노드
    Trie* go[26];
    // 현재 노드에서 해당 문자의 go 목적지가 없을 때 가는 노드
    Trie* fail;
    // 현재 노드에 도달하면 찾는 문자열 집합: 이 문제에서는 존재성만 따지면 됨
    bool output;
    int cnt, depth;

    Trie() : cnt(0) {
        fill(go, go + 26, nullptr);
        output = false;
    }
    ~Trie() {
        for (int i = 0; i < 26; i++)
            if (go[i]) delete go[i];
    }
    void insert(const char* key, int depth) {
        cnt++;
        this->depth = depth;
        if (*key == '\0') {
            output = true;
            return;
        }
        int next = *key - 'A';
        if (!go[next]) {
            go[next] = new Trie;
        }
        go[next]->insert(key + 1, depth + 1);
    }
};

long long get_prefix_len(Trie *now) {
    long long ret = 0;
    for(int i=0; i<26; i++) {
        if(now->go[i] && now->go[i]->cnt >= K)
            ret += get_prefix_len(now->go[i]);
    }
    return ret + now->cnt / K;
}

int main() {
//    freopen("1.in", "r", stdin);

    int T;
    cin >> T;
    for(int case_num=1; case_num<=T; case_num++) {
        int N;
        Trie *root = new Trie;

        cin >> N >> K;
        for(int i=0; i<N; i++) {
            cin >> s;
            root->insert(s, 0);
        }

        long long sum = 0;
        for(int i=0; i<26; i++) {
            if(root->go[i]) {
                sum += get_prefix_len(root->go[i]);
            }
        }

        cout << "Case #" << case_num << ": " << sum << '\n';

        delete root;
    }

    return 0;
}