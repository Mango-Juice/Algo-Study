#include <bits/stdc++.h>

#define F first
#define S second
#define B begin()
#define E end()
#define PB push_back
#define MP make_pair
#define REP(i, a, b) for (int i = a; i < b; i++)
#define endl "\n"

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

int n, k;
int arr[40];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n;
    REP(i, 0, n) cin >> arr[i];
    cin >> k;

    int center = n / 2;
    vi v1;
    unordered_map<int, int> m1;

    REP(i, 0, 1 << center) {
        int value = 0;
        REP(j, 0, center) {
            if(i & (1 << j)) value += arr[j];
        }
        v1.PB(value);
        m1[value] = i;
    }

    sort(v1.B, v1.E);
    REP(i, 0, 1 << (n - center)) {
        int value = 0;
        REP(j, 0, (n - center)) {
            if(i & (1 << j)) value += arr[center + j];
        }

        int target = *lower_bound(v1.B, v1.E, k - value);
        if(value + target == k) {
            REP(l, 0, center) cout << ((m1[target] & (1 << l)) ? 1 : 0);
            REP(l, 0, (n - center)) cout << ((i & (1 << l)) ? 1 : 0);
            return 0;
        }
    }

    return 0;
}