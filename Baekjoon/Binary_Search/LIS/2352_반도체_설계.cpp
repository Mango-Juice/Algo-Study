#include <stdio.h>
#include <algorithm>

using namespace std;

int a[40001];
int lis[40001];

int main(void) {
    int n, i, length;
    scanf("%d", &n);
    
    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    for (i = 0, length = 0; i < n; i++) {
        auto lb = upper_bound(lis, lis + length + 1, a[i]);
		*lb = a[i];
        if (lb == lis + length + 1) length++;
    }

    printf("%d\n", length);
}
