#include <string>
#include <vector>
#include <cmath>
#include <cstring>
#include <iostream>
#include <cstdlib>

#define MAX 360000

using namespace std;

int time2sec(string time) {
    int hour = (time[0] - '0') * 10 + (time[1] - '0');
    int min = (time[3] - '0') * 10 + (time[4] - '0');
    int sec = (time[6] - '0') * 10 + (time[7] - '0');
    return hour * 3600 + min * 60 + sec;
}

string sec2time(int sec) {
    int hour = sec / 3600;
    int min = (sec % 3600) / 60;
    sec = sec % 60;
    string time;
    time.resize(8);
    time[0] = (hour / 10) + '0';
    time[1] = (hour % 10) + '0';
    time[2] = ':';
    time[3] = (min / 10) + '0';
    time[4] = (min % 10) + '0';
    time[5] = ':';
    time[6] = (sec / 10) + '0';
    time[7] = (sec % 10) + '0';
    return time;
}

class Segtree {
private:
	int n_nodes;
	long long *seg_tree, *prop_tree;

	long long init(long long d[], int i, int l, int r) {
		if(l == r) return seg_tree[i] = d[l];

		int mid = (l + r) / 2;
		return seg_tree[i] = init(d, i*2, l, mid) + init(d, i*2+1, mid+1, r);
	}

public:
	Segtree(long long d[], int n) {
		n_nodes = (1 << (int)(ceil(log2(n)) + 1)) - 1;
		seg_tree = (long long *)malloc((n_nodes + 1) * sizeof(long long));
		prop_tree = (long long *)malloc((n_nodes + 1) * sizeof(long long));
		memset(seg_tree, 0, sizeof(long long) * (n_nodes + 1));
		memset(prop_tree, 0, sizeof(long long) * (n_nodes + 1));

		init(d, 1, 0, n-1);
	}

	~Segtree() {
		free(seg_tree);
		free(prop_tree);
	}

	long long add(int ql, int qr, long long val, int i, int l, int r) {
		if(qr < l || r < ql) {
			if(l < r) {
				prop_tree[i*2] += prop_tree[i];
				prop_tree[i*2+1] += prop_tree[i];
			}
			seg_tree[i] += prop_tree[i] * (r - l + 1);
			prop_tree[i] = 0;

			return seg_tree[i];
		}
		else if(ql <= l && r <= qr) {
			if(l < r) {
				prop_tree[i*2] += prop_tree[i] + val;
				prop_tree[i*2+1] += prop_tree[i] + val;
			}
			seg_tree[i] += (prop_tree[i] + val) * (r - l + 1);
			prop_tree[i] = 0;

			return seg_tree[i];
		}
		else {
			prop_tree[i*2] += prop_tree[i];
			prop_tree[i*2+1] += prop_tree[i];
			prop_tree[i] = 0;

			int mid = (l + r) / 2;
			return seg_tree[i] = add(ql, qr, val, i*2, l, mid) + add(ql, qr, val, i*2+1, mid+1, r);
		}
	}

	long long get_sum(int ql, int qr, int i, int l, int r) {
		if(qr < l || r < ql) {
			if(l < r) {
				prop_tree[i*2] += prop_tree[i];
				prop_tree[i*2+1] += prop_tree[i];
			}
			seg_tree[i] += prop_tree[i] * (r - l + 1);
			prop_tree[i] = 0;

			return 0;
		}
		else if(ql <= l && r <= qr) {
			if(l < r) {
				prop_tree[i*2] += prop_tree[i];
				prop_tree[i*2+1] += prop_tree[i];
			}
			seg_tree[i] += prop_tree[i] * (r - l + 1);
			prop_tree[i] = 0;

			return seg_tree[i];
		}
		else {
			prop_tree[i*2] += prop_tree[i];
			prop_tree[i*2+1] += prop_tree[i];
			prop_tree[i] = 0;

			int mid = (l + r) / 2;
			long long sum = get_sum(ql, qr, i*2, l, mid) + get_sum(ql, qr, i*2+1, mid+1, r);

			seg_tree[i] = seg_tree[i*2] + seg_tree[i*2+1];

			return sum;
		}
	}

	void print_seg() {
        cout << n_nodes << '\n';
		for(int i=1; i<=n_nodes; i++)
			cout << seg_tree[i] << ' ';
		cout << '\n';
	}

	void print_prop() {
		for(int i=1; i<=n_nodes; i++)
			cout << prop_tree[i] << ' ';
		cout << '\n';
	}
};

string solution(string play_time, string adv_time, vector<string> logs) {
    string answer = "";
    
    int len_play = time2sec(play_time);
    
    long long *d = (long long *)malloc(len_play * sizeof(long long));
    memset(d, 0, sizeof(long long) * len_play);
    Segtree st = Segtree(d, len_play);
    
    for(string log : logs) {
        string start = log.substr(0, 8);
        string end = log.substr(9, 8);
        int start_sec = time2sec(start);
        int end_sec = time2sec(end) - 1;
        
        st.add(start_sec, end_sec, 1, 1, 0, len_play-1);
    }
    
    // st.print_seg();
    
    int len_adv = time2sec(adv_time);
    int max_answer = time2sec(play_time) - len_adv;
    int sec_answer = 0;
    int fastest = 0;
    for(int start_sec = 0; start_sec <= max_answer; start_sec++) {
        // cout << st.get_sum(start_sec, start_sec + len_adv - 1, 1, 0, len_play-1) << '\n';
        int tmp =  st.get_sum(start_sec, start_sec + len_adv - 1, 1, 0, len_play-1);
        if(tmp > sec_answer) {
            sec_answer = tmp;
            fastest = start_sec;
        }
    }
    answer = sec2time(fastest);
    return answer;
}

int main() {
    vector<string> logs = {"01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"};

    cout << solution("02:03:55", "00:14:15", logs);
}