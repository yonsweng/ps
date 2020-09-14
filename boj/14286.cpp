#include <algorithm>
#include <string>
#include <queue>
#include <cstring>
#include <vector>
#include <iostream>
#define INF 987654321
#define MAX_A 501
using namespace std;
int S, E;
int n, z;
char x, y;
int level[MAX_A];
int work[MAX_A];
struct Edge {
    int v, cap, rev;
    Edge(int v, int cap, int rev) :v(v), cap(cap), rev(rev) {}
};    //간선 구조체 , 반대쪽에 연결 된 정점과 용량 역방향 간선의 위치를 가지고있다. 
vector<vector<Edge>> vt;
void addEdge(int s,int e,int c){
    vt[s].emplace_back(e, c, (int)vt[e].size());
    vt[e].emplace_back(s, c, (int)vt[s].size() - 1);
}    //벡터의 사이즈 만큼을 넣어주어 역방향 간선의 위치를 저장한다.

bool bfs(){
    memset(level, -1, sizeof(level));        //레벨 그래프 초기화
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
 
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int m;
    cin >> n >> m;
    vt.resize(MAX_A);
    for (int i = 0; i < m; i++){
        int a, b, c;
        cin >> a >> b >> c;
        addEdge(a, b, c);
    }
    cin >> S >> E;

    int res = 0;
    while (bfs()){    //레벨 그래프가 만들어 지는 경우에만 동작
        memset(work, 0, sizeof(work));
        while (1){
            int flow = dfs(S, INF);    //차단유량을 구하여
            if (!flow)break;    
            res += flow;    //차단유량이 1이상일 경우 maximum flow에 더해줌
        }
    }
    cout << res;
    return 0;
}