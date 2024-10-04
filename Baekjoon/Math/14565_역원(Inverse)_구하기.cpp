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

tuple<ll, ll, ll> extendedGcd(ll a, ll b) {
    if (b == 0) return {1, 0, a};
    ll x, y, g;
    tie(x, y, g) = extendedGcd(b, a % b);
    return {y, x - (a / b) * y, g};
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    ll n, a;
    cin >> n >> a;
    
    ll addRev = n - a;
    ll x, y, gcd;
    tie(x, y, gcd) = extendedGcd(a, n);
    if (x < 0) x += n;
    
    cout << addRev << " " << (gcd > 1 ? -1 : x);
}
