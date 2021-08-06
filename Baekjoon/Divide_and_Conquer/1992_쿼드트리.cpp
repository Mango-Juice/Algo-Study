// https://www.acmicpc.net/problem/1992

#include <iostream>
#include <string>

using namespace std;

int i, j, n;
string arr[65];

string solution(int fx, int fy, int tx, int ty) {
	char check = arr[fx][fy];
	bool flag = true;
	string result;

	for (i = fx; i <= tx; i++) {
		for (j = fy; j <= ty; j++) {
			if (arr[i][j] != check) {
				flag = false;
				break;
			}
		}
	}

	if (flag) result.push_back(check);
	else {
		result.push_back('(');
		int dx = tx - fx, dy = ty - fy;
		result += solution(fx, fy, fx + dx / 2, fy + dy / 2);
		result += solution(fx, fy + dy / 2 + 1, fx + dx / 2, ty);
		result += solution(fx + dx / 2 + 1, fy, tx, fy + dy / 2);
		result += solution(fx + dx / 2 + 1, fy + dy / 2 + 1, tx, ty);
		result.push_back(')');
	}

	return result;
}

int main() {
	ios::sync_with_stdio(false); 
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (i = 0; i < n; i++) cin >> arr[i];

	cout << solution(0, 0, n - 1, n - 1);

	return 0;
}