// https://www.acmicpc.net/problem/21758

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>

using namespace std;

int arr[100001];
int hap[100001];

int main() {
    int i, N, hap1, hap2, tong = 0;
    int answer;
    FAST_IO;

    cin >> N;
    for (i = 0; i < N; i++) {
        cin >> arr[i];
        hap[i] = i == 0 ? arr[i] : hap[i - 1] + arr[i];
        tong = max(tong, arr[i]);
    }

    // 통이 가운데에 있을 때
    answer = hap[N - 1] - arr[0] - arr[N - 1] + tong;

    for (i = 1; i < N - 1; i++) {
        // 통이 가장 왼쪽에 있을 때 - 벌 중 하나는 가장 오른쪽에 있음.
        hap1 = hap[N - 1] - arr[N - 1] - arr[i];
        hap2 = hap[i - 1];
        answer = max(answer, hap1 + hap2);

        // 통이 가장 오른쪽에 있을 때 - 벌 중 하나는 가장 왼쪽에 있음.
        hap1 = hap[N - 1] - arr[0] - arr[i];
        hap2 = hap[N - 1] - hap[i];
        answer = max(answer, hap1 + hap2);
    }

    cout << answer;

    return 0;
}