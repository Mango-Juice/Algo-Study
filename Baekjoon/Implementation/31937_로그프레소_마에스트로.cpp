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
    
    int n, m, k;
    int tmp, t, a, b;
    cin >> n >> m >> k;
    
    vector<bool> isInfected(n+1, false);
    REP(i, 0, k) {
        cin >> tmp;
        isInfected[tmp] = true;
    }
    
    vector<tuple<int, int, int>> v;
    REP(i, 0, m) {
        cin >> t >> a >> b;
        v.PB({t, a, b});
    }

    sort(v.B, v.E);
    REP(i, 1, n+1) {
        vector<bool> newInfected(n+1, false);
        newInfected[i] = true;
        bool answer = true;
        
        for(auto [ft, fa, fb]: v) {
            if(newInfected[fa]) newInfected[fb] = true;
        }
        
        REP(j, 1, n+1) {
            if(isInfected[j] != newInfected[j]) {
                answer = false;
                break;
            }
        }
        
        if(answer) {
            cout << i;
            return 0;
        }
    }
}