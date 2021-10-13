// https://codeforces.com/contest/1573/problem/A

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)
 
#include <iostream>
 
using namespace std;
 
int main() {
    int i, t;
    FAST_IO;
 
    cin >> t;
 
    for (i = 0; i < t; i++) {
        int n, answer = 0;
        char arr[105];
 
        cin >> n;
        cin >> arr;
 
        while (arr[n - 1] != '0') {
            arr[n - 1]--;
            answer++;
        }
 
        for (int j = 0; j < n - 1; j++) if (arr[j] != '0') answer += arr[j] - '0' + 1;
 
        cout << answer << '\n';
    }
 
    return 0;
}