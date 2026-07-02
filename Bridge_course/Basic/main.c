#include <stdio.h>

int main ()
{
    int n ,i=1;
    printf("Enter a no : ");
    scanf("%d", &n);
    
    while (i <=10){
        printf("%d* %d = %d\n", i, n, i*n);
        i++;
    }
    return 0;

}