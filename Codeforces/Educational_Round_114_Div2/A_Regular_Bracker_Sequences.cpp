// https://codeforces.com/contest/1574/problem/A

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)
 
#include <iostream>
#include <string>
 
using namespace std;
 
int finish = 0;
 
void solution(string s, int open, int n) {
    if (finish >= n) return;
    if (s.length() == 2 * n) {
        if (open == 0) {
            cout << s << '\n';
            finish++;
        }
        return;
    }
 
    if (open < 2 * n - s.length()) solution(s + '(', open + 1, n);
    if (open > 0) solution(s + ')', open - 1, n);
}
 
int main() {
    int t;
    FAST_IO;
 
    cin >> t;
    for (int i = 0; i < t; i++) {
        finish = 0;
        int n;
        cin >> n;
        solution("", 0, n);
    }
 
    return 0;
}