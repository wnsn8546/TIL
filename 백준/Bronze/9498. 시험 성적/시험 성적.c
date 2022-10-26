#include<stdio.h>
int main(){
  int a;
  //int b;
  //double result; 
  scanf("%d",&a);
  //scanf("%d %d",&a,&b);
  if(100>=a&&a>=90)printf("A");
  if(90>a&&a>=80)printf("B");
  if(80>a&&a>=70)printf("C");
  if(70>a&&a>=60)printf("D");
  if(60>a)printf("F");

    return 0;
}