#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b, int c) {
    int count = 0;
	int interval = b - a > c - b ? b - a : c - b;
	count = interval - 1;
    return count;
}

int main()
{
	int a,b,c;
	scanf("%d %d %d",&a,&b,&c);
	printf("%d",solution(a,b,c));
	return 0;
}
