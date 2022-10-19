#include<stdio.h>
int main(){
  int a;
  int a1;
  int a2;
  int a3;
  int b;
  int b1;
  int b2;
  int b3;

  
  scanf("%d", &a);
  scanf("%d", &b);
  a1=a/100*100;
  a2=(a-a1)/10*10;
  a3=a-a/10*10;
  b1=b/100*100;
  b2=(b-b1)/10*10;
  b3=b-b/10*10;
  printf("%d\n",a*b3);
  printf("%d\n",a*b2/10);
  printf("%d\n",a*b1/100);
  printf("%d\n",a*b);

    return 0;
}