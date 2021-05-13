#include <stdio.h>

int findCenter(int arr[300], int count){
	for(int i = 0; i < count; i ++){
		for(int j = i + 1; j < count; j ++) {
			if(arr[i] > arr[j]){
				int tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
		}
	}
	return arr[(count - 1) / 2];
}

int main() {
	int r, c;
	int h, w;
	int arr[300][300];
	int answer[300][300];
	scanf("%d %d", &c, &r);
	scanf("%d %d", &w, &h);
	
	for(int i = 0; i < w; i++){
		for(int j = 0; j < h; j++) scanf("%d", &arr[i][j]);
	}
	
	for(int i = 0; i < w; i++){
		for(int j = 0; j < h; j++){
			int tmp[260];
			int count = 0;
			for(int a = -1 * c / 2; a <= c / 2; a++){
				for(int b = -1 * r / 2; b <= r / 2; b++){
					if(i + a >= 0 && j + b >= 0 && i + a < w && j + b < h) tmp[count++] = arr[i + a][j + b]; 
					}
				}
			answer[i][j] = findCenter(tmp, count);
			}
	}
	
	for(int i = 0; i < w; i++){
		for(int j = 0; j < h; j++) printf("%4d", answer[i][j]);
		printf("\n");
	}
  return 0;
}
