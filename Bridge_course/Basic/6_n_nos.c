
#include <stdio.h>

int main()
{
    int n,i=1,sum=0;
    printf(" Enter n:");
    scanf("%d",&n);
    
    while (i<=n) {
        sum+=i;
        i++;
    }
    printf("sum of first %d numbers = %d\n",n,sum);
    return 0;
}