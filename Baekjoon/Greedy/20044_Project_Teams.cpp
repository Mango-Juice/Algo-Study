// https://www.acmicpc.net/problem/20044

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>

using namespace std;

int arr[10001];

int main() {
    int i, n, answer = 500000;
    FAST_IO;

    cin >> n;
    for (i = 0; i < n * 2; i++) cin >> arr[i];
    sort(arr, arr + 2 * n);
    for (i = 0; i < n; i++) answer = min(answer, arr[i] + arr[2 * n - i - 1]);
    cout << answer;

    return 0;
}