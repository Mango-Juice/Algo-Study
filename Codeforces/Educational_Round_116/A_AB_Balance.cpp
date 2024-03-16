// https://codeforces.com/contest/1606/problem/A

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <string>

using namespace std;

int main() {
    int i, j, t;
    FAST_IO;

    cin >> t;

    for (i = 0; i < t; i++) {
        int ab = 0, ba = 0;
        string s;
        cin >> s;

        for (j = 1; j < s.length(); j++) {
            if (s[j - 1] == 'a' && s[j] == 'b') ab++;
            else if (s[j - 1] == 'b' && s[j] == 'a') ba++;
        }

        for (j = s.length() - 1; j >= 0; j--) {
            if (ab == ba) break;
            if (ab > ba) {
                if (j > 0 && s[j - 1] == 'a' && s[j] == 'b') ab--;
                else if (j > 0 && s[j - 1] == 'b' && s[j] == 'b') ba++;
                s[j] = 'a';
            }
            else {
                if (j > 0 && s[j - 1] == 'b' && s[j] == 'a') ba--;
                else if (j > 0 && s[j - 1] == 'a' && s[j] == 'a') ab++;
                s[j] = 'b';
            }
        }

        cout << s << '\n';
    }
}