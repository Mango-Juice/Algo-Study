// https://www.acmicpc.net/problem/3649

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>

using namespace std;
int arr[1000001];

int main() {
    FAST_IO;

    while (!cin.eof()) {
        int i, x, n;
        int l1 = -1, l2 = -1;

        cin >> x;
        if (cin.eof() == true) break;
        cin >> n;
        for (i = 0; i < n; i++) cin >> arr[i];

        x *= 10000000;
        sort(arr, arr + n);

        for (i = 0; i < n - 1; i++) {
            int target = x - arr[i];
            if (target < arr[i]) break;
            int* lb = lower_bound(arr + i + 1, arr + n, target);

            if (*lb == target) {
                l1 = arr[i];
                l2 = *lb;
                break;
            }
        }

        if (l1 > -1) {
            cout << "yes " << l1 << " " << l2 << '\n';
        }
        else {
            cout << "danger" << '\n';
        }
    }

    return 0;
}