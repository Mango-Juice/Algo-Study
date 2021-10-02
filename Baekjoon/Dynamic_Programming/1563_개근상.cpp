// https://www.acmicpc.net/problem/1563

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

const int MOD = 1000000;
int arr[1001][2][3] = { 0 };

int main() {
    int i, N;
    arr[0][0][0] = 1;
    arr[0][1][0] = 1;
    arr[0][0][1] = 1;
    FAST_IO;

    cin >> N;

    for (i = 1; i < N; i++) {
        // 출석
        arr[i][0][0] = (arr[i][0][0] + arr[i - 1][0][0] + arr[i - 1][0][1] + arr[i - 1][0][2]) % MOD;
        arr[i][1][0] = (arr[i][1][0] + arr[i - 1][1][0] + arr[i - 1][1][1] + arr[i - 1][1][2]) % MOD;

        // 지각
        arr[i][1][0] = (arr[i][1][0] + arr[i][0][0]) % MOD;

        // 결석
        arr[i][0][1] = (arr[i][0][1] + arr[i - 1][0][0]) % MOD;
        arr[i][0][2] = (arr[i][0][2] + arr[i - 1][0][1]) % MOD;
        arr[i][1][1] = (arr[i][1][1] + arr[i - 1][1][0]) % MOD;
        arr[i][1][2] = (arr[i][1][2] + arr[i - 1][1][1]) % MOD;
    }

    cout << (arr[N - 1][0][0] + arr[N - 1][0][1] + arr[N - 1][0][2] + arr[N - 1][1][0] + arr[N - 1][1][1] + arr[N - 1][1][2]) % MOD;

    return 0;
}