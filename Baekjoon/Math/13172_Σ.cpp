#include <bits/stdc++.h>

#define F first
#define S second
#define B begin()
#define E end()
#define PB push_back
#define MP make_pair
#define REP(i, a, b) for (int i = a; i < b; i++)
#define endl "\n"
#define MOD 1000000007

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

ll recuesive_pow(ll a, ll b)
{
    if (b == 0)
        return 1;
    if (b % 2 == 0)
    {
        ll temp = recuesive_pow(a, b / 2);
        return temp * temp % MOD;
    }
    return a * recuesive_pow(a, b - 1) % MOD;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int m;
    ll n, s;
    ll ans = 0;

    cin >> m;
    REP(i, 0, m)
    {
        cin >> n >> s;
        ll inv = recuesive_pow(n, MOD - 2);
        ans = (ans + (s * inv % MOD)) % MOD;
    }
    cout << ans << endl;
}