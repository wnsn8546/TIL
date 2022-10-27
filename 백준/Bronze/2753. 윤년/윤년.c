#include<stdio.h>
int main(){
  int a;
  //int b;
  //double result; 
  scanf("%d",&a);
  //scanf("%d %d",&a,&b);
if((a%4==0&&a%100!=0)||a%400==0)
{
 printf("1");
}
else
printf("0");

    return 0;
}