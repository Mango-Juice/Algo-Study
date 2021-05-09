#include <stdio.h>

int main() {
	float a, b;
	scanf("%f %f", &a, &b);
	float c = (int)(100*a/b+0.5);
	printf("%.2f", c/100);
  return 0;
}
