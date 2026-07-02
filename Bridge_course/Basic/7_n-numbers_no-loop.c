
#include <stdio.h>

int main()
{
    int n,i =1,num,sum=0;
    printf("How many nos ?");
    scanf("%d",&n);
    
    while (i <=n)
    {
        printf("Enter no %d: ",i);
        scanf("%d",&num);
        sum +=num;
        i++;
    }
     printf("sum = %d\n",sum);
    return 0;
}
