// https://www.acmicpc.net/problem/11505

#include <stdio.h>

using namespace std;

typedef long long ll;
const int MOD = 1000000007;
ll tree[4000004];

ll multi(int from, int to, int index, int left, int right)
{
    if (from > right || to < left)
        return 1;
    if (left <= from && right >= to)
        return tree[index];

    int mid = (from + to) / 2;
    return multi(from, mid, index * 2, left, right) * multi(mid + 1, to, index * 2 + 1, left, right) % MOD;
}

ll update(int from, int to, int index, int target, int value)
{
    if (target < from || target > to)
        return tree[index];
    if (from == to)
        return tree[index] = value;

    int mid = (from + to) / 2; 

    return tree[index] = update(from, mid, index * 2, target, value) * update(mid + 1, to, index * 2 + 1, target, value) % MOD;
}

int main()
{
    int i, a, b, c, n, m, k;

    scanf("%d %d %d", &n, &m, &k);

    for (i = 1; i <= n; i++) {
        scanf(" %d", &a);
        update(1, n, 1, i, a);
    }   

    for (i = 0; i < m + k; i++)
    {
        scanf("%d %d %d", &a, &b, &c);
        if (a == 1)
            update(1, n, 1, b, c);
        else
            printf("%lld\n", multi(1, n, 1, b, c));
    }

    return 0;
}