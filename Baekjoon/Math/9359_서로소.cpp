#include <bits/stdc++.h>

#define F first
#define S second
#define B begin()
#define E end()
#define PB push_back
#define MP make_pair
#define REP(i, a, b) for (ll i = a; i < b; i++)
#define endl "\n"

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

ll t, a, b, n;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    cin >> t;
    REP(i, 0, t) {
        ll answer = 0;
        cin >> a >> b >> n;
        
        vector<ll> d;
        for(ll j = 2; j * j <= n; j++) {
            if (n % j == 0) {
                d.PB(j);
                while (n % j == 0) {
                    n /= j;
                }
            }
        }
        if(n > 1) d.PB(n);
        
        REP(j, 1, (1 << d.size())) {
            ll count = 0;
            ll target = 1;
            
            REP(k, 0, d.size()) {
                if(j & (1 << k)) {
                    count++;
                    target *= d[k];
                }
            }
            
            ll result = (b / target) - ((a - 1) / target);
            if(count & 1) answer += result;
            else answer -= result;
        }
        
        cout << "Case #" << i + 1 << ": " << b - a + 1 - answer << endl;
    }
}