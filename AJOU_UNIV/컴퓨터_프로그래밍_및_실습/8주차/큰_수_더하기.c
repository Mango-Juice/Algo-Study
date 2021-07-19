#include <stdio.h>

int getSize(char arr[], int max){
	int idx = 0;
	while(idx <= max && arr[idx] != '\0') idx ++;
	return idx;
}

int main() {
	char num1[102], num2[102];
	int size1 = 0, size2 = 0;
	int upper = 0;
	int answer[102];
	
	scanf("%s %s", num1, num2);
	
	size1 = getSize(num1, 101);
	size2 = getSize(num2, 101);
	
	for(int i = size1 - 1, j = size2 - 1; i >= 0 || j >= 0; i--, j--){
		int n1 = i >= 0 ? (int) num1[i] - 48 : 0;
		int n2 = j >= 0 ? (int) num2[j] - 48 : 0;
		answer[i > j ? i : j] = (n1 + n2 + upper) % 10;
		upper = (n1 + n2 + upper) / 10;
	}
	
	if(upper > 0)printf("1");
	for(int i = 0; i < (size1 > size2 ? size1 : size2); i++) printf("%d", answer[i]);
	
  return 0;
}
