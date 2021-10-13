// https://codeforces.com/contest/1593/problem/C

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

int arr[400001];

int main() {
    int i, t;
    FAST_IO;

    cin >> t;

    for (i = 0; i < t; i++) {
        int j, n, k;
        cin >> n >> k;
        for (j = 0; j < k; j++) cin >> arr[j];

        int idx = 0, cat = 0;
        sort(arr, arr + k, greater<int>());
        while (idx < k && cat < n) {
            if (cat >= arr[idx]) break;
            cat += n - arr[idx++];
        }

        cout << idx << '\n';
    }

    return 0;
}