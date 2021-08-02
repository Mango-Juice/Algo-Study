// https://www.acmicpc.net/problem/2096

#include <stdio.h>
#include <algorithm>

using namespace std;

int minimum[3];
int maximum[3];

int main() {
	int i, n, a, b, c;
	int new_max[3], new_min[3];

	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		scanf("%d %d %d", &a, &b, &c);
		if (i == 0) {
			minimum[0] = a; minimum[1] = b; minimum[2] = c;
			maximum[0] = a; maximum[1] = b; maximum[2] = c;
		}
		else {
			new_max[0] = a + max(maximum[0], maximum[1]);
			new_max[1] = b + max(max(maximum[0], maximum[1]), maximum[2]);
			new_max[2] = c + max(maximum[1], maximum[2]);
			new_min[0] = a + min(minimum[0], minimum[1]);
			new_min[1] = b + min(min(minimum[0], minimum[1]), minimum[2]);
			new_min[2] = c + min(minimum[1], minimum[2]);
			copy(new_max, new_max + 3, maximum);
			copy(new_min, new_min + 3, minimum);
		}
	}

	printf("%d %d", max(max(maximum[0], maximum[1]), maximum[2]), min(min(minimum[0], minimum[1]), minimum[2]));

	return 0;
}