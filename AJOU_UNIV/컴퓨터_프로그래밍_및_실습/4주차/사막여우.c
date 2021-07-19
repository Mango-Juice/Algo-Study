#include <stdio.h>

int main() {
	int n, p, q;
	int ok=0, sum=0;
	scanf("%d %d %d", &n, &p, &q);
	for(int i=0; i<n; i++){
		int tmp;
		scanf("%d", &tmp);
		if(tmp<=p){
			ok++;
			sum+=tmp;
		}
	}
	printf("%d %d\n", ok, sum);
	printf("%s", sum<=q ? "YES" : "NO");
  return 0;
}
