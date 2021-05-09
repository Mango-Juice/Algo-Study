#include <stdio.h>

unsigned long long gcd(unsigned long long a, unsigned long long b)
{ 
    return (a % b == 0 ? b : gcd(b,a%b));
}

int main() {
	int n;
	scanf("%d", &n);
	
	for(int i=0; i<n; i++){
		unsigned long long a, b, c, d, gcd_ab, gcd_cd, lcm_ab, lcm_cd, tmp;
		
		scanf("%lld %lld %lld %lld", &a, &b, &c, &d);
		gcd_ab = gcd(a, b), gcd_cd = gcd(c, d);
		lcm_ab = gcd_ab * (a/gcd_ab) * (b/gcd_ab), lcm_cd = gcd_cd * (c/gcd_cd) * (d/gcd_cd);
		tmp = gcd(lcm_ab, lcm_cd);
			
		printf("%lld %lld\n", gcd(gcd_ab, gcd_cd), tmp * (lcm_ab/tmp) * (lcm_cd/tmp));
	}
  return 0;
}
