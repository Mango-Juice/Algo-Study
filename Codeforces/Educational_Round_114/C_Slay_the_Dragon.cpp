// https://codeforces.com/contest/1574/problem/C

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)
 
#include <iostream>
#include <algorithm>
 
using namespace std;
typedef long long ll;
 
ll players[200001];
ll sum = 0;
 
ll maximum(ll a, ll b) {
    return a > b ? a : b;
}
 
ll minimum(ll a, ll b) {
    return a < b ? a : b;
}
 
int main() {
    int n, m;
    FAST_IO;
 
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> players[i];
        sum += players[i];
    }
 
    sort(players, players + n);
 
    cin >> m;
    for (int i = 0; i < m; i++) {
        ll x, y;
        cin >> x >> y;
 
        int left = 0, right = n - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (players[mid] > x) right = mid;
            else left = mid + 1;
        }
 
        if (right > 0 && players[right] > x) right--;
        ll val1 = maximum(0, x - players[right]) + maximum(0, y - sum + players[right]);
        ll val2 = right < n - 1 ? maximum(0, x - players[right + 1]) + maximum(0, y - sum + players[right + 1]) : val1;
        cout << minimum(val1, val2) << '\n';
    }
 
    return 0;
}