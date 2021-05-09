#include <stdio.h>

int char_to_num(char c){
	int tmp = c;
	if(tmp >= 65) tmp = c - 55;
	else tmp = c - 48;
	return tmp;
}

int main() {
	char inp[3];
	scanf("%s", inp);
	
	printf("%d", char_to_num(inp[0]) * 16 + char_to_num(inp[1]));
  return 0;
}
