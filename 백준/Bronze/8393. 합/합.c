#include<stdio.h>
int main(){
  int n;
  int i;
  //int a;
 // int b;
  int sum=0;
  scanf("%d",&n);
  

for(i=1;i<=n;i++)
{
    sum+=i;
}
printf("%d",sum);
    return 0;
}