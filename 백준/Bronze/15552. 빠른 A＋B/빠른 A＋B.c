#include<stdio.h>
int main(){
  int n;
  int i;
  int a;
  int b;
  //int sum=0;
  scanf("%d",&n);
  

for(i=0;i<n;i++)
{
  scanf("%d %d",&a,&b);
  printf("%d\n",a+b);
}

    return 0;
}