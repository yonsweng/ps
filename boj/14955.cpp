#include <bits/stdc++.h>

#define INF 987654321
#define MAX_A 101

using namespace std;

struct OriEdge {
    int u, v, w;

    OriEdge(int u, int v, int w) : u(u), v(v), w(w) {}

    bool operator<(OriEdge &e) const {
        return w < e.w;
    }
};

struct Edge {
    int v, cap, rev;
    Edge(int v, int cap, int rev) :v(v), cap(cap), rev(rev) {}
};

int n, m;
vector<OriEdge> edges;

vector<vector<Edge>> vt;
int S, E;
int level[MAX_A];
int work[MAX_A];

void add_edge(vector<vector<Edge>> &vt, int s, int e, int c) {
    vt[s].emplace_back(e, c, (int)vt[e].size());
    vt[e].emplace_back(s, c, (int)vt[s].size() - 1);
}

bool bfs(){
    fill_n(level, MAX_A, -1);
    memset(level, -1, sizeof(int)*MAX_A);        //레벨 그래프 초기화
    queue<int> qu;
    level[S] = 0;
    qu.push(S);        //S는 소스를 의미한다.
    while (qu.size()){
        int here = qu.front();
        qu.pop();
        for (auto i : vt[here]) {
            int there = i.v;
            int cap = i.cap;
            if (level[there] == -1 && cap > 0) {    //레벨이 아직 정해지지 않았고 잔여용량이 0이상
                level[there] = level[here] + 1;    //현재의 레벨값+1을 할당해준다.
                qu.push(there);
            }
        }
    }
    return level[E] != -1;    //E는 싱크를 의미한다. 싱크의 레벨이 할당이 안된 경우 0을 리턴
}

int dfs(int here, int crtcap) {
    if (here == E)return crtcap;        //싱크일 경우 현재 흐르는 유량을 return 
    for (int &i = work[here]; i < vt[here].size(); i++) {    //work 배열에는 다음 탐색 위치가 저장되어 있다.
        int there = vt[here][i].v;
        int cap = vt[here][i].cap;
        if (level[here] + 1 == level[there] && cap>0) {    //레벨 그래프가 1만큼 크고 잔여 용량이 0 이상인 간선
            int c= dfs(there, min(crtcap, cap));        //dfs로 다음 위치 탐색
            if (c> 0) {        //싱크까지 도달하여 흐르는 차단유량이 0 이상일 경우 
                vt[here][i].cap -= c;    //현재 용량에서 차단 유량만큼을 빼줌
                vt[there][vt[here][i].rev].cap += c;    //역방향 간선에 c만큼 용량을 추가해줌
                return c;
            }
        }
    }
    return 0;
}

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    cin >> n >> m;
    for(int i=0; i<m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.emplace_back(u, v, w);
    }
    sort(edges.begin(), edges.end());

    int answer = 0;
    vt.resize(MAX_A);

    for(int i=0; i<int(edges.size()); i++) {
        // Make a graph using the edges whose weights are smaller than edges[i].
        for(int j=0; j<=n; j++) vt[j].clear();
        for(int j=0; j<i; j++) {
            if(edges[j].w < edges[i].w) {
                add_edge(vt, edges[j].u, edges[j].v, 1);
            }
        }

        // Minimum cut
        fill_n(level, MAX_A, 0);
        fill_n(work, MAX_A, 0);
        S = edges[i].u, E = edges[i].v;
        int res = 0;
        while (bfs()){    //레벨 그래프가 만들어 지는 경우에만 동작
            fill_n(work, MAX_A, 0);
            // memset(work, 0, sizeof(int)*MAX_A);
            while (1){
                int flow = dfs(S, INF);    //차단유량을 구하여
                if (!flow)break;    
                res += flow;    //차단유량이 1이상일 경우 maximum flow에 더해줌
            }
        }
        answer += res;
    }

    cout << answer;
    return 0;
}