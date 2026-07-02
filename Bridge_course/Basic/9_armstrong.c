#include <stdio.h>
#include <math.h>
int main() {
    long n, original, remainder, result = 0;
    int digits = 0;

    printf("Enter a number: ");
    scanf("%ld", &n);
    original = n;

    long temp = n;
    do {
        digits++;
        temp /= 10;
    } while (temp != 0);

    temp = n;
    do {
        remainder = temp % 10;
        result += (long) pow(remainder, digits);
        temp /= 10;
    } while (temp != 0);

    if (result == original)
        printf("%ld is an Armstrong number\n", original);
    else
        printf("%ld is not an Armstrong number\n", original);

    return 0;
}