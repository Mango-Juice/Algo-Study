// https://www.acmicpc.net/problem/18119

#include <stdio.h>
#include <string>

using namespace std;

int words[10000] = { 0 };

int main(int argc, char** argv) {
	int i, j, n, m, command;
	char target;
	int remember = 0;
	char tmp[1000];

	scanf("%d %d", &n, &m);

	for (i = 0; i < 26; i++) remember += (1 << i);

	for (i = 0; i < n; i++) {
		j = 0;
		scanf("%s", tmp);

		while (tmp[j] != '\0') {
			int num = tmp[j++] - 'a';
			words[i] |= (1 << num);
		}
	}

	for (i = 0; i < m; i++) {
		int answer = 0;
		scanf("%d %c", &command, &target);
		remember ^= (1 << ((int)target - 'a')); // command 상관없이 뒤집으면 됨 (기억했었음/잊었었음이 보장되므로)
		
		for (j = 0; j < n; j++) {
			if ((words[j] & remember) == words[j]) answer++;
		}

		printf("%d\n", answer);
	}

	return 0;
}