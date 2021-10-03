// https://www.acmicpc.net/problem/13904

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>

using namespace std;

pair<int, int> arr[1001];
int visited[1002] = { false };

bool compare(pair<int, int> a, pair<int, int>b) { return a.second > b.second; }

int main() {
    int i, day, N, answer = 0;
    FAST_IO;

    cin >> N;
    for (i = 0; i < N; i++) cin >> arr[i].first >> arr[i].second;
    sort(arr, arr + N, compare);

    for (i = 0; i < N; i++) {
        day = arr[i].first;
        while (visited[day] && day >= 1) day--;
        if (day >= 1) {
            visited[day] = true;
            answer += arr[i].second;
        }
    }

    cout << answer;

    return 0;
}