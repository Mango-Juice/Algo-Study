#include <stdio.h>
#include <limits.h>

int main() {
	int max = INT_MIN, min = INT_MAX, min2 = INT_MAX;
	int toReturn = 0;
	for(int i=0; i<5; i++){
		int n;
		scanf("%d", &n);
		if(max < n) max = n;
		if(min > n) {
			min2 = min;
			min = n;
		}
		else if(min2 > n) min2 = n;
	}
	toReturn = max > min + min2 ? max : min + min2;
	printf("%d", toReturn);
  return 0;
}
