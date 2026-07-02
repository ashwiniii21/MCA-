#include <stdio.h>

int main()

{

    int number, originalNumber, digit, reverse = 0;

    printf("Enter a number: ");

    scanf("%d", &number);

    originalNumber = number;

    while (number > 0)

    {

        digit = number % 10;

        reverse = reverse * 10 + digit;

        number = number / 10;

    }

    if (originalNumber == reverse)

    {

        printf("%d is a Palindrome number.\n", originalNumber);

    }

    else

    {

        printf("%d is not a Palindrome number.\n", originalNumber);

    }

    return 0;

}
