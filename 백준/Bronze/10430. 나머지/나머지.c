#include<stdio.h>
int main(){
  int a;
  int b;
  int c;
  scanf("%d %d %d", &a,&b,&c);
  printf("%d\n",(a+b)%c);
  printf("%d\n",((a%c)+(b%c))%c);
  printf("%d\n",(a*b)%c);
  printf("%d\n",((a%c)*(b%c))%c);
  printf("");
    return 0;
}