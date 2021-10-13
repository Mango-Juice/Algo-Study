// https://codeforces.com/contest/1579/problem/D

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int i, j, t, n;
    FAST_IO;

    cin >> t;

    for(i = 0; i < t; i++){
        priority_queue<pair<int, int>> q;
        vector<pair<int, int>> answer;
        cin >> n;

        for (j = 0; j < n; j++) {
            int tmp;
            cin >> tmp;
            q.push(pair<int, int>(tmp, j));
        }

        while (q.top().first > 0) {
            pair<int, int> a = q.top(); q.pop();
            pair<int, int> b = q.top(); q.pop();

            if (b.first == 0) break;
            answer.push_back(pair<int, int>(a.second, b.second));
            a.first--; b.first--;
            q.push(a); q.push(b);
        }

        cout << answer.size() << '\n';
        for (j = 0; j < answer.size(); j++)
            cout << answer[j].first + 1 << " " << answer[j].second + 1 << '\n';
    }

    return 0;
}