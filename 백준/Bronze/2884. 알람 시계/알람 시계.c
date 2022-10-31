#include<stdio.h>
int main(){
  int a;
  int b;

  scanf("%d %d",&a,&b);

  if(b-45>=0)
  {
    printf("%d %d",a,b-45);
  }
  else{
    if(a==0)
    {
      printf("23 %d",60-(45-b));
    }
    else
    {
      printf("%d %d",a-1,60-(45-b));
    }
  }
    return 0;
}