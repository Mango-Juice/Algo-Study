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

vi primes;

int check(ll target) {
    ll result = target;
    queue<tuple<int, int, ll>> q;
    
    REP(i, 0, primes.size()) {
        ll prime = (ll) primes[i];
        if(prime * prime > target) break;
        q.push({1, i, prime});
    }
    
    while(!q.empty()) {
        auto [count, index, number] = q.front();
        q.pop();
        
        if(count & 1) result -= target / (number * number);
        else result += target / (number * number);
        
        REP(i, index + 1, primes.size()) {
            ll prime = (ll) primes[i];
            if(prime * prime * number * number > target) break;
            if(number % prime == 0) continue;
            q.push({count + 1, i, number * prime});
        }
    }
    
    return result;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    int k;
    cin >> k;
    
    // 1단계: 소수 찾기
    int numMax = sqrt(2 * k) + 1;
    vector<bool> isPrime(numMax, true);
    isPrime[0] = false;
    isPrime[1] = false;
    
    REP(i, 2, sqrt(numMax) + 1) {
        if(isPrime[i]) {
            for(int j = i * 2; j < numMax; j += i) {
                isPrime[j] = false;
            }
        }
    }
    
    REP(i, 2, numMax) {
        if(isPrime[i]) {
            primes.PB(i);
        }
    }

    // 2단게: 이분 탐색
    int l = 0, r = 2 * k, mid;
    while(l < r) {
        mid = (r - l) / 2 + l;
        if(check((ll) mid) < k) l = mid + 1;
        else r = mid;
    }
    
    cout << r;
}