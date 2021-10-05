// https://www.acmicpc.net/problem/16287

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

int arr[5001];
bool exist[800000];

int main() {
    int i, j, w, n;
    FAST_IO;

    cin >> w >> n;
    for (i = 0; i < n; i++) cin >> arr[i];

    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (arr[i] + arr[j] > w) continue;
            if (exist[w - arr[i] - arr[j]]) {
                cout << "YES";
                return 0;
            }
        }
        for (j = 0; j < i; j++) if(arr[i] + arr[j] < w) exist[arr[i] + arr[j]] = true;
    }

    cout << "NO";

    return 0;
}