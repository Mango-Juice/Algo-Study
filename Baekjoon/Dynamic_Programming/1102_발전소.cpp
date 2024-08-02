#include <bits/stdc++.h>

#define F first
#define S second
#define B begin()
#define E end()
#define PB push_back
#define MP make_pair
#define REP(i, a, b) for (int i = a; i < b; i++)
#define endl "\n"
#define INF 10000

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

int n, p;
int arr[16][16];
int dp[1 << 16];

int dfs(int now) {
    if(__builtin_popcount(now) >= p) return 0;
    if(dp[now] >= 0) return dp[now];
    
    dp[now] = INF;
    REP(i, 0, n) {
        if((now & (1<<i)) == 0) continue;
        REP(j, 0, n) {
            if((now & (1<<j)) == 1) continue;
            dp[now] = min(dp[now], dfs(now | (1 << j)) + arr[i][j]);
        }
    }
    return dp[now];
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    cin >> n;
    REP(i, 0, n) REP(j, 0, n) cin >> arr[i][j];
    
    int now = 0;
    REP(i, -1, n) {
        char c = cin.get();
        if(c == 'Y') now |= (1 << i);
    }
    cin >> p;
    
    memset(dp, -1, sizeof(dp));
    int answer = dfs(now);
    cout << (answer == INF ? -1 : answer);
}