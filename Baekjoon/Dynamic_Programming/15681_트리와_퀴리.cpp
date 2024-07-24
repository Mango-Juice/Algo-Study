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

int n, r, q, a, b;
vi path[100001];
int dp[100001] = { 0, };

int getAnswer(int node) {
    dp[node] = 1;
    for(auto i: path[node])
        if(dp[i] == 0)
            dp[node] += getAnswer(i);
    return dp[node];
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n >> r >> q;
    
    REP(i, 0, n - 1) {
        cin >> a >> b;
        path[a].PB(b);
        path[b].PB(a);
    }
    
    getAnswer(r);
    
    REP(i, 0, q) {
        cin >> a;
        cout << dp[a] << endl;
    }
}