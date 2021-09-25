// https://www.acmicpc.net/problem/1107

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

const int MAX = 1000010;
int broken = 0, result = MAX, N;

int getCount(int n) {
    if (n == 0) return abs(n - N) + 1;
    return abs(n - N) + (int)floor(log10(n)) + 1;
}

void findNearestNumber(int n) {
    if (n > MAX) return;

    int count = getCount(n);
    if (count < result) if(n > 0 || (broken & 1) == 0) result = count;

    for (int i = 0; i < 10; i++) {
        if (broken & (1 << i)) continue;
        if (n == 0 && i == 0) continue;
        findNearestNumber(n * 10 + i);
    }
}

int main() {
    int tmp, M;
    FAST_IO;

    cin >> N; cin >> M;

    for (int i = 0; i < M; i++) {
        cin >> tmp;
        broken |= (1 << tmp);
    }

    if (broken != (1 << 10) - 1) findNearestNumber(0);     
    cout << min(result, abs(100 - N));
    return 0;
}