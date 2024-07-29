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
    
    int n, m, tmp;
    set<int> s;
    cin >> n >> m;
    
    REP(i, 1, n + 1) s.insert(i);
    REP(i, 0, m) {
        cin >> tmp;
        s.erase(tmp);
    }
    
    int last = -1, result = 0;
    for(int number: s) {
        if (last == -1) result += 7;
        else result += min(7, (number - last) * 2);
        last = number;
    }
    
    cout << result;
}