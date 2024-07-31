#include <bits/stdc++.h>

#define F first
#define S second
#define B begin()
#define E end()
#define PB push_back
#define MP make_pair
#define REP(i, a, b) for (int i = a; i < b; i++)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

int n, l;
int x[100000], w[100000];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n >> l;
    
    REP(i, 0, n) cin >> x[i];
    REP(i, 0, n) cin >> w[i];
    
    double left = 0, right = l, mid;
    REP(i, 0, 100) {
        mid = (right + left) / 2;
        double hap = 0;
        
        REP(j, 0, n) hap += (x[j] - mid) * w[j];
        if(hap > 0) left = mid;
        else right = mid;
    }
    
    cout.precision(15);
    cout << mid;
}