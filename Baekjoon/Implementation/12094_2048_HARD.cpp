// https://www.acmicpc.net/problem/12094

#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

enum { UP = 0, DOWN, LEFT, RIGHT };
const int ga[11] = { 1024, 518, 256, 128, 64, 32, 16, 8, 4, 2, 1 };
const int MAX = 21;

int n;
int answer = 0;

int getMax(int board[][MAX]) {
	int result = 0;
	int i, j;
	for (i = 0; i < n; i++) for (j = 0; j < n; j++) result = max(result, board[i][j]);
	return result;
}

void upBoard(int board[][MAX]) {
	int i, j, value, idx;

	for (j = 0; j < n; j++) {
		value = -1, idx = -1;
		for (i = 0; i < n; i++) {
			if (board[i][j] == 0) continue;
			if (board[i][j] == value) {
				board[idx][j] <<= 1;
				value = -1;
			}
			else {
				value = board[i][j];
				board[++idx][j] = board[i][j];
			}
		}
		for (i = idx + 1; i < n; i++) board[i][j] = 0;
	}
}

void downBoard(int board[][MAX]) {
	int i, j, value, idx;

	for (j = 0; j < n; j++) {
		value = -1, idx = n;
		for (i = n - 1; i >= 0; i--) {
			if (board[i][j] == 0) continue;
			if (board[i][j] == value) {
				board[idx][j] <<= 1;
				value = -1;
			}
			else {
				value = board[i][j];
				board[--idx][j] = board[i][j];
			}
		}
		for (i = idx - 1; i >= 0; i--) board[i][j] = 0;
	}
}

void leftBoard(int board[][MAX]) {
	int i, j, value, idx;

	for (i = 0; i < n; i++) {
		value = -1, idx = -1;
		for (j = 0; j < n; j++) {
			if (board[i][j] == 0) continue;
			if (board[i][j] == value) {
				board[i][idx] <<= 1;
				value = -1;
			}
			else {
				value = board[i][j];
				board[i][++idx] = board[i][j];
			}
		}
		for (j = idx + 1; j < n; j++) board[i][j] = 0;
	}
}

void rightBoard(int board[][MAX]) {
	int i, j, value, idx;

	for (i = 0; i < n; i++) {
		value = -1, idx = n;
		for (j = n - 1; j >= 0; j--) {
			if (board[i][j] == 0) continue;
			if (board[i][j] == value) {
				board[i][idx] <<= 1;
				value = -1;
			}
			else {
				value = board[i][j];
				board[i][--idx] = board[i][j];
			}
		}
		for (j = idx - 1; j >= 0; j--) board[i][j] = 0;
	}
}

void dfs(int board[][MAX], int count) {
	//printf("%d\n", count);
	if (count == 10) return;

	for (int i = 0; i < 4; i++) {
		int now[MAX][MAX];
		copy(&board[0][0], &board[0][0] + 441, &now[0][0]);

		switch (i) {
		case UP: upBoard(now); break;
		case DOWN: downBoard(now); break;
		case LEFT: leftBoard(now); break;
		case RIGHT: rightBoard(now);
		}

		int max_val = getMax(now);

		if (!equal(&board[0][0], &board[0][0] + 441, &now[0][0]) && max_val * ga[count + 1] > answer) {
			answer = max(answer, max_val);
			dfs(now, count + 1);
		}
	}
}

int main(void) {
	int arr[MAX][MAX];
	int i, j;

	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			scanf(" %d", &arr[i][j]);
			answer = max(answer, arr[i][j]);
		}
	}

	dfs(arr, 0);
	printf("%d", answer);

	return 0;
}