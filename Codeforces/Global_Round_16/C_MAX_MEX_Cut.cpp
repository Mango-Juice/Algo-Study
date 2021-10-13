// https://codeforces.com/contest/1566/problem/C

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)
 
#include <iostream>
#include <algorithm>
 
using namespace std;
 
int arr[100001] = { 0 };
char a[100001];
char b[100001];
 
int main() {
	FAST_IO;
 
	int t, l, answer, i, j;
	cin >> t;
 
	for (j = 0; j < t; j++) {
		cin >> l;
 
		cin >> a;
		cin >> b;
 
		answer = 0;
		for (i = 0; i < l; i++) {
			if (a[i] == b[i]) {
				arr[i] = 1 - a[i] + '0';
				answer += arr[i];
 
				if (i > 0 && arr[i] + arr[i - 1] == 1) {
					arr[i] = 2;
					answer++;
				}
			}
			else {
				arr[i] = 2;
				answer += 2;
			}
		}
 
		cout << answer<< '\n';
	}
 
	return 0;
}