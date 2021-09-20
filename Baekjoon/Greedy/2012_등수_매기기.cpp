// https://www.acmicpc.net/problem/2012

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int arr[500001];

int main() {
    int i, N;
    long long answer = 0;
    FAST_IO;
    
    cin >> N;

    for (i = 0; i < N; i++) cin >> arr[i];
    sort(arr, arr + N);

    for (i = 0; i < N; i++) answer += abs(i + 1 - arr[i]);

    cout << answer;
    return 0;
}