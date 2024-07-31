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

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    int b, x, n;
    int answer = 0;
    short arr[288000][9] = { 0, };
    bool unfinished[9] = { false, };
    cin >> b >> x >> n;
    
    REP(i, 0, n) {
        REP(j, 0, 9) {
            cin >> arr[i][j];
        }
    }
    
    REP(j, 0, 9) {
        bool onLong = false;
        int single = 0;
        short last = -1;
        
        for(int i = n - 1; i >= 0; i--) {
            if(arr[i][j] == 2) {
                if(last == 0 || (last == -1 && arr[n-2][j] != 0)) {
                    onLong = true;
                    answer += 80;
                    answer += single * 100;
                    single = 1;
                } else {
                    onLong = false;
                    answer += (single + 1) * x / 6;
                    single = 0;
                }
            }
            else if(arr[i][j] == 1) {
                single++;
            }
            last = arr[i][j];
        }
        if(single > 0) {
            if(onLong) answer += single * x / 6;
            else answer += 100 * single;
        }
    }
    
    cout << answer;
}