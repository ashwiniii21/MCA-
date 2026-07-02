#include <stdio.h>

int main()

{

    float kilometer, miles;

    printf("Enter speed in kilometers per hour: ");

    scanf("%f", &kilometer);

    miles = kilometer * 0.621371;

    printf("Speed in miles per hour = %.2f\n", miles);

    return 0;

}
