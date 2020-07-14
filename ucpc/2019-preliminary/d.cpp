#include <bits/stdc++.h>

using namespace std;

struct Trie {
    Trie* go[26];
    int cnt;

    Trie() : cnt(0) {
        fill(go, go + 26, nullptr);
    }

    ~Trie() {
        for (int i = 0; i < 26; i++)
            if (go[i])
                delete go[i];
    }

    void insert(const char* key) {
        cnt++;

        if (*key == '\0')
            return;

        int next = *key - 'a';
        if (!go[next])
            go[next] = new Trie;
        go[next]->insert(key + 1);
    }
};

Trie *head;
char s[200001];  // sentence
int n;  // strlen(s)
int d[200000];  // dp memoization

int dp(int i) {
    if(i == n)
        return 1;

    if(d[i] != -1)
        return d[i];

    int sum = 0;
    Trie *now = head;
    for(int j=i; j<n && now->go[s[j]-'a']; j++) {
        now = now->go[s[j]-'a'];
        sum = ( sum + (long long)now->cnt * dp(j+1) ) % 1000000007;
    }
    return d[i] = sum;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(NULL);

    int N;
    cin >> N;

    head = new Trie;
    for(int i=0; i<N; i++) {
        char word[301];
        cin >> word;
        head->insert(word);
    }
    cin >> s;
    n = strlen(s);

    for(int i=0; i<n; i++)
        d[i] = -1;

    cout << dp(0);

    return 0;
}