// https://www.acmicpc.net/problem/2115

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

int N, M;
char arr[1001][1001];

int up() {
    int r = 0, c = 1, result = 0;

    while (r < N - 1) {
        if (arr[r][c] == '.' && arr[r][c - 1] == '.' && arr[r + 1][c] == 'X' && arr[r + 1][c - 1] == 'X') {
            result++;
            c++;
        }
        if (++c >= M) {
            r++;
            c = 1;
        }
    }

    return result;
}

int down() {    
    int r = 0, c = 1, result = 0;

    while (r < N - 1) {
        if (arr[r][c] == 'X' && arr[r][c - 1] == 'X' && arr[r + 1][c] == '.' && arr[r + 1][c - 1] == '.') {
            result++;
            c++;
        }
        if (++c >= M) {
            r++;
            c = 1;
        }
    }

    return result;
}

int left() {
    int c = 0, r = 1, result = 0;

    while (c < M - 1) {
        if (arr[r][c] == '.' && arr[r - 1][c] == '.' && arr[r][c + 1] == 'X' && arr[r - 1][c + 1] == 'X') {
            result++;
            r++;
        }
        if (++r >= N) {
            c++;
            r = 1;
        }
    }
    return result;
}

int right() {
    int c = 0, r = 1, result = 0;

    while (c < M - 1) {
        if (arr[r][c] == 'X' && arr[r - 1][c] == 'X' && arr[r][c + 1] == '.' && arr[r - 1][c + 1] == '.') {
            result++;
            r++;
        }
        if (++r >= N) {
            c++;
            r = 1;
        }
    }
    return result;
}

int solution() { 
    if (M == 1 || N == 1) return 0;
    return up() + down() + left() + right();
}

int main() {
    int i;
    FAST_IO;

    cin >> N >> M;
    for (i = 0; i < N; i++) cin >> arr[i];

    cout << solution();
    return 0;
}