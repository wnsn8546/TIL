#include<stdio.h>
int main(){
  int a;
  int b;

  scanf("%d",&a);
  scanf("%d",&b);
if(a>0&&b>0)printf("1");
if(a<0&&b>0)printf("2");
if(a<0&&b<0)printf("3");
if(a>0&&b<0)printf("4");

    return 0;
}