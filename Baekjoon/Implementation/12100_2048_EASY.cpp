// https://www.acmicpc.net/problem/12100

#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<vector<int>> vvi;
enum { UP = 0, DOWN, LEFT, RIGHT };

int n;
int answer = 0;

void updateMax(vvi& board) {
	int i, j;
	for (i = 0; i < n; i++) for (j = 0; j < n; j++) answer = max(answer, board[i][j]);
}

void upBoard(vvi& board) {
	int i, j, newi, newj;
	bool flag;

	for (j = 0; j < n; j++) {
		flag = false;

		for (i = 1; i < n; i++) {
			newi = i, newj = j;

			while (newi > 0 && board[newi - 1][newj] == 0) {
				board[newi - 1][newj] = board[newi][newj];
				board[newi--][newj] = 0;
			}

			if (!flag && newi > 0 && board[newi - 1][newj] == board[newi][newj]) {
				board[newi - 1][newj] = board[newi][newj] * 2;
				board[newi][newj] = 0;
				flag = true;
			}
			else if (board[newi][newj] != 0) flag = false;
		}
	}
}

void downBoard(vvi& board) {
	int i, j, newi, newj;
	bool flag;

	for (j = 0; j < n; j++) {
		flag = false;

		for (i = n - 2; i >= 0; i--) {
			newi = i, newj = j;

			while (newi < n - 1 && board[newi + 1][newj] == 0) {
				board[newi + 1][newj] = board[newi][newj];
				board[newi++][newj] = 0;
			}

			if (!flag && newi < n - 1 && board[newi + 1][newj] == board[newi][newj]) {
				board[newi + 1][newj] = board[newi][newj] * 2;
				board[newi][newj] = 0;
				flag = true;
			}
			else if (board[newi][newj] != 0) flag = false;
		}
	}
}

void leftBoard(vvi& board) {
	int i, j, newi, newj;
	bool flag;

	for (i = 0; i < n; i++) {
		flag = false;

		for (j = 1; j < n; j++) {
			newi = i, newj = j;

			while (newj > 0 && board[newi][newj - 1] == 0) {
				board[newi][newj - 1] = board[newi][newj];
				board[newi][newj--] = 0;
			}

			if (!flag && newj > 0 && board[newi][newj - 1] == board[newi][newj]) {
				board[newi][newj - 1] = board[newi][newj] * 2;
				board[newi][newj] = 0;
				flag = true;
			}
			else if (board[newi][newj] != 0) flag = false;
		}
	}
}

void rightBoard(vvi& board) {
	int i, j, newi, newj;
	bool flag;

	for (i = 0; i < n; i++) {
		flag = false;

		for (j = n - 2; j >= 0; j--) {
			newi = i, newj = j;

			while (newj < n - 1 && board[newi][newj + 1] == 0) {
				board[newi][newj + 1] = board[newi][newj];
				board[newi][newj++] = 0;
			}

			if (!flag && newj < n - 1 && board[newi][newj + 1] == board[newi][newj]) {
				board[newi][newj + 1] = board[newi][newj] * 2;
				board[newi][newj] = 0;
				flag = true;
			}
			else if (board[newi][newj] != 0) flag = false;
		}
	}
}

void updateBoard(vvi& board, int type) {
	switch (type) {
	case UP: upBoard(board); break;
	case DOWN: downBoard(board); break;
	case LEFT: leftBoard(board); break;
	case RIGHT: rightBoard(board);
	}
}

void dfs(vvi board, int count) {
	if (count == 5) {
		updateMax(board);
		return;
	}

	for (int i = 0; i < 4; i++) {
		vvi now = board;
		updateBoard(now, i);
		dfs(now, count + 1);
	}
}

int main(void) {
	vvi arr;
	int i, j, tmp;

	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		vector<int> line;

		for (j = 0; j < n; j++) {
			scanf(" %d", &tmp);
			line.push_back(tmp);
			answer = max(answer, tmp);
		}

		arr.push_back(line);
	}

	dfs(arr, 0);
	printf("%d", answer);

	return 0;
}