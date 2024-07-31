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

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    int m, n, tmp;
    int arr[1001][1001] = { 0, };
    int ans = 0;
    
    cin >> m >> n;
    REP(i, 1, m + 1) {
        REP(j, 1, n + 1){
            cin >> tmp;
            if(tmp == 0) {
                arr[i][j] = min(min(arr[i - 1][j], arr[i][j - 1]), arr[i - 1][j - 1]) + 1;
                ans = max(ans, arr[i][j]);
            }
        }
    }
    
    cout << ans;
}