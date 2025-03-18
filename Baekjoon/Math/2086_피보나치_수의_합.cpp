#include <bits/stdc++.h>

#define F first
#define S second
#define B begin()
#define E end()
#define PB push_back
#define MP make_pair
#define REP(i, a, b) for (int i = a; i < b; i++)
#define endl "\n"
#define MOD 1000000000

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

void matrix_mul(ll a[2][2], ll b[2][2], ll (*result)[2])
{
    REP(i, 0, 2)
    {
        REP(j, 0, 2)
        {
            REP(k, 0, 2)
            {
                result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % MOD;
            }
        }
    }
}

void matrix_pow(ll a[2][2], ll n, ll (*result)[2])
{
    if (n == 1)
    {
        result[0][0] = a[0][0];
        result[0][1] = a[0][1];
        result[1][0] = a[1][0];
        result[1][1] = a[1][1];
        return;
    }

    ll temp[2][2] = {0};
    if (n % 2 == 0)
    {
        matrix_pow(a, n / 2, temp);
        matrix_mul(temp, temp, result);
    }
    else
    {
        matrix_pow(a, n - 1, temp);
        matrix_mul(temp, a, result);
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    ll a, b;
    cin >> a >> b;

    if (b == 1)
    {
        cout << 1 << endl;
        return 0;
    }

    ll start[2][2] = {{1, 1}, {1, 0}};
    ll result[2][2] = {0};
    matrix_pow(start, b - 1, result);
    ll total_sum = (result[0][0] + result[0][1] + result[1][0] + result[1][1] - 1) % MOD;

    ll start_sum = 0;
    if (a <= 2)
    {
        start_sum = a - 1;
    }
    else
    {
        result[0][0] = result[0][1] = result[1][0] = result[1][1] = 0;
        matrix_pow(start, a - 2, result);
        start_sum = (result[0][0] + result[0][1] + result[1][0] + result[1][1] - 1) % MOD;
    }

    cout << (total_sum - start_sum + MOD) % MOD << endl;
}