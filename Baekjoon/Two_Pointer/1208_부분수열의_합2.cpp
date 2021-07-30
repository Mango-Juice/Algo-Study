// https://www.acmicpc.net/problem/1208

#include <iostream>
#include <algorithm>

using namespace std;

int arr[40];
int hap[2][1500000];
int idx[] = { 0, 0 };

// 부분 집합의 합을 구하는 함수 (재귀)
void makeSum(int sum, int from, int to, int type) {
	if (from >= to) hap[type][idx[type]++] = sum;
	else {
		makeSum(sum, from + 1, to, type);
		makeSum(sum + arr[from], from + 1, to, type);
	}
}

int main(int argc, char** argv) {
	int i, n, s, left, right;
	unsigned long long answer = 0;

	cin >> n >> s;

	for (i = 0; i < n; i++) cin >> arr[i];

	// 반 쪼개서 각각의 부분 집합의 합 구하기
	makeSum(0, 0, n / 2, 0);
	makeSum(0, n / 2, n, 1);

	// 오름차순 정렬
	sort(hap[0], hap[0] + idx[0]);
	sort(hap[1], hap[1] + idx[1]);

	// 투포인터
	left = 0;
	right = idx[1] - 1;

	while (left < idx[0] && right >= 0) {
		int lvalue = hap[0][left];
		int rvalue = hap[1][right];

		if (lvalue + rvalue < s) left++;
		else if (lvalue + rvalue > s) right--;
		else {
			// 같은 숫자 찾기
			unsigned long long lc = 0, rc = 0;
			while (left < idx[0] and hap[0][left] == lvalue) {
				lc++;
				left++;
			}
			while (right >= 0 and hap[1][right] == rvalue) {
				rc++;
				right--;
			}
			answer += lc * rc;
		}
	}

	if (s == 0) answer--; // 부분 집합 구하는 과정에서 공집합의 합을 0이라 뒀기 때문

	cout << answer;

	return 0;
}