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
    
    ll l, tmp; int n, k;
    int count = 0;
    queue<ll> q;
    unordered_map<ll, int> visited;
    
    cin >> l >> n >> k;
    
    REP(i, 0, n) {
        cin >> tmp;
        q.push(tmp);
        visited[tmp] = 0;
        count++;
    }
    
    REP(i, 0, k) {
        ll target = q.front();
        q.pop();
        cout << visited[target] << endl;
        
        if (count < k && target > 0 && visited.find(target - 1) == visited.E) {
            q.push(target - 1);
            visited[target - 1] = visited[target] + 1;
            count++;
        }
        
        if (count < k && target < l && visited.find(target + 1) == visited.E) {
            q.push(target + 1);
            visited[target + 1] = visited[target] + 1;
            count++;
        }
    }
}