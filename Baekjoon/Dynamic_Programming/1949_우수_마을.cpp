#include <bits/stdc++.h>

#define F first
#define S second
#define B begin()
#define E end()
#define PB push_back
#define MP make_pair
#define REP(i, a, b) for (int i = a; i < b; i++)
#define endl "\n"

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

int n, a, b;
vi path[10001];
int value[10001] = { 0, };
int dp[10001][2] = { 0, };
bool visited[10001] = { false };

void getAnswer(int node) {
    visited[node] = true;
    dp[node][0] = value[node];
    dp[node][1] = 0;
    
    for(auto i: path[node]){
        if(visited[i]) continue;
        getAnswer(i);
        dp[node][0] += dp[i][1];
        dp[node][1] += max(dp[i][0], dp[i][1]);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n;
    
    REP(i, 0, n) cin >> value[i + 1];
    
    REP(i, 0, n - 1) {
        cin >> a >> b;
        path[a].PB(b);
        path[b].PB(a);
    }
    
    getAnswer(1);
    cout << max(dp[1][0], dp[1][1]) << endl;
}