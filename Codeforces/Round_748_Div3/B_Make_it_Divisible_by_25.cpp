// https://codeforces.com/contest/1593/problem/B

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

void sol(int &answer, string &s, char q, char w) {
    int j, a = -1, b = -1;
    for (j = s.length() - 1; j >= 0; j--) {
        if (s[j] == w) {
            a = j;
            break;
        }
    }
    if (a != -1) {
        for (j = a - 1; j >= 0; j--) {
            if (s[j] == q) {
                b = j;
                break;
            }
        }
    }
    if (a != -1 && b != -1) answer = min(answer, (int)s.length() - b - 2);
}

int main() {
    int i, t;
    FAST_IO;

    cin >> t;

    for (i = 0; i < t; i++) {
        string s;
        cin >> s;
        if (stoll(s) % (long long)25 == 0) cout << 0 << '\n';
        else if (s.length() <= 2) cout << s.length() << '\n';
        else {
            int answer = s.length();
            int a = -1, b = -1;

            sol(answer, s, '2', '5');
            sol(answer, s, '5', '0');
            sol(answer, s, '7', '5');
            sol(answer, s, '0', '0');
            
            cout << answer << '\n';
            
        }
    }

    return 0;
}