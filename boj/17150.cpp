#include <iostream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

struct Tile {
    int price;
    int height;
    int index;

    Tile() {}
    Tile(int price, int height, int index) : price(price), height(height), index(index) {}

    bool operator<(const Tile &a) const {
        if(price < a.price) return true;
        else if(price == a.price && height < a.height) return true;
        else return false;
    }
};

vector<Tile> back, front;
vector<int> back_order, front_order;

int main()
{
	// freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false), cin.tie(NULL);

    int n;
    cin >> n;

    back.resize(n), front.resize(n);

    for(int i=0; i<n; i++)
        cin >> back[i].price;
    for(int i=0; i<n; i++)
        cin >> back[i].height;
    for(int i=0; i<n; i++)
        cin >> front[i].price;
    for(int i=0; i<n; i++)
        cin >> front[i].height;
    for(int i=0; i<n; i++)
        back[i].index = front[i].index = i;

    sort(back.begin(), back.end());
    sort(front.begin(), front.end());

    bool impossible = false;
    int back_l = 0, back_r, front_l = 0, front_r;
    back_r = lower_bound(back.begin() + back_l, back.end(), Tile(back[back_l].price+1, 0, 0)) - back.begin();
    front_r = lower_bound(front.begin() + front_l, front.end(), Tile(front[front_l].price+1, 0, 0)) - front.begin();

    multiset<Tile> back_set, front_set;
    for(int i=back_l; i<back_r; i++)
        back_set.insert(back[i]);
    for(int i=front_l; i<front_r; i++)
        front_set.insert(front[i]);

    while(back_l < n && front_l < n) {
        // back is shorter
        if(back_set.size() <= front_set.size()) {
            Tile pivot = *back_set.begin();
            back_set.erase(back_set.begin());
            back_order.push_back(pivot.index);

            //multiset<Tile>::iterator lb = lower_bound(front_set.begin(), front_set.end(), pivot, comp_height);
            multiset<Tile>::iterator lb = front_set.lower_bound(Tile(front_set.begin()->price, pivot.height, 0));

            if(lb-- == front_set.begin()) {  // not found
                impossible = true;
                break;
            }

            front_order.push_back(lb->index);
            front_set.erase(lb);
        }
        // front is shorter
        else {
            Tile pivot = *front_set.begin();
            front_set.erase(front_set.begin());
            front_order.push_back(pivot.index);

            //multiset<Tile>::iterator lb = upper_bound(back_set.begin(), back_set.end(), pivot, comp_height);
            multiset<Tile>::iterator lb = back_set.upper_bound(Tile(back_set.begin()->price, pivot.height, 0));
            
            if(lb == back_set.end()) {  // not found
                impossible = true;
                break;
            }

            back_order.push_back(lb->index);
            back_set.erase(lb);
        }

        if(back_set.empty()) {
            back_l = back_r;
            back_r = lower_bound(back.begin() + back_l, back.end(), Tile(back[back_l].price+1, 0, 0)) - back.begin();

            for(int i=back_l; i<back_r; i++)
                back_set.insert(back[i]);
        }

        if(front_set.empty()) {
            front_l = front_r;
            front_r = lower_bound(front.begin() + front_l, front.end(), Tile(front[front_l].price+1, 0, 0)) - front.begin();

            for(int i=front_l; i<front_r; i++)
                front_set.insert(front[i]);
        }
    }

    if(impossible) cout << "impossible";
    else {
        for(int i=0; i<n; i++)
            cout << back_order[i] + 1 << ' ';
        cout << '\n';
        for(int i=0; i<n; i++)
            cout << front_order[i] + 1 << ' ';
    }

	return 0;
}