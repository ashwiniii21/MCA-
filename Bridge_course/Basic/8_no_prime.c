#include <stdio.h>

int main() {
    
    int n, i, isPrime = 1;
    
    printf("Enter a number: ");
    scanf("%d", &n);

    if (n <= 1) {
        isPrime = 0;
    } else {
        i = 2;
        while (i * i <= n) {
            if (n % i == 0) {
                isPrime = 0;
                break;
            }
            i++;
        }
    }

    if (isPrime)
        printf("%d is Prime\n", n);
    else
        printf("%d is Not Prime\n", n);

    return 0;
}