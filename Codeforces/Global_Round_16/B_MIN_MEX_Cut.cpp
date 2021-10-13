// https://codeforces.com/contest/1566/problem/B

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)
 
#include <iostream>
#include <string>
#include <algorithm>
 
using namespace std;
 
int main() {
	FAST_IO;
 
	int t;
	cin >> t;
 
	for (int i = 0; i < t; i++) {
		string s;
		cin >> s;
 
		// 0 덩어리 세기
		int count = 0;
		int last = -1;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '0' && last != '0') count++;
			last = s[i];
		}
		
		if (count == 0) cout << 0 << '\n';
		else if (count > 2) cout << 2 << '\n';
		else cout << count << '\n';
	}
 
	return 0;
}