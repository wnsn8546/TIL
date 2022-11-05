#include<stdio.h>
int main(){
  int i;
  int j;
  int a;
  //int b;
  scanf("%d",&a);
  //scanf("%d %d",&a,&b);

for(i=a;i<a+1;i++)
{
  for(j=1;j<10;j++)
  {
    printf("%d * %d = %d\n",i,j,i*j);
  }

}

  
    return 0;
}