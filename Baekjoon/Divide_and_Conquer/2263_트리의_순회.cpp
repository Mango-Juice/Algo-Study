// https://www.acmicpc.net/problem/2263

#include <stdio.h>

using namespace std;

int rootindex;
int inorder[100005];
int postorder[100005];
int index[100005];

void printPreOrder(int infrom, int into, int postfrom, int postto) {
	if (infrom > into || postfrom > postto) return;

	int rootidx = index[postorder[postto]];
	printf("%d ", postorder[postto]); // 루트

	printPreOrder(infrom, rootidx - 1, postfrom, postfrom + rootidx - infrom - 1); // L
	printPreOrder(rootidx + 1, into, postfrom + rootidx - infrom, postto - 1); // R
}

int main() {
	int i, n;
	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		scanf(" %d", inorder + i);
		index[inorder[i]] = i;
	}

	for (i = 0; i < n; i++) scanf(" %d", postorder + i);

	printPreOrder(0, n - 1, 0, n - 1);

	return 0;
}