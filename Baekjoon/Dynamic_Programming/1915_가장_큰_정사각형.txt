// https://www.acmicpc.net/problem/1915
#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>

using namespace std;

char arr[1005][1005];
int dp[1005][1005] = { 0 };

int main() {
    int answer = 0;
    int i, j, a, b, c;
    int n, m;
    FAST_IO;

    cin >> n >> m;

    for (i = 0; i < n; i++) cin >> arr[i];

    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            if (arr[i][j] == '0') continue;

            a = i > 0 ? dp[i - 1][j] + 1 : 1; // 위
            b = j > 0 ? dp[i][j - 1] + 1 : 1; // 왼
            c = i > 0 && j > 0 ? dp[i - 1][j - 1] + 1 : 1; // 대각선(왼위)

            dp[i][j] = min(a, min(b, c));
            answer = max(answer, dp[i][j]);
        }
    }

    cout << answer * answer << '\n';


    return 0;
}