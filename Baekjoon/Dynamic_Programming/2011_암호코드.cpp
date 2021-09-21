// https://www.acmicpc.net/problem/2011

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
typedef long long ll;
const int MOD = 1000000;

ll dp[5001] = { 0 };

int main() {
    string s;
    FAST_IO;

    cin >> s;

    dp[0] = (int)s[0] > '0';
    for (int i = 1; i < s.length(); i++) {
        if(s[i] > '0') dp[i] += dp[i - 1];
        if (s[i - 1] == '1' || (s[i - 1] == '2' && s[i] <= '6')) dp[i] += dp[max(0, i - 2)];
        dp[i] %= MOD;
    }

    cout << dp[s.length() - 1];

    return 0;
}