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

int n, a, b, c;
vector<pi> vec;

vi lis;

bool comp(int a, int b){
    return a >= b;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    cin >> n;
    REP(i, 0, n) {
        cin >> a >> b >> c;
        vec.PB({b, -1 * c});
    }
    
    sort(vec.B, vec.E);
    vec.erase(unique(vec.B, vec.E), vec.E);
    for(auto [f, b] : vec) {
        b *= -1;
        auto target = lower_bound(lis.B, lis.E, b, comp);
        if(target == lis.E) {
            lis.PB(b);
        } else {
            *target = b;
        }
    }
    
    cout << lis.size();
}