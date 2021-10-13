// https://codeforces.com/contest/1579/problem/B

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>
#include <tuple>
#include <vector>

using namespace std;

int arr[51];
int sorted_arr[51];

void shift(int f, int t) {
    int tmp = arr[f];
    for (int i = f; i < t; i++) arr[i] = arr[i + 1];
    arr[t] = tmp;
}

int main() {
    int i, j, t, n;
    FAST_IO;

    cin >> t;

    for(i = 0; i < t; i++){
        vector<tuple<int, int, int>> answer;
        cin >> n;

        for (j = 0; j < n; j++) {
            cin >> arr[j];
            sorted_arr[j] = arr[j];
        }

        sort(sorted_arr, sorted_arr + n);

        for (j = 0; j < n - 1; j++) {
            int tmp = 0;

            while (arr[j] != sorted_arr[j]) {
                shift(j, n - 1);
                tmp++;
            }

            if (tmp > 0) answer.push_back(tuple<int, int, int>(j + 1, n, tmp));
        }

        cout << answer.size() << '\n';

        for (j = 0; j < answer.size(); j++)
            cout << get<0>(answer[j]) << ' ' << get<1>(answer[j]) << ' ' << get<2>(answer[j]) << '\n';

    }

    return 0;
}