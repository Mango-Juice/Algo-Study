// https://www.acmicpc.net/problem/17976

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<int, int>> v;
int n;

bool possible(int a) {
    int i;
    int last = v[0].first;

    for (i = 1; i < n; i++) {
        if (last <= v[i].first - a) last = v[i].first;
        else if (last - v[i].second > v[i].first - a) return false;
        else last += a;
    }

    return true;
}

int main() {
    int i, a, b, tmp;
    int maxi = 0, mini = 1000000001;
    FAST_IO;

    cin >> n;

    for (i = 0; i < n; i++) {
        cin >> a >> b;
        v.push_back(make_pair(a, b));
        mini = min(mini, a);
        maxi = max(maxi, a + b);
    }

    sort(v.begin(), v.end());

    int l = 0, r = maxi - mini, mid, result = 0;
    while (l <= r) {
        mid = r - (r - l) / 2;
        if (possible(mid)) {
            result = mid;
            l = mid + 1;
        }
        else r = mid - 1;
    }

    cout << result;

    return 0;
}