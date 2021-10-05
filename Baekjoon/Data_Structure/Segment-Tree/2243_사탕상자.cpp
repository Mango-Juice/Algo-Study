// https://www.acmicpc.net/problem/2243

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

const int MAX = 1000001;
int tree[MAX * 4 + 1] = { 0 };

void update(int idx, int target, int cha, int from, int to) {
    if (target < from || target > to) return;
    tree[idx] += cha;
    if (from == to) return;
    int mid = (from + to) / 2;
    update(idx * 2, target, cha, from, mid);
    update(idx * 2 + 1, target, cha, mid + 1, to);
}

int getIndex(int idx, int target, int from, int to) {
    if (from == to) return from;
    int mid = (from + to) / 2;
    if (target <= tree[idx * 2]) return getIndex(idx * 2, target, from, mid);
    return getIndex(idx * 2 + 1, target - tree[idx * 2], mid + 1, to);
}

int main() {
    int i, a, b, c, n;
    FAST_IO;

    cin >> n;
    for (i = 0; i < n; i++) {
        cin >> a;
        if (a == 1) {
            cin >> b;
            int idx = getIndex(1, b, 1, MAX);
            cout << idx << '\n';
            update(1, idx, -1, 1, MAX);
        }
        else {
            cin >> b >> c;
            update(1, b, c, 1, MAX);
        }
    }
    
    return 0;
}