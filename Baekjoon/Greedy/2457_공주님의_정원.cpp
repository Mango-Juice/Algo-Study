// https://www.acmicpc.net/problem/2457
#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const pair<int, int> finish = { 11, 30 };
const pair<int, int> start = { 3, 1 };
const pair<int, int> zero = { 0, 0 };
vector<pair<pair<int, int>, pair<int, int>>> v;

int main() {
    int a, b, c, d, idx = 0;
    int i, N, answer = 0;
    pair<int, int> now = start, max = { 0, 0 };

    cin >> N;

    for (i = 0; i < N; i++) {
        cin >> a >> b >> c >> d;
        v.push_back({ {a, b}, {c, d} });
    }

    sort(v.begin(), v.end());

    for (i = 0; i < N; i++) {
        // 꽃을 다 심었으면 break
        if (now > finish) break;

        // 심을 꽃 찾기
        if (max < v[i].second && v[i].first <= now) {
            idx = i;
            max = v[i].second;
        }

        // now에 포함되지 않는다면 날짜 갱신
        if (max != zero) {
            if (v[i].first > now) {
                now = v[idx].second;
                answer++;
                i--;
                max = zero;
            }
            else if (i == N - 1) {
                now = v[i].second;
                answer++;
            }
        }
        else { // 해당 날짜에 포함되는 꽃이 없으면 답은 0
            answer = 0;
            break;
        }

    }

    if (now > finish) cout << answer;
    else cout << 0;

    return 0;
}