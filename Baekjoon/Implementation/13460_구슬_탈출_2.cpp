// https://www.acmicpc.net/problem/13460

#include <stdio.h>
#include <algorithm>

using namespace std;

const int MAX = 10;
enum type { EMPTY = 0, WALL, HOLE, BALL };
enum direction { LEFT = 0, RIGHT, UP, DOWN };

bool success = false, fail = false;
int answer = 100;

bool moveLeft(pair<int, int>& target, int arr[][MAX]) {
	int& a = target.second;
	arr[target.first][a] = EMPTY;

	while (arr[target.first][--a] == EMPTY);
	if (arr[target.first][a] == HOLE) return true;

	arr[target.first][++a] = BALL;
	return false;
}

bool moveRight(pair<int, int>& target, int arr[][MAX]) {
	int& a = target.second;
	arr[target.first][a] = EMPTY;

	while (arr[target.first][++a] == EMPTY);
	if (arr[target.first][a] == HOLE) return true;

	arr[target.first][--a] = BALL;
	return false;
}

bool moveUp(pair<int, int>& target, int arr[][MAX]) {
	int& a = target.first;
	arr[a][target.second] = EMPTY;

	while (arr[--a][target.second] == EMPTY);
	if (arr[a][target.second] == HOLE) return true;

	arr[++a][target.second] = BALL;
	return false;
}

bool moveDown(pair<int, int>& target, int arr[][MAX]) {
	int& a = target.first;
	arr[a][target.second] = EMPTY;

	while (arr[++a][target.second] == EMPTY);
	if (arr[a][target.second] == HOLE) return true;

	arr[--a][target.second] = BALL;
	return false;
}

void tiltLeft(pair<int, int>& red, pair<int, int>& blue, int arr[][MAX]) {
	if (red.first == blue.first && blue.second < red.second) {
		fail = moveLeft(blue, arr);
		success = moveLeft(red, arr);
	}
	else {
		success = moveLeft(red, arr);
		fail = moveLeft(blue, arr);
	}
}

void tiltRight(pair<int, int>& red, pair<int, int>& blue, int arr[][MAX]) {
	if (red.first == blue.first && blue.second > red.second) {
		fail = moveRight(blue, arr);
		success = moveRight(red, arr);
	}
	else {
		success = moveRight(red, arr);
		fail = moveRight(blue, arr);
	}
}

void tiltUp(pair<int, int>& red, pair<int, int>& blue, int arr[][MAX]) {
	if (red.second == blue.second && blue.first < red.first) {
		fail = moveUp(blue, arr);
		success = moveUp(red, arr);
	}
	else {
		success = moveUp(red, arr);
		fail = moveUp(blue, arr);
	}
}

void tiltDown(pair<int, int>& red, pair<int, int>& blue, int arr[][MAX]) {
	if (red.second == blue.second && blue.first > red.first) {
		fail = moveDown(blue, arr);
		success = moveDown(red, arr);
	}
	else {
		success = moveDown(red, arr);
		fail = moveDown(blue, arr);
	}
}

void dfs(int count, pair<int, int> red, pair<int, int> blue, int arr[][MAX]) {
	if (count == 10) return;

	for (int i = 0; i < 4; i++) {
		int new_arr[MAX][MAX];
		copy(&arr[0][0], &arr[0][0] + (MAX * MAX), &new_arr[0][0]);
		pair<int, int> new_red(red);
		pair<int, int> new_blue(blue);

		switch (i) {
		case LEFT: tiltLeft(new_red, new_blue, new_arr);  break;
		case RIGHT: tiltRight(new_red, new_blue, new_arr); break;
		case UP: tiltUp(new_red, new_blue, new_arr); break;
		case DOWN: tiltDown(new_red, new_blue, new_arr); break;
		}

		if (fail || success) {
			if (success && !fail) answer = min(answer, count + 1);
			success = false;
			fail = false;
			continue;
		}
		if (!equal(&arr[0][0], &arr[0][0] + (MAX * MAX), &new_arr[0][0])) dfs(count + 1, new_red, new_blue, new_arr);
	}
}

int main(void) {
	char tmp;
	int i, j, n, m;
	int arr[MAX][MAX] = { EMPTY };
	pair<int, int> red(0, 0);
	pair<int, int> blue(0, 0);

	scanf("%d %d ", &n, &m);

	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			scanf("%c", &tmp);

			switch (tmp) {
			case '#': arr[i][j] = WALL; break;
			case '.': arr[i][j] = EMPTY; break;
			case 'O': arr[i][j] = HOLE; break;
			case 'R': arr[i][j] = BALL; red.first = i; red.second = j; break;
			case 'B': arr[i][j] = BALL; blue.first = i; blue.second = j; break;
			}
		}
		scanf("%c", &tmp);
	}

	dfs(0, red, blue, arr);
	printf("%d", answer < 100 ? answer : -1);

	return 0;
}