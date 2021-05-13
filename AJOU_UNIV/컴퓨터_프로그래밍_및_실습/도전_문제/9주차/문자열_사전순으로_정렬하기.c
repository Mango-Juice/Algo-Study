#include <stdio.h>
#include <string.h>

int main() {
	int n;
	char arr[100][55];
	scanf("%d", &n);
	for(int i = 0; i < n; i ++){
		scanf("%s", arr + i);
	}
	
	for(int i = 0; i < n; i ++){
		for(int j = i + 1; j < n; j ++){
			if(strcmp(arr[i], arr[j]) > 0){
				char tmp[55];
				strcpy(tmp, arr[i]);
				strcpy(arr[i], arr[j]);
				strcpy(arr[j], tmp);
			}
		}
	}
	
	for(int i = 0; i < n; i ++){
		printf("%s\n", arr[i]);
	}
  return 0;
}
