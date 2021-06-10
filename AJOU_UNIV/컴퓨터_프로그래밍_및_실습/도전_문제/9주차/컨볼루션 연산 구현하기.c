#include <stdio.h>

int main() {
	int filter_size_x, filter_size_y;
	int image_size_x, image_size_y;
	int answer_size_x, answer_size_y;
	int filter[256][256], image[256][256], answer[256][256];
	
	scanf("%d %d", &filter_size_x, &filter_size_y);
	for(int i = 0; i < filter_size_x; i++)
		for(int j = 0; j < filter_size_y; j++)
			scanf("%d ", &filter[i][j]);
	
	scanf("%d %d", &image_size_x, &image_size_y);
	for(int i = 0; i < image_size_x; i++)
		for(int j = 0; j < image_size_y; j++)
			scanf("%d ", &image[i][j]);
	
	answer_size_x = image_size_x - filter_size_x + 1;
	answer_size_y = image_size_y - filter_size_y + 1;
	
	for(int i = 0; i < answer_size_x; i++){
		for(int j = 0; j < answer_size_y; j++){
			int num = 0;
			
			for(int x = 0; x < filter_size_x; x++){
				for(int y = 0; y < filter_size_y; y++){
					num += image[i+x][j+y] * filter[x][y];
				}
			}
			
			answer[i][j] = num;
		}
	}
	
	for(int i = 0; i < answer_size_x; i++){
		for(int j = 0; j < answer_size_y; j++){
			printf("%6d", answer[i][j]);
		}
		printf("\n");
	}
	
  return 0;
}
