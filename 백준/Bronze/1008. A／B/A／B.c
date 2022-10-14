#include<stdio.h>
int main(){
  int a;
  int b;
  double result; 
  
  scanf("%d %d",&a,&b);
  result=(double)a/b;
  printf("%.15lf",result);

    return 0;
}