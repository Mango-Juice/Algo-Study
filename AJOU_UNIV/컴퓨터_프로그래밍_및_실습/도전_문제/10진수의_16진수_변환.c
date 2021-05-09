#include <stdio.h>

char num_to_char(int n){
	if(n < 9) return 48 + n;
	else return 55 + n;
}

int main() {
	int inp;
	scanf("%d", &inp);
	printf("%c%c", num_to_char(inp/16), num_to_char(inp%16));
  return 0;
}
