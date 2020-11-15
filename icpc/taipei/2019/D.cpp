#include <iostream>
#include <vector>

using namespace std;

int main() {
    freopen("input/1.in", "r", stdin);

    vector<string> words;

    while(true) {
        string word;
        cin >> word;

        if(word == "") {
            break;
        }

        if(word == "bubble" || word == "tapioka") {
            continue;
        } else {
            words.push_back(word);
        }
    }

    if(words.empty()) {
        cout << "nothing";
        return 0;
    }
    for(auto word : words) {
        cout << word << ' ';
    }

    return 0;
}