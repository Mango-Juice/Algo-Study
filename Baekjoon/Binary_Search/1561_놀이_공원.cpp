// https://www.acmicpc.net/problem/1561

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>

using namespace std;
typedef long long ll;
int arr[10001];
ll N, M;

ll getPerson(ll time) {
    ll hap = M;
    for (int i = 0; i < M; i++) hap += time / arr[i];
    return hap;
}

int main() {
    int i;
    int maximum = 0;
    FAST_IO;

    cin >> N >> M;
    for (i = 0; i < M; i++) {
        cin >> arr[i];
        maximum = max(maximum, arr[i]);
    }

    if (N <= M) {
        cout << N;
        return 0;
    }

    ll left = 0, right = (ll)maximum * N, mid, result = 0;
    while (left <= right) {
        mid = (left + right) / 2;
        if (getPerson(mid) >= N) {
            result = mid;
            right = mid - 1;
        }
        else left = mid + 1;
    }

    ll people = getPerson(result - 1);

    for (i = 0; i < M; i++) {
        if (result % arr[i] == 0) people++;
        if (people == N) {
            cout << i + 1;
            break;
        }
    }

    return 0;
}