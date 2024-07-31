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

int gcd(int a, int b) {
    if(b == 0) return a;
    return gcd(b, a % b);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    int n, answer = 0;
    cin >> n;
    
    vi factors;
    for(int i = 1; i * i <= n; i++) {
        if(n % i == 0) { 
            factors.PB(i);
            if(i != n / i) factors.PB(n / i);
        }
    }
    
    for(int fac: factors) {
        int target = fac + 1;
        REP(i, 1, target / 2 + 1) {
            if(gcd(target - i, i) == 1) {
                answer++;
            }
        }
    }
    
    cout << answer;
}