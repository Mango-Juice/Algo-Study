// https://codeforces.com/contest/1579/problem/A

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)
 
#include <iostream>
#include <string>
 
using namespace std;
 
 
int main() {
    int i, j, t;
    string s;
    FAST_IO;
 
    cin >> t;
 
    for(i = 0; i < t; i++){
        int count[3] = { 0 };
        cin >> s;
        for (j = 0; j < s.size(); j++) count[s[j] - 'A']++;
        if (count[0] + count[2] == count[1]) cout << "YES" << '\n';
        else cout << "NO" << '\n';
    }
 
    return 0;
}