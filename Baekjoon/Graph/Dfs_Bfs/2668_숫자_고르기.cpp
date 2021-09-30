// https://www.acmicpc.net/problem/2668

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>

using namespace std;

vector<int> answer;
int arr[102];
bool visited[102] = { false };

void checkCycle(int target, int now) {
    if (visited[now]) {
        if (target == now) answer.push_back(target);
        return;
    }
    visited[now] = true;
    checkCycle(target, arr[now]);
}

int main() {
    int N, i;
    FAST_IO;

    cin >> N;
    for (i = 1; i <= N; i++) cin >> arr[i];

    for (i = 1; i <= N; i++) {
        checkCycle(i, i);
        memset(visited, false, sizeof(visited));
    }

    cout << answer.size();
    for (i = 0; i < answer.size(); i++) cout << '\n' << answer[i];

    return 0;
}