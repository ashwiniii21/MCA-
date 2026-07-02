#include <stdio.h>

int main()

{

    int num1, num2;

    printf("Enter the first number: ");

    scanf("%d", &num1);

    printf("Enter the second number: ");

    scanf("%d", &num2);

    while (num2 != 0)

    {

        num1--;

        num2--;

    }

    printf("Difference = %d\n", num1);

    return 0;

}
