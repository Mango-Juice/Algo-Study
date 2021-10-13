// https://codeforces.com/contest/1566/problem/A

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)
 
#include <iostream>
 
using namespace std;
 
int main() {
	FAST_IO;
 
	int t;
	cin >> t;
 
	for (int i = 0; i < t; i++) {
		int n, s;
		cin >> n >> s;
		int target = (n - 1) / 2;
		int range = n - target;
		cout << (int)(s / range) << '\n';
	}
 
	return 0;
}