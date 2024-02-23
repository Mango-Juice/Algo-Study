#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

int main() {
    int i, j, n;
    FAST_IO;

    cin >> n;
    for (i = 0; i < n - 1; ++i) {
        for (j = 0; j < i; ++j) cout << " ";
        for (j = 0; j < (n - i) * 2 - 1; ++j) cout << "*";
        cout << "\n";
    }
    for (i = n - 1; i >= 0; --i) {
        for (j = 0; j < i; ++j) cout << " ";
        for (j = 0; j < (n - i) * 2 - 1; ++j) cout << "*";
        cout << "\n";
    }

    return 0;
}