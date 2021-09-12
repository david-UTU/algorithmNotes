/* The Legendre Symbol Conditions
 * - L(a,p) = (a^((p-1)/2))%(p)
 *   If a =1, L(a,p) = 1
 *   If a%2 = 0, L(a,p) = L(a/2, p)*(-1)^(((p^2)-1))/8)
 *   If a%2 = 1 and a != 1, L(a,p) = L((p%a), a)*(-1^((a-1)*(p-1)/4))*/
#include <stdio.h>

int main() {
  int a, p, x;
  printf("What is the a value?\n");
  scanf("%d", &a);
  printf("What is the p value?\n");
  scanf("%d", &p);
  if(a == 1) {
    x = 1}
  else {
    
  }
}
