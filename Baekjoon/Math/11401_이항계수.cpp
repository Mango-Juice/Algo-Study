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

int fac[4000001] = {
    1,
};

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

ll factorial(int n)
{
    if (fac[n] != 0)
        return fac[n];
    return fac[n] = n * factorial(n - 1) % MOD;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, k;
    cin >> n >> k;

    ll fac_n = factorial(n);
    ll result1 = recuesive_pow(fac[k], MOD - 2);
    ll result2 = recuesive_pow(fac[n - k], MOD - 2);

    ll temp = fac_n * result1 % MOD;
    cout << temp * result2 % MOD << endl;
}