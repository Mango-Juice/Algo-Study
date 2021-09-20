// https://www.acmicpc.net/problem/5904

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

int n, cnt = 0;

void print(char a) {
    cout << a;
    exit(0);
}

void solution(int a) {
    if (a == 1) {
        if (cnt + 1 == n) print('m');
        else if (n - cnt <= 3) print('o');
        cnt += 3;
        return;
    }

    solution(a - 1);
    if (++cnt == n) print('m');
    for (int i = 0; i <= a; i++) if (++cnt == n) print('o');
    solution(a - 1);
}

int main() {
    FAST_IO;
    cin >> n;
    solution(30);
    return 0;
}