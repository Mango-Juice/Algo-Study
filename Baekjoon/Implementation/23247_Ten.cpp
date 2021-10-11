// https://www.acmicpc.net/problem/23247

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;
int arr[302][302] = { 0 };
int answer = 0;

bool hap(int a, int b, int c, int d) {
    int result = arr[c][d] - arr[c][b - 1] - arr[a - 1][d] + arr[a - 1][b - 1];
    if (result == 10) answer++;
    else if (result > 10) return false;
    return true;
}

int main() {
    int i, j, k, l, tmp, n, m;
    FAST_IO;

    cin >> n >> m;
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++) {
            cin >> tmp;
            arr[i][j] = tmp + arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1];
        }
    }

    // (i, j) : 왼위, (k, l) : 오아래
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++) {
            for (l = j; l <= m; l++) {
                bool flag = true;
                for (k = i; k <= n; k++) {
                    if (!hap(i, j, k, l)) break;
                    flag = false;
                }
                if (flag) break;
            }
        }
    }

    cout << answer;

    return 0;
}