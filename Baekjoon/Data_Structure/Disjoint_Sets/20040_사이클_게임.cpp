// https://www.acmicpc.net/problem/20040
#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>

using namespace std;

int tree[1000001] = { 0 };

int Find(int a) {
    if (tree[a] == -1) return a;
    tree[a] = Find(tree[a]);
    return tree[a];
}

void Union(int a, int b) { tree[a] = b; }

int main() {
    int a, b, i, n, m;
    FAST_IO;

    cin >> n >> m;
    fill_n(tree, n, -1);

    for (i = 0; i < m; i++) {
        cin >> a >> b;
        a = Find(a); b = Find(b);
        if (a == b) {
            cout << i + 1;
            return 0;
        }
        Union(a, b);
    }

    cout << 0;
    return 0;
}