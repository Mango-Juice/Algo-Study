// https://www.acmicpc.net/problem/19637

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <string>

using namespace std;

int power[100001];
string names[100001];
int newN;

string solution(int target) {
    int left = 0;
    int right = newN - 1;

    while (left < right) {
        int center = (left + right) / 2;
        
        if (power[center] >= target) {
            right = center;
            if (left == right) break;
        }
        else left = center + 1;
    }

    return names[right];
}

int main() {
    FAST_IO;
    int i, N, M;

    cin >> N >> M;

    int idx = 0;
    newN = N;
    for (i = 0; i < N; i++) {
        cin >> names[idx];
        cin >> power[idx];

        if (idx > 0 && power[idx] == power[idx - 1]) newN--;
        else idx++;
    }

    for (i = 0; i < M; i++) {
        int target;
        cin >> target;
        cout << solution(target) << '\n';
    }

    return 0;
}